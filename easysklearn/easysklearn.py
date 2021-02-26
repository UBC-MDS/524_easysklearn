def eda():

def miss_data(x_train, x_test, method = "mean"):
    """
    
    
    Parameters
    ----------
    x_train : Pandas DataFrame
              The train set dataframe with missing values in it.
    
    x_test : Pandas DataFrame 
             The test set DataFrame with (or without) missing values in it. 
    
    method: string
            The imputation strategy:
            
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
    
    >>> x_train = pd.DataFrame(np.array([[4500, np.nan, 4], [3450, 350_000, 6],
    [np.nan, 800_000, 9]]), columns = ['size', 'price', 'bedrooms'])
    
    >>> x_test = pd.DataFrame(np.array([[2500, np.nan, 4], [5000, 750_000, 4],
    [np.nan, 1_200_000, 5]]), columns = ['size', 'price', 'bedrooms'])
    
    >>> x_train_imp, x_test_imp = miss_data(x_train, x_test, strategy = "mean")
    """

def baseline_fun():

def feature_select():