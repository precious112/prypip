from setuptools import setup
import setuptools

with open("README.md", encoding="utf8") as f:
    long_description=f.read()

setup(name='prypip',
      version='1.0.7',
      description='pip for wrapper for properly auto updating requirements.txt and sorting out dependencies',
      author='Balogun Precious',
      author_email='preciouskent8@gmail.com',
      url='https://www.github.com/precious112/prypip',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      keywords=['pip','requirements','requirements.txt','dependency management'],
      python_requires='>=3.8',
      install_requires=[
        'colorama'
      ],
      entry_points={
        "console_scripts": [
            'prypip=app.prypip:main'
        ]
      }
     )