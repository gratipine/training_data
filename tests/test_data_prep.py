from unittest import TestCase
import pandas as pd

from src.data_prep import get_line_edges, get_stations_in_line


class TestingTransportLines(TestCase):
    def test_transformer_gives_back_line_edges(self):
        input = [{
            'lineId': 'hammersmith-city',
            'lineName': 'Hammersmith & City',
            'branches': [
                {"branchName": 'Sittingbourne  &harr;  Sheerness-on-Sea ',
                 "stationIds": []},
                {"branchName": 'Strood  &harr;  Tonbridge ',
                 "stationIds": []}]
        }]
        expected = pd.DataFrame([
            ["Sittingbourne", "Sheerness-on-Sea", "Hammersmith & City"],
            ["Strood", "Tonbridge", "Hammersmith & City"]
        ], columns=["line_start", "line_end", "line_name"])

        result = get_line_edges(input)
        pd.testing.assert_frame_equal(result, expected)

    def test_transformer_gives_back_line_edges_no_spaces(self):
        input = [{
            'lineId': 'hammersmith-city',
            'lineName': 'Hammersmith & City',
            'branches': [
                {"branchName": 'London Victoria&harr;Sevenoaks',
                 "stationIds": []},
                {"branchName": 'Strood  &harr;  Tonbridge ',
                 "stationIds": []}]}]
        expected = pd.DataFrame([
            ["London Victoria", "Sevenoaks", "Hammersmith & City"],
            ["Strood", "Tonbridge", "Hammersmith & City"]
        ], columns=["line_start", "line_end", "line_name"])

        result = get_line_edges(input)
        pd.testing.assert_frame_equal(result, expected)

    def test_getting_branches_form_dictionary(self):
        input = [{
            'lineId': 'hammersmith-city',
            'lineName': 'Hammersmith & City',
            'branches': [
                {"branchName": 'London Victoria&harr;Sevenoaks',
                 "stationIds": ["940GZZLUEHM", "940GZZLUEHA"]},
                {"branchName": 'Strood  &harr;  Tonbridge ',
                 "stationIds": ["940GZZLUEHM", "940GZZLUEHA"]}]}]
        expected = pd.DataFrame([
            ["London Victoria", "Sevenoaks", "Hammersmith & City", "940GZZLUEHM"],
            ["London Victoria", "Sevenoaks", "Hammersmith & City", "940GZZLUEHA"],
            ["Strood", "Tonbridge", "Hammersmith & City", "940GZZLUEHM"],
            ["Strood", "Tonbridge", "Hammersmith & City", "940GZZLUEHA"]
        ], columns=["line_start", "line_end", "line_name", "station_id"])

        result = get_stations_in_line(input)
        pd.testing.assert_frame_equal(result, expected)