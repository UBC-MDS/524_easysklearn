from easysklearn.miss_data import miss_data
import pandas as pd
import numpy as np 
from pytest import raises


x_train = pd.DataFrame(np.array([[4500, np.nan, 4], [3450, 350_000, 6], [2000, 450_000, np.nan],
    [np.nan, 800_000, 9]]), columns = ['size', 'price', 'bedrooms'])


x_test = pd.DataFrame(np.array([[2500, np.nan, 4], [5000, 750_000, 4], [2000, 450_000, np.nan],
    [np.nan, 1_200_000, 5]]), columns = ['size', 'price', 'bedrooms'])

def test_input_data():
    
    with raises(TypeError):
        baseline_fun(x_train, x_test, method = 'sum')
    
    with raises(TypeError):
        baseline_fun(1, x_test, method = 'mean')
    
    with raises(TypeError):
        baseline_fun(x_train, 1, method = 'mean')
    
    with raises(TypeError):
        baseline_fun(x_train, x_test, method = 2)
    
    
    
    
    