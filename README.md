# python_project_in_github

[![Python application](https://github.com/iwatake2222/python_project_in_github/actions/workflows/python-app.yml/badge.svg)](https://github.com/iwatake2222/python_project_in_github/actions/workflows/python-app.yml)
[![pages-build-deployment](https://github.com/iwatake2222/python_project_in_github/actions/workflows/pages/pages-build-deployment/badge.svg)](https://iwatake2222.github.io/python_project_in_github)

```sh
pip install git+https://github.com/iwatake2222/python_project_in_github
```

```sh
### Install requirements ###
pip3 install -r requirements.txt

### Execute script ###
python3 -m calculator --op + --lval 6 --rval 4

### Debug ###
python3 main.py

### Install ###
pip3 install ./
# python3 setup.py sdist
# pip3 install dist/calculator-1.0.tar.gz

### Test ###
python3 -m pytest --doctest-modules  -v --cov=./calculator
python3 -m pylint ./calculator
```


## Note to add mkdoc
```sh
pip3 install -r mkdocs-requirements.txt

python3 -m mkdocs new ./
python3 -m mkdocs build
python3 -m mkdocs serve
```

https://iwatake2222.github.io/python_project_in_github
