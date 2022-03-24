# Foo Package

An example package with version controlled with [setuptools_scm](https://github.com/pypa/setuptools_scm/). Inspired (copied) from [python-package-example](https://github.com/activescott/python-package-example).

## How to interpret the version
Install with HEAD pointing at a tag:
```python
>>> import foo_package as foo
>>> foo.version
'0.0.1'
```

Install with uncommited changes in the repo on 2022/03/24 where the last commit was 9ecb096:
```
>>> import foo_package as foo
>>> foo.version
'0.0.2.dev0+g9ecb096.d20220324'
```

Install with HEAD pointing at 1 commit past 0.0.1 commit cae2b19
```
>>> import foo_package as foo
>>> foo.version
'0.0.2.dev1+gcae2b19'
```
