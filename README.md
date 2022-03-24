# Foo Package

An example package with version controlled with [setuptools_scm](https://github.com/pypa/setuptools_scm/). Inspired (copied) from [python-package-example](https://github.com/activescott/python-package-example).

## Install foo_package
While in top directory with `environment.yml` and `setup.py` run the following:
1. Create environment
```bash
conda env create -f environment.yml
conda activate foo_package
```
2. Install foo_package using pip
```bash
python -m pip install .
```

## How to interpret the version
Package was installed with HEAD pointing at tag [v0.0.1](https://github.com/jennyfothergill/foo_package/releases/tag/v0.0.1):
```python
>>> import foo_package as foo
>>> foo.version
'0.0.1'
```

Package was installed with uncommited changes in the repo on 2022/03/24 where the last commit was [9ecb096](https://github.com/jennyfothergill/foo_package/commit/9ecb0961cb24b2e82e421b282a5a9339839272f3):
```python
>>> import foo_package as foo
>>> foo.version
'0.0.2.dev0+g9ecb096.d20220324'
```

Package was installed with HEAD pointing at 1 commit past tag [v0.0.1](https://github.com/jennyfothergill/foo_package/releases/tag/v0.0.1) commit [cae2b19](https://github.com/jennyfothergill/foo_package/commit/cae2b19d7b8d5d2413a9c925221fe580873cacad):
```python
>>> import foo_package as foo
>>> foo.version
'0.0.2.dev1+gcae2b19'
```
