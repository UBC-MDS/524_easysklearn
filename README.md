# easysklearn 

[![build](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/build.yml)
[![Deploy](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/deploy.yml)
![](https://github.com/yzr1996/easysklearn/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/524_easysklearn/branch/main/graph/badge.svg?token=3KW44NKWAS)](https://codecov.io/gh/UBC-MDS/524_easysklearn) [![Documentation Status](https://readthedocs.org/projects/easysklearn/badge/?version=latest)](https://easysklearn.readthedocs.io/en/latest/?badge=latest)

## Summary

Easysklearn is a python package designed to perform exploratory data analysis, to help with missing data imputation and to give baseline models. Also, it assists in feature selection which is a common problem when undertaking a data science or machine learning analysis. As its name indicates, this function operates like sklearn. It carries out tasks such as splitting data, feature selection, model fitting, numerical missing data imputation etc.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ easysklearn
```

## Features

This package introduces a data science enthusiast, with little to no knowledge of machine learning, to the common steps required when undertaking a Supervised learning analysis. The package contains four functions that accept a pandas DataFrame. All functions can be used on a dataset with numerical features. The functions might have their own required and optional arguments.

- **eda**: The `eda` function will split the original data into train and test dataset and will generate a statistical report such as correlation between the variables, number of missing data, class imbalance and type of data present in the dataset.

- **miss_data**: The `miss_data` function will handle missing numerical data in the data frame.

- **baseline_fun**: The `baseline_fun` function will give users a quick check of the performance of the selected sklearn models compared to a baseline model, upon which the model can be improved. 

- **feature_select**: The `feature_select` function will remove redundant features based on the forward selection.

## How the easysklearn package fits into the Python ecosystem

To our knowledge, while pandas profiling provides some data statistical analysis, there is no general-purpose library for performing the aforementioned tasks together in the Python ecosystem.

## Dependencies


- python = "^3.8"
- pandas = "^1.2.3"
- numpy = "^1.20.1"
- matplotlib = "^3.3.4"
- sklearn = "^0.0"
- seaborn = "^0.11.1"
- ipython = "^7.21.0"    
- jupyter = "^1.0.0"


## Usage

| Task | Function  |
|------------|-----|
| Exploratory data analysis| `eda(df, target)`|
| Numerical data imputation| `miss_data(x_train, x_test, strategy="mean")`|
| Compare selected model to a baseline model| `baseline_fun(X_train, y_train, type="regression", metrics_1="accuracy", metrics_2="r2")`|
| Feature selection to reduce data dimension| `feature_select(X_train, y_train, threshold=0.05)`|



## Example

```Python

from easysklearn import eda, baseline_fun, miss_data, feature_select

example_df = pd.DataFrame(np.array([[4500, np.nan, 4], [3450, 350_000, 6],
    [np.nan, 800_000, 9]]), columns = ['size', 'price', 'bedrooms'])

- eda = eda(example_df, target)
- x_train, x_test = miss_data(x_train, x_test, strategy="mean")
- results = baseline_fun(X_train, y_train, type="regression", metrics_1="accuracy", metrics_2="r2")
- best_features = feature_select(X_train, y_train, threshold=0.05)
```

## Documentation

The official documentation is hosted on Read the Docs: https://easysklearn.readthedocs.io/en/latest/

## Contributors

Development leaders:

- Ifeanyi Anene
- Lara Habashy
- Sakshi Jain
- Zhenrui Yu


We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/yzr1996/easysklearn/graphs/contributors). If you would like to contribute, please view our [contributing guidelines](https://github.com/UBC-MDS/524_easysklearn/blob/main/CONTRIBUTING.rst) and get familiar with the [Github flow](https://blog.programster.org/git-workflows) workflow.

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
