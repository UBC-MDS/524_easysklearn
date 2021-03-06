import pandas as pd
import sklearn
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_validate


def baseline_fun(
    X_train, y_train, type="regression", metrics_1="accuracy", metrics_2="r2"
):
    """
    Gives the scoring metrics of sklearn DummyRegressor and LinearRegression or sklearn DummyClassifier and LogisticRegression.

    Parameters
    ----------
    X_train : Pandas DataFrame
            The train set dataframe.

    y_train : Pandas DataFrame
            The target of train set dataframe.

    type: string
            What kind of supervised machine learning to use, regression or classification:

            If “regression”, then DummyRegressor and LinearRegression would be used.

            If “classification", then DummyClassifier and LogisticRegression would be used.

    metrics_1: string
            What kind of score metrics to use for classification problem, the default one is accuracy.
            Use sorted(sklearn.metrics.SCORERS.keys()) to get valid options.

    metrics_2: string
            What kind of score metrics to use for regression problem, the default one is r2
            Use sorted(sklearn.metrics.SCORERS.keys()) to get valid options.

    Return
    -------
    score : Pandas DataFrame
            The DataFrame contains the mean of fit time, score time, training score and validation score by 5-fold cross validation for both two models.

    Examples
    --------
    >>> from easysklearn.baseline_fun import baseline_fun

    >>> import pandas as pd

    >>> import sklearn.datasets as datasets

    >>> iris = datasets.load_iris(return_X_y=True)

    >>> X = pd.DataFrame(iris[0])

    >>> y = pd.DataFrame(iris[1])

    >>> baseline_fun(X, y, type = 'regression', metrics = 'neg_root_mean_squared_error')
            DummyRegressor	LinearRegression
    fit_time	0.002573	0.003994
    score_time	0.002200	0.002614
    test_score	-0.882971	-0.244363
    train_score	-0.790971	-0.209256
    """

    # input test
    if not isinstance(X_train, pd.DataFrame):
        raise TypeError("Input X should be a data frame")

    if not isinstance(y_train, pd.DataFrame):
        raise TypeError("Input y should be a data frame")

    if type not in ["regression", "classification"]:
        raise TypeError(
            "Please check what kind of supervised machine learning to use, regression or classification"
        )

    if metrics_1 not in sklearn.metrics.SCORERS.keys():
        raise KeyError(
            "Please check sklearn.metrics.SCORERS.keys() to get valid options"
        )

    if metrics_2 not in sklearn.metrics.SCORERS.keys():
        raise KeyError(
            "Please check sklearn.metrics.SCORERS.keys() to get valid options"
        )

    # fit data into the model
    score = {}
    if type == "regression":
        dr_score = cross_validate(
            DummyRegressor(),
            X_train,
            y_train,
            return_train_score=True,
            scoring=metrics_2,
        )
        lr_score = cross_validate(
            LinearRegression(),
            X_train,
            y_train,
            return_train_score=True,
            scoring=metrics_2,
        )
        score["DummyRegressor"] = pd.DataFrame(dr_score).mean()
        score["LinearRegression"] = pd.DataFrame(lr_score).mean()
    if type == "classification":
        dc_score = cross_validate(
            DummyClassifier(),
            X_train,
            y_train,
            return_train_score=True,
            scoring=metrics_1,
        )
        lr_score = cross_validate(
            LogisticRegression(),
            X_train,
            y_train,
            return_train_score=True,
            scoring=metrics_1,
        )
        score["DummyClassifier"] = pd.DataFrame(dc_score).mean()
        score["LogisticRegression"] = pd.DataFrame(lr_score).mean()

    return pd.DataFrame(score)
