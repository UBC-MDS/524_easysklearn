from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from easysklearn.feature_select import feature_select
import numpy as np
import pandas as pd
import pytest

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

def test_feature_input():
    """
<<<<<<< Updated upstream
    This test function tests the input exceptions of feature_select() 
    """  
    df = pd.DataFrame(np.random.randint(0,10,size=(10, 5)), columns=list('ABCDE')) 
    one_d_array = pd.Series(np.random.rand(10,))
    random_array = pd.Series(np.random.rand(11,))
    
=======
    This test function tests the input exceptions of feature_select()
    """
    df = pd.DataFrame(np.random.randint(0, 10, size=(10, 5)), columns=list("ABCDE"))
    one_d_array = pd.Series(np.random.rand(10, ))
    random_array = pd.Series(np.random.rand(11,))
    threshold = 0.05

    assert isinstance(threshold, float)

>>>>>>> Stashed changes
    # X must not be 1-d either
    with pytest.raises(ValueError):
        feature_select(one_d_array, one_d_array)
    
    # y must be 1-d array
    with pytest.raises(ValueError):
        feature_select(df, df)
        
    # X and y must have consistent number of samples
    with pytest.raises(ValueError):
        feature_select(df, random_array)

<<<<<<< Updated upstream

=======
    # test threshold
    with pytest.raises(ValueError):
        feature_select(df, one_d_array, 1.2)
    
    with pytest.raises(ValueError):
        feature_select(df, one_d_array, -0.2)
    
    with pytest.raises(TypeError):
        feature_select(df, one_d_array, 5)

    with pytest.raises(TypeError):
        feature_select(df, one_d_array, "hi")

    with pytest.raises(TypeError):
        feature_select(df, one_d_array, [0.8])
>>>>>>> Stashed changes
