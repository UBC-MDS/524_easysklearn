def eda():

def miss_data(x_train, x_test, method = "mean"):
    """
    Impute value(s) wherever there is (are) a missing value(s) in the dataframe. 
    
    Takes in a the train and test split dataframes and apply univariate feature
    imputation on the missing values in either dataframe depending on the strategy
    selected by the user. 
    
    Parameters
    ----------
    x_train : Pandas DataFrame
              The train set dataframe with missing values in it.
    
    x_test : Pandas DataFrame 
             The test set DataFrame with (or without) missing values in it. 
    
    method: string
            The imputation strategy:
            
            Imputing the mean along each column is the default setting. 
            
            If “mean”, then replace missing values using the mean along each column. This can only be used with numeric data.

            If “median”, then replace missing values using the median along each column. This can only be used with numeric data.

            If “most_frequent”, then replace missing using the most frequent value along each column. 
    
    Returns
    -------
    x_train_imp : Pandas DataFrame
                  The imputed train set DataFrame.
    
    x_test_imp : Pandas DataFrame
                 The imputed test set DataFrame.
    
    
    Examples
    --------
    >>> from easysklearn import miss_data
    
    >>> strategy = "median"
    
    >>> x_train = pd.DataFrame(np.array([[4500, np.nan, 4], [3450, 350_000, 6],
    [np.nan, 800_000, 9]]), columns = ['size', 'price', 'bedrooms'])
    
    >>> x_test = pd.DataFrame(np.array([[2500, np.nan, 4], [5000, 750_000, 4],
    [np.nan, 1_200_000, 5]]), columns = ['size', 'price', 'bedrooms'])
    
    >>> x_train_imp, x_test_imp = miss_data(x_train, x_test, method = strategy)
    
    >>> x_train_imp
        size     price    bedrooms
    0  4500.0  975000.0       4.0
    1  3450.0  350000.0       6.0
    2  3750.0  800000.0       9.0
    
    >>> x_test_imp 
        size      price     bedrooms
    0  2500.0   975000.0       4.0
    1  5000.0   750000.0       4.0
    2  3750.0  1200000.0       5.0
    """

def baseline_fun():

def feature_select():