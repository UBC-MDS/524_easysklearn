import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def feature_select(X_train, y_train, threshold=0.05):
    """
    Performs forward selection of features in the data by starting with an empty model, 
    and iteratively adds features that improve the model's score. The algorithm stops once 
    the increase of the accuracy from an additional features is smaller than the threshold.

    Parameters
    ----------
    X_train : Pandas DataFrame
              The training set of the data.

    y_train : Pandas DataFrame
              The target of the data.

    threshold : int (default=None)
                user input threshold used for stopping criteria.
    Returns
    -------
    result : Pandas DataFrame
             A DataFrame containing the selected features, i.e. the best features in the model       
    Examples
    --------
    >>> from easysklearn import feature_select
    >>> from sklearn.linear_model import LinearRegression

    >>> feature_select(X_train, y_train, threshold=None)
    """

    # exception handling
    if len(X_train.shape) != 2:
        raise ValueError('X_train must be 2-dimensional.')

    if len(y_train.shape) != 1:
        raise ValueError('y_train must be 1-dimensional.')

    if X_train.shape[0] != y_train.shape[0]:
        raise ValueError(f'X_train and y_train have a dimensions mismatch: '
                         '[{X_train.shape[0]}, {y_train.shape[0]}]')

    initial_features = X_train.columns.tolist()
    best_features = []
    scores = []
    max_features = X_train.shape[1]
    previous = 0

    for j in range(0, max_features):
        remaining_features = list(set(initial_features)-set(best_features))
        temp = pd.Series(index=remaining_features, dtype='float64')
        for temp_feature in remaining_features:

            model = LinearRegression().fit(
                X_train[best_features+[temp_feature]], y_train)
            temp[temp_feature] = 1 - \
                model.score(X_train[best_features+[temp_feature]], y_train)

        min_value = temp.min()
        scores.append(min_value)

        # Stopping Criteria: Based on threshold
        if (j > 1):
            previous = sorted(np.array(scores))[1]
            if(((previous - np.min(scores)) / previous) >= threshold):
                break
        best_features.append(temp.idxmin())
    return best_features
