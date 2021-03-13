# easysklearn 

[![build](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/build.yml)
[![Deploy](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/524_easysklearn/actions/workflows/deploy.yml)
![](https://github.com/yzr1996/easysklearn/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/524_easysklearn/branch/main/graph/badge.svg?token=3KW44NKWAS)](https://codecov.io/gh/UBC-MDS/524_easysklearn) [![Documentation Status](https://readthedocs.org/projects/easysklearn/badge/?version=latest)](https://easysklearn.readthedocs.io/en/latest/?badge=latest)

## Summary

Easysklearn is an open-source library designed to perform exploratory data analysis, to help with missing data imputation and to give baseline models. Also, it assists in feature selection which is a common problem when undertaking a data science or machine learning analysis.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ easysklearn
```

## Features

This package contains four functions that accept a pandas DataFrame. All functions can be used on a dataset with numerical and categorical features. Each function will have it's own required and optional arguments.

- eda: EDA data analysis will split the original data into train and test dataset and will generate a statistical report such as correlation between the variables, number of missing data, class imbalance and type of data present in the dataset.

- Data imputation: It will handle missing data in the data frame.

- Baseline Function: Baseline function will give users a quick check of the performance of the selected sklearn models as a baseline for further model training.

- Feature selection: This will remove redundant features based on the forward selection.

## How the easysklearn package fits into the Python ecosystem

To our knowledge, while pandas profiling provides some data statistical analysis, there is no general-purpose library for performing the above task together in the Python ecosystem.

## Dependencies

- TODO

## Usage

- TODO

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
