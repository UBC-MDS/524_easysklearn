from easysklearn.baseline_fun import baseline_fun
import pandas as pd
import sklearn.datasets as datasets
import pytest


def data_setup():
    """
    import Iris dataset for testing
    """

    iris = datasets.load_iris(return_X_y=True)
    X = pd.DataFrame(iris[0])
    y = pd.DataFrame(iris[1])
    score_r = baseline_fun(X, y)
    score_c = baseline_fun(X, y, type="classification")

    return (X, y, score_r, score_c)


def test_input_exception():
    """
    To test whether the input exceptions works
    """

    X, y, score_r, score_c = data_setup()

    with pytest.raises(TypeError):
        baseline_fun(X, y, type="class")

    with pytest.raises(TypeError):
        baseline_fun(1, y, type="class")

    with pytest.raises(TypeError):
        baseline_fun(X, 1, type="class")

    with pytest.raises(KeyError) as exc:
        baseline_fun(X, y, metrics_1="square error")
    assert (
        str(exc.value)
        == "'Please check sklearn.metrics.SCORERS.keys() to get valid options'"
    )

    with pytest.raises(KeyError) as exc:
        baseline_fun(X, y, metrics_2="square error")
    assert (
        str(exc.value)
        == "'Please check sklearn.metrics.SCORERS.keys() to get valid options'"
    )

    return


def test_output():
    """
    Test the output of the basline_fun().
    Raises assertion errors if tests fail
    """
    X, y, score_r, score_c = data_setup()

    assert score_r.shape == (4, 2)
    assert score_c.shape == (4, 2)
    assert (score_r.keys() == ["DummyRegressor", "LinearRegression"]).all()
    assert (score_c.keys() == ["DummyClassifier", "LogisticRegression"]).all()
    assert (
        score_r.index == ["fit_time", "score_time", "test_score", "train_score"]
    ).all()
    assert (
        score_c.index == ["fit_time", "score_time", "test_score", "train_score"]
    ).all()

    return
