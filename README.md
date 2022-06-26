# Python library quick start
This is a minimal template for uploading your python packages to pypi.org.

## To Use
* First clone this project.
```bash
# Clone this repository
git clone https://github.com/defartsa23/python-library-quick-start.git
# Go into the repository
cd python-library-quick-start
```
* Rename the folder `your-package` to the package name you want. then place all your files into a folder. Open the `__init__.py` file with a text editor of your choice. In this file, you write nothing but the import statement which has the following schema:
```python
from .Filename import Classname
```
* Replace the information in the `setup.py` file with the matching content.
* Upload your package to PyPi
```sh
python setup.py sdist
twine upload dist/*
```
