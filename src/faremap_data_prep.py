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