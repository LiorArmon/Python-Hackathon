from enum import Enum
import pandas as pd
import xlrd
from pathlib import Path
import numpy as np
import csv


class Tag(Enum):
    NO_GO = "no go"
    GO = "go"
    S_H = "sanity high"
    S_L = "sanity low"
    NO_SHOW = "no show"


class Sort_By_BDM:
    """
    This class reads a text file of BSM results and excel file of keys of tagging by ranking and
    creates a sorted DataFrame with the snack image name as index.
    the columns of the DataFrame are ranking (1 for the highest Bid), Bid (score by BDM),
    tag (Enum object), show (boolean) and cued (boolean)
    Other attributes: the full text file name, the full excel file name and key DataFrame with
    ranking as index, a tag column (string) and enum_col (Tags)
    """
    def __init__(self, text_file_path, key_file_path):
        self.text_file_path = Path(text_file_path)
        self.key_file_path = Path(key_file_path)
        self.sorted_df = None
        self.key_df = None

    def create_full_df(self):
        self._read_BDM_results()
        self._read_keys_file()
        self._disp_changes()
        self._add_beep_and_show_cols()
        self._validate_df_is_full()
        return self.sorted_df

    def _read_BDM_results(self):
        """
        reads the BDM results text file and return a DataFrame with snacks' image names as index and Bid column
        the returned DataFrame is sorted by Bid, descending values
        """
        with open(self.text_file_path) as file:
            df = pd.read_table(file, index_col=0)
        # creating a dataframe with the stimulus name as index (image name) and sorted by ranking
        df.set_index('StimName', inplace=True)
        df.pop('RT')
        self.sorted_df = df.sort_values('Bid', ascending=0)

    def _read_keys_file(self):
        """
        reads an excel keys file that contain a ranking column and tag column
        returns a DataFrame with ranking as index and a tag column
        """
        xl = pd.ExcelFile(self.key_file_path)
        key_df = xl.parse()
        key_df.set_index('ranking', inplace=True)
        # adds a column with the Tag object to use instead of the strings
        key_df['enum_col'] = key_df.tag.apply(lambda x: Tag(x))
        self.key_df = key_df

    def _disp_changes(self):
        # adds a column of tag to sorted_df
        self.sorted_df['tag'] = self.key_df['enum_col'].tolist()
        # adds a column of ranking
        self.sorted_df.insert(loc=0, column='ranking', value=self.key_df.index.values)

    def _add_beep_and_show_cols(self):
        # adds a boolean columns that indicate if we should show a snack and if its cued
        self.sorted_df['show'] = self.sorted_df.tag.apply(lambda x: x.name != 'NO_SHOW')
        self.sorted_df['cued'] = self.sorted_df.tag.apply(lambda x: x.name == 'GO')


    def _validate_df_is_full(self):
        # verifying the dataframe has no null values
        if self.sorted_df.isnull().values.any():
            raise IndexError('The snacks of the BDM and the Excel file do not match')

if __name__ == '__main__':
    # reading the results of the BDM
    p = r'C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon\Only_6_snacks.txt'
    file_path = Path(p)

    # reading and creating a dataframe with tag for each position of the sorted ranking
    key_p = r'C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon\Only_6_snacks_ladder_key.xlsx'
    key_p = Path(key_p)
    print(key_p)
    A = Sort_By_BDM(file_path, key_p)
    print(A.create_full_df())

    A.sorted_df.to_csv('Only_6_sorted_BDM_mock_data.csv')
