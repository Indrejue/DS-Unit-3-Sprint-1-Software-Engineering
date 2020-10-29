import unittest

from mod1_examp import *

class DataFrameTests(unittest.TestCase):
    """Tests for the usability of Data wrangling function"""
    def setUp(self):
        df1 = pd.read_csv(
            'https://raw.githubusercontent.com/Indrejue/'
            'DS-Unit-2-Applied-Modeling/master/data/burritos/'
            'burritos.csv',
            parse_dates=['Date'])
        cols = df1.columns
        values = df1.values
        self.testdf = MyDataFrame(columns=cols,data=values)

    def test_null(self):
        """Testing the Null function is counting the nulls"""
        self.assertEqual(self.testdf.nulls(), 18256)

    def test_month_cols(self):
        """Testing to see if a months column is added to the DF"""
        self.assertIn('month',self.testdf.date_split())

if __name__ == "__main__":
    unittest.main()