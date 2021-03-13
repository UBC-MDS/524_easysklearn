# import libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


def eda(input_file, target):
    """This function takes dataframe with numeric and non numeric variables splits the data into train and test dataframe, provides
    statistical summary of the numeric variables for a dataframe. This also provides imbalance data information.
    Additonally, the function plots a correlation matrix of each numeric variable.

    Parameters
    -----------
    dataframe: `pandas.DataFrame`
    The dataframe to be inspected.

    Returns
    --------
    Dictionery
    a dictionery of a statistical summary of the all variables as a
    `pandas.Dataframe` and a grid of `seaborn` plot containing
    correlation matrix

    Examples
    ---------
    >>> import pandas as pd
    >>> gen_data = pd.DataFrame()
    >>>gen_data["num1"] = [9.4, 8, 9.1, 9.3, 9.4]
    >>>gen_data["num2"] = [0.91, 0.92, 0.93 , 0.94 , 0.95]
    >>>gen_data["num3"] = [0.56, 0.68, 0.65, 0.59, 0.51]
    >>>gen_data["num4"] = [0.072, 0.098, 0.092, 0.075, 0.076]
    >>>gen_data["cat1"] = ["Good","Bad","Excellent","Ok","Good"]
    >>>gen_data["target"] = [1,2,2,3,1]
    >>>res = eda(gen_data,"target")
    >>>res
    """

    # def eda(input_file, target):
    # Check the dataframe input
    if not isinstance(input_file, pd.DataFrame):
        raise Exception(
            "The value of the argument 'dataframe' "
            + "should be of type pandas dataframe."
        )

    results = {}
    train_df, test_df = train_test_split(input_file, test_size=0.2, random_state=123)

    results = {
        "head": train_df.head(3),
        "tail": train_df.tail(3),
        "shape": train_df.shape,
        "data_info_num": train_df.select_dtypes("number").columns.to_list(),
        "data_info_cat": list(
            set(list(train_df.columns))
            - set(train_df.select_dtypes("number").columns.to_list())
        ),
        "data_character": train_df.describe(include="all"),
        "imbalance": train_df["target"].value_counts(normalize=False, dropna=True),
        "correlation": sns.heatmap(
            train_df.corr(),
            annot=True,
            vmin=-1,
            vmax=1,
            center=0,
            cmap="coolwarm",
            linewidths=3,
            linecolor="black",
        ),
    }

    return results
