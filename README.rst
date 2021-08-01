Template Transcriber Package
=================================
Command line tool for generating file structures from Jinja2 templates

Note: All  below commands should be executed from root (directory of this readme)

Production Use
---------------
+++++++++++++
Installation
+++++++++++++
Installing package with dependencies (update accordingly for actual github link/PyPI)::

    $ python3 -m pip install git+https://github.com/vcamp314/template-transcriber

++++++
Usage
++++++
How to run:

- change directory to where you want your resulting file structures created
- run the below command, replacing the paths for those pointing to where the json scheme and where the template structure you wish to use is::

    $ tt ./path/to/json/scheme ./path/to/template


Development
---------------
++++++
Setup
++++++
Installing package with dependencies::

    $ python3 -m pip install -r requirements.txt

+++++++
Running
+++++++
How to run (template example, to be replaced with actual project's example)

Default run example::

    $ python3 -m tt ./path/to/json/scheme ./path/to/template


++++++++
Testing
++++++++
how to run unit tests including doctests::

    $ pytest


