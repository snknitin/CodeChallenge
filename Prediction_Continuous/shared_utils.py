import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

IMAGES_PATH=os.path.join(os.getcwd(),"static/")
if not os.path.exists(IMAGES_PATH):
        os.makedirs(IMAGES_PATH)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


def load():
    """
    Loads the dataset
    """
    # step 1: Load the data and include column headers
    data_file = os.path.join(os.getcwd(), "data/cal_housing.txt")
    dataframe_all = pd.read_csv(data_file, sep=",")
    # convert object type to float64
    dataframe_all = dataframe_all.convert_objects(convert_numeric=True)

    num_rows = dataframe_all.shape[0]

    # Calculate number of features. -1 because we are saving one as the target variable (Benign or malignant)
    n_features = dataframe_all.shape[1] - 1

    # Print the results
    print("Total number of cases: {}".format(num_rows))
    print("Number of features: {}".format(n_features))

    columns = dataframe_all.columns
    print(columns)

    # Divide by 1.5 to limit the number of income categories
    dataframe_all["income_cat"] = np.ceil(dataframe_all["median_income"] / 1.5)
    # Label those above 5 as 5
    dataframe_all["income_cat"].where(dataframe_all["income_cat"] < 5, 5.0, inplace=True)

    return dataframe_all