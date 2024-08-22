# my_package
Example repository for setting up a pip installable project

## documentation
https://my_package.readthedocs.io/en/latest/
Read this to understand how to set up the automated documentation

## github installation
To install run the following line in your environment

    pip install git+https://github.com/MikeSmithLabTeam/my_package

## github update
To update run the following line in your environment

    pip install --upgrade git+https://github.com/MikeSmithLabTeam/my_package

## Setup docs

1. Install sphinx

    pip install sphinx

2. Change to the docs directory

    cd docs

3. Run sphinx-quickstart

    sphinx-quickstart

4. Edit the conf.py file

    Add the following lines to the top of the file

    ```python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../my_package'))
    ```

    Add the following lines to the extensions list

    ```python
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    ```

    Add the following lines to the end of the file

    ```python
    # -- Extension configuration -------------------------------------------------
    autodoc_mock_imports = ['numpy', 'pandas', 'matplotlib', 'scipy', 'sklearn', 'seaborn', 'statsmodels', 'tensorflow', 'torch', 'keras', 'xgboost', 'lightgbm', 'catboost']
    ```

5. Run sphinx-apidoc

    sphinx-apidoc -f -o source/ ../my_package

6. Build the docs

    make html

7. Open the docs

    open _build/html/index.html


