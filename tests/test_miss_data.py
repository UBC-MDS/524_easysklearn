from easysklearn.miss_data import miss_data
import pandas as pd
import numpy as np
from pytest import raises


x_train = pd.DataFrame(
    np.array(
        [
            [4500, np.nan, 4],
            [3450, 350_000, 6],
            [2000, 450_000, np.nan],
            [np.nan, 800_000, 9],
        ]
    ),
    columns=["size", "price", "bedrooms"],
)


x_test = pd.DataFrame(
    np.array(
        [
            [2500, np.nan, 4],
            [5000, 750_000, 4],
            [2000, 450_000, np.nan],
            [np.nan, 1_200_000, 5],
        ]
    ),
    columns=["size", "price", "bedrooms"],
)


def test_input_data():

    with raises(TypeError):
        miss_data(x_train, x_test, strategy="sum")

    with raises(TypeError):
        miss_data(1, x_test, strategy="mean")

    with raises(TypeError):
        miss_data(x_train, 1, strategy="mean")

    with raises(TypeError):
        miss_data(x_train, x_test, strategy=2)


def test_output_result():

    x_train_imp_mean, x_test_imp_mean = miss_data(x_train, x_test, strategy="mean")

    x_train_imp_med, x_test_imp_med = miss_data(x_train, x_test, strategy="median")

    assert x_train_imp_mean.shape == (
        4,
        3,
    ), "output train dataframe has the desired shape"
    assert x_test_imp_mean.shape == (
        4,
        3,
    ), "output test dataframe has the desired shape"
    assert (
        x_train_imp_mean["price"][0] == 800000.0
    ), "Imputed mean value in the output train dataframe is valid"
    assert (
        x_test_imp_mean["size"][3] == 3166.6666666666665
    ), "Imputed mean value in the output test dataframe is valid"
    assert (
        x_train_imp_med["price"][0] == 750000.0
    ), "Imputed median value in outtput train dataframe is valid"
    assert (
        x_test_imp_med["size"][3] == 2500.0
    ), "Imputed median value in the output test dataframe is valid"
