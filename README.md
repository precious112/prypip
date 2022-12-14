
# Prypip

Python package for auto updating requirements.txt and managing dependencies installed with pip.

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![Python 3.6](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Why Prypip?

updating requirements.txt file in your python project requires manually adding the package or running :

```
pip freeze

```
which is not ideal because it could introduce packages useless to the project which could possibly break your 
code in production (trust me,been there 😪) especially when using environments like conda and also adds sub dependencies ( packages that are required by packages you installed) which will fill up the requirements.txt with too much packages and can be a hussle trying to uninstall a package  as you won't know immediately which package is dependent on another.

Prypip helps with these issues by :

- Auto updates your requirements.txt whenever you install,uninstall and upgrade a package via pip.

- Only adds packages you installed directly and separates sub dependencies in the ``` dependency_tree.json ``` file

- Doesn't allow redundant packages lying in your project.

In summary prypip will make your development and coding process much easier.

Would appreciate you using prypip, i'm very much open to feed backs 😁 .

# More

Contributors a very much welcomed, more ideas,features and correction are welcomed.

I also want to put this here that i'm open to remote and possibly sponsored relocation roles incase you have any job roles you know of or an employer, recommendations for roles are very much welcomed, I'm a fullstack developer with extensive knowledge of the foillowing technologies:

- Django
- Flask
- Fast api
- React js
- Next js

You can reach me via my email address preciouskent8@gmail.com, linked in profile link https://www.linkedin.com/in/precious-balogun-7392141b2/ . Link to my resume https://drive.google.com/file/d/1ItIuzXq_srjgVg6DzNVmTWb1x8wHPK-q/view?fbclid=IwAR0ccEf0woz5UIbBt8m26RFd0MT3pry4MtQS1sF2g7xlYvn_GDpJVliSiuE .

Thank you 😁 .







## Usage/Examples

you can install prypip by simply:

```
pip install prypip
```

Note: prypip should only be used within a virtual environment.
you shouldn't add prypip to your requirements.txt to avoid adding 
it to production,prypip is only meant to work locally.

After installing via pip you will need to create a
```venv_py_path.txt``` file that will contain the path
to two file paths namely:

- The path to the virtual environment's python interpreter,this is usually within the Scripts folder in the virtual environment directory.An example of this path in windows is :

```
C:\Users\user\otherPipProj\otherpipENV\Scripts\python
```

- The second line in the ```venv_py_path.txt``` should contain the site-packages path where pip stores all installed packages,specifying this path is required for the package to fully work. An example of this path in windows is :

```
C:\Users\user\otherPipProj\otherpipENV\Lib\site-packages
```

All these file paths are available on all OS,you can make a bit of google search to know exactly how to find these file paths in your PC.

After all is set,viola! you're ready to use prypip 🥳 .

Prypip can be used on the command line with the root command ``` prypip ``` .

To install a package you can use :

```
prypip run pip install <package_name>
```

This will perform the regular pip install function with the added fuctionality of updating your requirements.txt automatically.

Note: Make sure you're within the root directory of your project which is where the requirements.txt file usually resides.

Other commands and examples include:

```

prypip run pip uninstall <package_name>  [<automatically removes a package from requirements.txt when pip uninstalls a package>]

prypip run pip install <package_name> --upgrade [<automatically updates the version of the upgraded package in requirements.txt>]

prypip open dependency_tree.json [<this command opens the dependency_tree.json file(check api reference for more) and displays every package with their dependencies in a tree structure>]

```

## API Reference

``` venv_py_path.txt ``` : file created by user to store virtual environment's python interpreter path and site-packages
path.

``` dependency_tree.json ``` : file that stores each installed package as a key and every sub packages that it requires
(packages in which the installed package depends on) as value in a dict then converted to json.

``` prypip ``` : The main command for working with prypip.

``` run ``` : used to specify execution of commands external to prypip e.g pip

``` open ``` : used for opening and displaying special documents in prypip, e.g ``` prypip open dependency_tree.json ```
displays tthe content of dependency_tree.json in a tree like structure.


