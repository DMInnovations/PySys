from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '2.2'
DESCRIPTION = 'Simple library to see your computer spec information.'
LONG_DESCRIPTION = 'None'

# Setting up
setup(
    name="PySys",
    version=VERSION,
    author="DMInnovation",
    author_email="<none>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'python3', 'pysys', 'PySys', 'dminnovations', 'geekbench', 'system'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)