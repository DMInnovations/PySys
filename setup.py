from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = 'v2.2'
DESCRIPTION = "Simple library to see your computer's spec information."

# Setting up
setup(
    name="pysys",
    version=VERSION,
    author="DMInnovations",
    author_email="None",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['os', 'platform', 'psutil', 'numpy'],
    keywords=['python', 'geekbench', 'system', 'python3', 'specs', 'pysys', 'dminnovations'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)