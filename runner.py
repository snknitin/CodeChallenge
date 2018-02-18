import argparse
import os

import data_visualization as dv
import shared_utils as su


parser = argparse.ArgumentParser()
parser.add_argument("data_directory", help="location of the dataset",type=str)

args = parser.parse_args()


class Solution(object):
    def prepare_data(self,filepath):
        self.filepath=filepath
        input_file = os.path.join(self.filepath, "Autism-Adult-Data.arff")
        output_file = os.path.join(self.filepath, "dataframe.pkl")
        su.arff_to_df(input_file, output_file)
        dv.preprocess(output_file)






if __name__ == '__main__':
    s = Solution()
    print("Loading the dataset at %s" %(args.data_directory))

