import pandas as pd
import config.indices_of_records as dicts

def create_columns_out_of_indices(
    relevant_dictionary: dict,
    records_of_specified_type: pd.DataFrame):
    
    for key, pair_indices in relevant_dictionary.get("records").items():
        records_of_specified_type[key] = (
            records_of_specified_type["records"]
            .str[pair_indices[0]:pair_indices[1]]
        )
    
    return records_of_specified_type

def create_records_table(
    relevant_dictionary: dict, table_with_records: pd.DataFrame, lengths_of_records: pd.Series):
    
    lengths_of_record_type = relevant_dictionary.get("length")
    
    records_of_specified_type = table_with_records[
        lengths_of_records == lengths_of_record_type].copy()
    
    records_of_specified_type = create_columns_out_of_indices(
        relevant_dictionary, records_of_specified_type)
    
    records_of_specified_type = records_of_specified_type[
        records_of_specified_type["record_type"] == relevant_dictionary.get("record_type")]
    
    return records_of_specified_type


def prep_locations_tables(files_pattern):
    locations_file = pd.read_table(f"../data/{files_pattern}/{files_pattern}.LOC")
    
    locations_file.rename(
    columns={'/!! Start of file                            ' +
             '                                   ':"records"},
    inplace=True)
    
    lengths_of_records_locations = locations_file["records"].str.len()
    
    locations_records = create_records_table(
        relevant_dictionary=dicts.dictionary_locations,
        table_with_records=locations_file, 
        lengths_of_records=lengths_of_records_locations)
    
    synonym_records = create_records_table(
        relevant_dictionary=dicts.dict_synonym,
        table_with_records=locations_file, 
        lengths_of_records=lengths_of_records_locations)
    
    return locations_records, synonym_records


def prep_fares_table(files_pattern):
    flow_data = pd.read_table(f"../data/{files_pattern}/{files_pattern}.FFL")
    flow_data.rename(columns={
        "/!! Start of file                               " + 
        "                                ":"records"}, inplace=True)
    
    lengths_of_records = flow_data["records"].str.len()
    
    flow_records = create_records_table(
    relevant_dictionary=dicts.dict_flow_records,
    table_with_records=flow_data, 
    lengths_of_records=lengths_of_records)
    
    
    fare_records = create_records_table(
    relevant_dictionary=dicts.dict_fare_records,
    table_with_records=flow_data, 
    lengths_of_records=lengths_of_records)
    
    merged_data = flow_records.merge(
    fare_records,
    on=["flow_id", "update_marker"])
    
    return merged_data


def prep_routes_tables(files_pattern):
    routes_file = pd.read_table(f"../data/{files_pattern}/{files_pattern}.RTE")
    
    routes_file.rename(
    columns={'/!! Start of file                            ' + 
             '                                   ':"records"},
    inplace=True)
    
    lengths_of_records_routes = routes_file["records"].str.len()
    
    routes_records = create_records_table(
    relevant_dictionary=dicts.dict_routes,
    table_with_records=routes_file, 
    lengths_of_records=lengths_of_records_routes)

    route_excl_records = create_records_table(
    relevant_dictionary=dicts.dict_route_exclusions,
    table_with_records=routes_file, 
    lengths_of_records=lengths_of_records_routes)

    return routes_records, route_excl_records


def combine_fares_and_routes(merged_data, routes_records):
    routes_with_fares = merged_data.merge(routes_records, on=["route_code", "update_marker"], how="left")
    
    routes_with_fares_filtered = routes_with_fares.drop([
    "records_x", "record_type_x", "records_y", "record_type_y", "records",
    "record_type", "end_date_x", "end_date_y", "start_date_x", "start_date_y"], axis=1)
    
    return routes_with_fares_filtered


def combine_fares_routes_locations(routes_with_fares_filtered, locations_records):
    routes_fares_descriptions = routes_with_fares_filtered.merge(
    locations_records[["nlc_code", "description"]].drop_duplicates(),
    left_on="origin_code", right_on="nlc_code", how="left"
    )
    print(len(routes_fares_descriptions))
    routes_fares_descriptions.rename(columns={
    "description_x":"route_description",
    "description_y":"origin_station"}, inplace=True)

    routes_fares_descriptions = routes_fares_descriptions.merge(
        locations_records[["nlc_code", "description"]].drop_duplicates(),
        left_on="destination_code", right_on="nlc_code",
        suffixes=["_origin", "_destination"], how="left" 
    )
    print(len(routes_fares_descriptions))
    
    return routes_fares_descriptions


def prep_single_record_type_in_file_table(files_pattern, dictionary_types, file_ending):
    data_in = pd.read_table(
        f"../data/{files_pattern}/{files_pattern}.{file_ending}",
        skipfooter=1, engine="python", names=["records"], header=5)
    
    data_in = create_columns_out_of_indices(
        relevant_dictionary=dictionary_types,
        records_of_specified_type=data_in)
    
    return data_in


def get_line_edges(input_list):
    out = pd.DataFrame()

    for element in input_list:
        line_name = list(element.items())[1][1]
        branches_in_both_directions = list(element.items())[2][1]
        
        for direction in branches_in_both_directions:
            direction_name = direction.get("branchName").split("&harr;")
            direction_name.append(line_name)

            out = pd.concat([out, pd.DataFrame([direction_name])])

    out.rename(
        columns={0: "line_start", 1: "line_end", 2: "line_name"},
        inplace=True)
    out.reset_index(drop=True, inplace=True)
    
    out["line_start"] = out["line_start"].str.strip()
    out["line_end"] = out["line_end"].str.strip()

    return out


def get_stations_in_line(input_list):
    out = pd.DataFrame()

    for element in input_list:
        line_name = list(element.items())[1][1]
        branches_in_both_directions = list(element.items())[2][1]

        for direction in branches_in_both_directions:
            direction_name = direction.get("branchName").split("&harr;")
            direction_name.append(line_name)

            stations = pd.DataFrame(direction.get("stationIds"))
            stations.rename(inplace=True, columns={0: "station_id"})
            stations["merge"] = 1
            temp = pd.DataFrame([direction_name])
            temp["merge"] = 1
            temp = temp.merge(stations, on="merge").drop("merge", axis=1)

            out = pd.concat([out, temp])

    out.rename(
        columns={0: "line_start", 1: "line_end", 2: "line_name"},
        inplace=True)
    out.reset_index(drop=True, inplace=True)

    out["line_start"] = out["line_start"].str.strip()
    out["line_end"] = out["line_end"].str.strip()

    return out