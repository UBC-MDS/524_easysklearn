#Spliting the data into train and test

def EDA(df):
        """[Split DataFrame into random train and test subsets, inspection of data by printing first and last 5 lines of DataFrame, reporting missing values in the dataset, reporting type of features, checking imbalance present in dependent variable, investigate correlation matrix]
        
        Parameters
        ----------
        df: pandas DataFrame
                Pandas dataframes. 
        
        Returns
        -------
        DataFrame: DataFrame
                DataFrame
        
        None: 
                This method prints a summary of a DataFrame and returns None.
        
        ax: matplotlib Axes
              Axes object with the heatmap.

        Series

        """



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
    
    >>> x_train = pd.DataFrame(np.array([['Blue', 56, 4], ['Red', 35, 6],
    ['Green', 18, 9]]), columns = ['color', 'count', 'usage'])
    
    >>> x_test = pd.DataFrame(np.array([['Blue', 56, 4], ['Red', 35, 6],
    ['Green', 18, 9]]), columns = ['color', 'count', 'usage'])
    
    >>> x_train_imp, x_test_imp = miss_data(x_train, x_test, strategy = "mean")
    """

def baseline_fun(X_train, y_train, type = 'regression', metrics_1 = 'accuracy', metrics_2 = 'r2'):
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
            The all avaliable scoring metrics is https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
    
    metrics_2: string
            What kind of score metrics to use for regression problem, the default one is r2
            The all avaliable scoring metrics is https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

    Returns
    -------
    result : Pandas DataFrame
                  The DataFrame contains the mean of fit time, score time, training score and validation score by 5-fold cross validation for both two models.
    
    Examples
    --------
    >>> from easysklearn import baseline_fun
    
    >>> baseline_fun(x_train, y_train, type = 'regression', metrics = 'neg_root_mean_squared_error')
    """

def feature_select():