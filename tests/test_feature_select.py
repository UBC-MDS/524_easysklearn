from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from feature_select import feature_select
import numpy as np
import pandas as pd

def test_feature_select():
    """
    This test imports the Boston dataset which has 13 features. Applying
    the forward selection algorithm for feature selection with the default
    threshold of 0.05, the function selects two features.
    """
    boston = load_boston()
    bos = pd.DataFrame(boston.data, columns = boston.feature_names)
    bos['Price'] = boston.target
    X_train = bos.drop("Price", 1)       
    y_train = bos['Price']              

    best_features = feature_select(X_train, y_train)
    
    # output length 
    assert len(best_features) == 2
    assert len(best_features) < len(X_train.columns.tolist())
    
    # output type
    assert isinstance(best_features, list)
    assert isinstance(best_features[0], str)