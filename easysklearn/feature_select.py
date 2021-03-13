import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def feature_select(X_train, y_train, threshold=0.05):
    """
    Performs forward selection of features in the data by starting with an empty model, 
    and iteratively adds features that improve the model's score. The algorithm stops once 
    the decrease of the accuracy from an additional features is bigger than the threshold.

    Parameters
    ----------
    X_train : Pandas DataFrame
              The training set of the data
    
    y_train : Pandas DataFrame
              The target of the data
    
    threshold : float (default=0.05)
                user input threshold between 0 and 1 used for bounding features selected
    
    Returns
    -------
    result : List
             A list containing the selected features of type str, i.e. the best features in the model
             
    Examples
    --------
    >>> from easysklearn import feature_select
    >>> from sklearn.linear_model import LinearRegression
    
    >>> feature_select(X_train, y_train)
    """
    
    # exception handling
    if type(X_train) not in {pd.DataFrame}:
        raise TypeError('X_train must be a Pandas DataFrame.')

    if len(X_train.shape) != 2:
        raise ValueError('X_train must be 2-dimensional.')
        
    if type(y_train) not in {pd.DataFrame, pd.Series}:
        raise TypeError('y_train must be a Pandas DataFrame.')

    if len(y_train.shape) != 1:
        raise ValueError('y_train must be 1-dimensional.')
        
    if X_train.shape[0] != y.shape[0]:
        
    # bound threshold - percentage change
    if ((threshold < 0.0) or (threshold > 1.0)):
        raise ValueError('Threshold must be a float between 0 and 1')
    
    # initialize variables
    initial_features = X_train.columns.tolist()
    best_features = []
    scores = []
    max_features = X_train.shape[1]
    previous = 0
    
        remaining_features = list(set(initial_features)-set(best_features))
        temp = pd.Series(index=remaining_features, dtype= 'float64')
        for temp_feature in remaining_features:
            
            # fit and score data
            model = LinearRegression().fit(X_train[best_features+[temp_feature]], y_train)
            temp[temp_feature] = model.score(X_train[best_features+[temp_feature]], y_train)
 
        # best scores
        scoring = temp.max()
        scores.append(scoring)
        max_val = max(scores)

        # stopping criteria based on threshold 
        if (j > 1):
            previous = (np.array(scores))[j-1]
            previous = previous.max()
            if(((max_val - previous) / previous) > threshold):
                break
        best_features.append(temp.idxmax())  

    return best_features
