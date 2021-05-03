from unittest import TestCase
import pandas as pd

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
