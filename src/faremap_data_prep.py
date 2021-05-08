import pandas as pd


def prep_stations(stations_json):
    stations = pd.DataFrame()
    for item in stations_json:
        temp = pd.DataFrame({
            "station_id": item.get("stationId"),
            "station_name": item.get("stationName")
        }, index=[0])
        stations = pd.concat([stations, temp])

    return stations


def line_to_dt(dictionary_with_lines):
    out = pd.DataFrame(dictionary_with_lines.get("stationIds"), columns=["station_ids"])
    out["branch_name"] = dictionary_with_lines.get("branchName")
    return out

def json_prices_to_dt(input_json, stations):
    station_id = input_json.get("fromId")
    out = pd.DataFrame()
    for key in sorted(input_json.get("fares").keys()):
        dictionary_of_station = input_json.get("fares").get(key)

        for ticket in dictionary_of_station:
            if ticket.get("ticketName") == 'SDS ANYTIME DAY S   ':
                temp = pd.DataFrame({
                    "station_id": key,
                    "price": ticket.get("price"),
                    "isDefaultRoute": ticket.get("isDefaultRoute"),
                    "routeDescription": ticket.get("routeDescription"),
                    "offPeakOnly": ticket.get("offPeakOnly")
                }, index=[0])

                out = pd.concat([temp, out])

    explanatory_table = out.merge(stations)
    explanatory_table["from_station_id"] = station_id
    explanatory_table["from_station_name"] = str(stations.loc[
        stations["station_id"] == station_id, "station_name"].values[0])

    return explanatory_table