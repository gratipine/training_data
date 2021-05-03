import unittest
import pandas as pd

import src.faremap_data_prep as fdp

class Faremap_data_prep(unittest.TestCase):
    def lines_tranformation(self):

        line_dictionary = {
            "branchName": "Tree of life",
            "stationIds": ["id_1", "id_2", "id_3"]
        }

        expected = pd.DataFrame({
            "branch_name": ["Tree of life"],
            "station_ids": ["id_1", "id_2", "id_3"]
        })

        result = fdp.line_to_dt(line_dictionary)

        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
