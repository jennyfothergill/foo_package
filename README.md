# Foo Package

An example package with version controlled with [setuptools_scm](https://github.com/pypa/setuptools_scm/). Inspired (copied) from [python-package-example](https://github.com/activescott/python-package-example).

## Install foo_package
While in top directory with `environment.yml` and `setup.py` run the following:
1. Create environment
```
conda env create -f environment.yml
conda activate foo_package
```
2. Install foo_package using pip
```
python -m pip install .
```

## How to interpret the version
Package was installed with HEAD pointing at tag v0.0.1:
```python
>>> import foo_package as foo
>>> foo.version
'0.0.1'
```

Package was installed with uncommited changes in the repo on 2022/03/24 where the last commit was 9ecb096:
```
>>> import foo_package as foo
>>> foo.version
'0.0.2.dev0+g9ecb096.d20220324'
```

Package was installed with HEAD pointing at 1 commit past tag v0.0.1 commit cae2b19:
```
>>> import foo_package as foo
>>> foo.version
'0.0.2.dev1+gcae2b19'
```
