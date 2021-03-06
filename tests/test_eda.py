#import libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pytest
from easysklearn.eda import eda

#generate dataset
import pandas as pd
def get_test_data():
    """
    This test will generate a dummy dataset
    """    
    gen_data = pd.DataFrame()
    gen_data["num1"] = [9.4, 8, 9.1, 9.3, 9.4]
    gen_data["num2"] = [0.91, 0.92, 0.93 , 0.94 , 0.95]
    gen_data["num3"] = [0.56, 0.68, 0.65, 0.59, 0.51]
    gen_data["num4"] = [0.072, 0.098, 0.092, 0.075, 0.076]
    gen_data["cat1"] = ["Good","Bad","Excellent","Ok","Good"]
    gen_data["target"] = [1,2,2,3,1]
    
    return gen_data
gen_data= get_test_data()


#Check if all eda attributes are generating
def test_eda_check_all_attributes_generated():
    
    test_data = get_test_data()
    eda_results = eda(test_data,'target')

    assert 'head' in eda_results
    assert 'tail' in eda_results
 
# Check if shape of train dataset is 80% of orginal dataset
train_df, test_df = train_test_split(gen_data, test_size=0.2, random_state=123)
assert train_df.shape[0] == int(len(gen_data)*.8)


# Check if shape of train and test dataset is same
    
if len(train_df.columns) != len(test_df.columns):
        raise ValueError(f'X_train and y_train have a dimensions mismatch')






    
