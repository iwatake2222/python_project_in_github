# python_project_in_github

```
# Install requirements
pip3 install -r requirements.txt

# Execute script
python3 calculator/__main__.py --op + --lval 6 --rval 4

# Install
python3 setup.py sdist
pip3 install dist/calculator-1.0.tar.gz
python3 -m calculator --op + --lval 6 --rval 4

# Test
python3 -m pytest --doctest-modules  -v --cov=./calculator
python3 -m pylint ./calculator
```


```
pip3 install mkdoc
pip3 install mkdocs-material
pip3 install pygments

python3 -m mkdocs new ./
python3 -m mkdocs build
python3 -m mkdocs serve
```
