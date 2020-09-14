import pandas as pd

def create_records_table(relevant_dictionary: dict, table_with_records: pd.DataFrame, lengths_of_records: pd.Series):
    lengths_of_record_type = relevant_dictionary.get("length")
    
    records_of_specified_type = table_with_records[
        lengths_of_records == lengths_of_record_type].copy()
    
    for key, pair_indices in relevant_dictionary.get("records").items():
        records_of_specified_type[key] = (
            records_of_specified_type["records"]
            .str[pair_indices[0]:pair_indices[1]]
        )
    
    records_of_specified_type = records_of_specified_type[
        records_of_specified_type["record_type"] == relevant_dictionary.get("record_type")]
    
    return records_of_specified_type