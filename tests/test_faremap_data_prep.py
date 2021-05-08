from unittest import TestCase
import pandas as pd
import copy

import src.faremap_data_prep as fdp


class FaremapDataPrep(TestCase):
    def test_lines_tranformation(self):
        line_dictionary = {
            "branchName": "Tree of life",
            "stationIds": ["id_1", "id_2", "id_3"]
        }

        expected = pd.DataFrame({
            "branch_name": ["Tree of life", "Tree of life", "Tree of life"],
            "station_ids": ["id_1", "id_2", "id_3"]
        })

        result = fdp.line_to_dt(dictionary_with_lines=line_dictionary)
        result.sort_index(axis=1, inplace=True)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_json_prices_to_dt(self):
        input_station_id = "dummy_id"
        dest_station_1_list = [
            {'price': 2710,
             'offPeakOnly': False,
             'ticketName': 'SDS ANYTIME DAY S   ',
             'isDefaultRoute': True,
             'isTFL': False,
             'routeDescription': 'ANY PERMITTED'},
            {'price': 2090,
             'offPeakOnly': False,
             'ticketName': 'SDS ANYTIME DAY S   ',
             'isDefaultRoute': True,
             'isTFL': False,
             'routeDescription': 'VIA NARNIA'},
             {'hops': [],
              'price': 1840,
              'offPeakOnly': False,
              'ticketName': 'Split Ticket',
              'isDefaultRoute': False,
              'isTFL': False,
              'routeDescription': 'Via countryside'},
        ]

        dest_2_list = copy.deepcopy(dest_station_1_list[0:2])
        dest_2_list[0]["price"] = 1900

        input_json = {
            "fromId": input_station_id, 
            "fares": {
                "dest_station_1": dest_station_1_list,
                "dest_station_2": dest_2_list
            }

        }
        stations = pd.DataFrame({
            "station_id": 
                ["dest_station_1", "dest_station_2", input_station_id],
            "station_name": 
                ["First Station", "Second Station", "Origin"]
        })
        result = fdp.json_prices_to_dt(input_json, stations)
        expected = pd.DataFrame([
            ["dest_station_1", 2710, True, "ANY PERMITTED", False, 
            "First Station", input_station_id, "Origin"],
            ["dest_station_1", 2090, True, 'VIA NARNIA', False, 
            "First Station", input_station_id, "Origin"],
            ["dest_station_2", 1900, True, "ANY PERMITTED", False, 
            "Second Station", input_station_id, "Origin"],
            ["dest_station_2", 2090, True, 'VIA NARNIA', False, 
            "Second Station", input_station_id, "Origin"],
        ], columns=[
            "station_id", "price", "isDefaultRoute", 
            "routeDescription", "offPeakOnly", "station_name", 
            "from_station_id", "from_station_name"])
        print(expected)
        print(result)
        pd.testing.assert_frame_equal(
            expected, result.iloc[::-1].reset_index(drop=True))