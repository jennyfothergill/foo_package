import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="foo_package",
    version="0.0.1",
    author="Jenny Fothergill",
    author_email="jennyfothergill@boisestate.edu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jennyfothergill/foo_package",
    project_urls={
        "Bug Tracker": "https://github.com/jennyfothergill/foo_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "foo_package"},
    packages=setuptools.find_packages(where="foo_package"),
    python_requires=">=3.6",
)
