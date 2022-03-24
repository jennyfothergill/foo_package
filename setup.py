from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

def myversion():
    from setuptools_scm.version import get_local_dirty_tag
    def clean_scheme(version):
        return get_local_dirty_tag(version) if version.dirty else '+clean'

    return {'local_scheme': clean_scheme}

setup(
    name="foo_package",
    version="0.0.1",
    use_scm_version=myversion,
    author="Jenny Fothergill",
    author_email="jennyfothergill@boisestate.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jennyfothergill/foo_package",
    license="GPLv3",
    project_urls={
        "Bug Tracker": "https://github.com/jennyfothergill/foo_package/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "foo_package"},
    packages=find_packages(),
    python_requires=">=3.6",
)
