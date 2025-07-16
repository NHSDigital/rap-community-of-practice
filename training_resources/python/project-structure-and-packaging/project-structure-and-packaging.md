---
title: Project and Package structuring

tags: 
  - Project structure
  - Python
  - Packaging
  - Pip
  - Anaconda
---

#
!!! tip "TLDR"
    - Generally you should use a standard repo structure - this page describes how and why
    - [RAP Python Package template](https://github.com/NHSDigital/rap-package-template) comes with sections for the different bits of your code, testing and prepares you for making your code into a Python package.
    - There is guidance on [how to adapt the RAP Package template for your project](#adapting-package-structure-for-analytical-work)

??? question "Why should we care?"
    - If we use a standard repo structure it will be easier for other people to understand and reuse your code.
    - This structure follows current best practice for Python
    - Packaging your code makes it easier for other people to re-run it, or use the functions / classes / etc. that you've made.

??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[Levels of RAP](../../introduction_to_RAP/levels_of_RAP.md)|Essential|Having well organised code and following a standard directory format is a component of **Silver RAP**|

A Python package is a way to bundle your code into a single thing that can be shared and reused. If our goal is to be able to share and reuse code across NHS England and externally then there are many benefits to packaging code:

- **Shareable**: The most important reason to use packages is that it is the way to share Python code. Not using packages runs the risk that other people will not be able to run your code... "It works fine on my machine".
- **Databricks**: It looks likely that packaging code will be the easiest way to get your code onto databricks. (NB: we are keeping a close eye on Data Refinery to answer this question)
- **Reliability**: Packages go a long way to ensuring that other people in your team can open your code and run it without hitting issues.
- **Organised**: Packages allow you to organise your code in logical sections. This makes it much easier to test and to maintain over time.
- **Predictable**: since all packages follow a similar structure, other analysts will be able to quickly understand how you have organised your code. No more hunting through a random directory structure trying to figure out where everything is kept.

This is a tricky topic at first so we recommend asking for some support when you set this up for the first time.

## How to package Python code

In order to package your code, you just need to follow the standard templates for Python projects. I describe this briefly here but provide links to the comprehensive official guidance below.

Here is an outline of a very basic Python project for a publication as an example:

```txt
project_name
├── LICENSE
├── README.md
├── requirements.txt
├── pyproject.toml
├── src/
|   ├── __init__.py
|   ├── main.py
│   └── example_package/
│       ├── __init__.py
│       └── example.py
├── sql/
├── templates/
└── tests/
```

Note that the whole directory is called `project_name` but we also have a sub-folder called `src`. All of our code lives inside this `src` sub-folder. Sometimes you might see the folder that contains all the code called `scripts` but the other common convention is to name it the same as the overall project.

The README.md file is extremely important as this functions as the package’s landing page. The README provides a bird's eye view of the whole package. You should treat it as the first thing a new starter might read when trying to understand your code. It might contain an overview of the code, details of inputs/outputs, how to install package, ownership, contributing and licence info.

The random-seeming files (`pyproject.toml`, `requirements.txt`, etc.) are all involved in dependency management. Your package will depend on certain things being in place in order to run - these files manage those dependencies. Be aware that dependency management has evolved over the years in Python and other languages and best practice has changed over time. Here, we aim to keep it as simple as possible while still achieving the goal of producing robust, shareable code.

Also note the funny looking `__init__.py`. This file tells Python that this code is part of a package. With this file in place you can import functions from the different parts of your code. E.g. `from sdd.example_package.example import my_function`. Again - you can learn more about this in the links below.

Here is another for the [NDA publication](https://github.com/NHSDigital/national-diabetes-audit) so you can see the pattern. We have a more elaborate version of this below.

```
national-diabetes-audit/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── diabetes_code/
|   ├── __init__.py
|   ├── main.py
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

## Generic package template

To help get you started, we have created a generic package structure that you can adapt for your own purposes. The repository is stored on [GitHub](https://github.com/NHSDigital/rap-package-template). You can fork this repo and use it as a starting point for your own package.

## So what now?

- Make your own package either by adding the files yourself or by cloning the [generic template](https://github.com/NHSDigital/rap-package-template) that we provide.
- Once you have the package structure in place, you can install that package on your machine following any of these options:
- Never used virtual environments before? Visit our [RAP COP guidance](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/virtual-environments/why-use-virtual-environments/)!

### Using pip
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
For Visual Studio Code it is necessary that you change your default interpreter to the virtual environment you just created .venv. To do this use the shortcut Ctrl-Shift-P, search for Python: Select interpreter and select .venv from the list.

### Using conda
The first line of the `environment.yml` file sets the new environment's name. In this template, the name is `rap_template`- you should change this in the `environment.yml` file, as well as the following code, to the name of your project.
```
conda env create -f environment.yml
conda activate <environment_name>
```

  Once the package is installed it will be able to identify all the modules inside your code. If you have populated the `setup.py` and `requirements.txt`, Python will install all of the bits that your code needs in order to run.

- More importantly, other people can install finished your package from gitlab using `pip install git+path_to_my_repo`. For example `pip install git+https://<domain>/<path>/diabetes_rap`

- Even better, you can bundle all of your code into a single file called a wheel (.whl). This wheel can be shared, stored in an online repository for others to use, or installed into data processing platforms such as Databricks.

## Adapting package structure for analytical work

Every Python project should follow the standard package structure to help ensure portability and reliability. Nevertheless, there is scope to adapt this structure to fit the workflow of specific projects. The [cookie cutter data science template](https://drivendata.github.io/cookiecutter-data-science/#directory-structure) shows how you can include folders for output data, validation reports, figures, etc.
The figure below shows how we have applied this structure to the [RAP package template](https://github.com/NHSDigital/rap-package-template).

```
project_name
|   .gitignore                        <- Files (& file types) automatically removed from version control for security purposes
|   config.toml                       <- Configuration file with parameters we want to be able to change (e.g. date)
|   environment.yml                   <- Conda equivalent of requirements file
|   requirements.txt                  <- Requirements for reproducing the analysis environment 
|   pyproject.toml                    <- Configuration file containing package build information
|   LICENCE                           <- License info for public distribution
|   README.md                         <- Quick start guide / explanation of your project
|
|   create_publication.py             <- Runs the overall pipeline to produce the publication     
|
+---src                               <- Scripts with functions for use in 'create_publication.py'. Contains project's codebase.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---utils                     <- Scripts relating to configuration and handling data connections e.g. importing data, writing to a database etc.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       file_paths.py             <- Configures file paths for the package
|   |       logging_config.py         <- Configures logging
|   |       data_connections.py       <- Handles data connections i.e. reading/writing dataframes from SQL Server
|   | 
|   +---processing                    <- Scripts with modules containing functions to process data i.e. clean and derive new fields
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       clean.py                  <- Perform cleaning and wrangling processes 
|   |       derive_fields.py          <- Create new field definitions, columns, derivations.
|   | 
|   +---data_ingestion                <- Scripts with modules containing functions to preprocess read data i.e. perform validation/data quality checks, other preprocessing etc.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       preprocessing.py          <- Perform preprocessing, for example preparing your data for metadata or data quality checks.
|   |       validation_checks.py      <- Perform validation checks e.g. a field has acceptable values.
|   |
|   +---data_exports
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       write_excel.py            <- Populates an excel .xlsx template with values from your CSV output.
|   |
+---sql                               <- SQL scripts for importing data  
|       example.sql
|
+---templates                         <- Templates for output files
|       publication_template.xlsx
|
+---tests
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---backtests                     <- Comparison tests for the old and new pipeline's outputs
|   |       backtesting_params.py
|   |       test_compare_outputs.py
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---unittests                     <- Tests for the functional outputs of Python code
|   |       test_data_connections.py
|   |       test_processing.py
|   |       __init__.py               <- Makes the functions folder an importable Python module
```

Some things to notice about this structure:

- All of the actual code lives inside the `src` directory. Everything else at the top level has to do with packaging and testing the code.
- In the repository there are two files: `create_publication.py` and `config.toml`. These top level files are the highest level of abstraction and should be the main place where users interact with the code.

  - The `config.toml` file contains all of the parameters that we expect to change frequently, e.g. input data.
  - The `create_publication.py` file organises the steps in a simple, easy-to-understand manner that should be readable by anyone, even if they don't know python. In this way, we aim to reduce risk by make the code accessible to new staff.
  - The `requirements.txt` file which specifies all the Python packages you wish to install. See [venv virtual environments guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/virtual-environments/venv/).
  - The `environment.yml` is Conda offering a way to export and share environments via a yaml file. See [Conda virtual environments guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/virtual-environments/conda/) for more info.
  - The `pyproject.toml` file, which contains build system requirements and information, which are used by pip to build the package. For more information see [pyproject.toml documentation](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/). 

### `root`

In the highest level of this repository (known as the 'root'), there is one Python file: `create_publication.py`. This top level file should be the main place where users interact with the code, where you store the steps to create your publication.

This file currently runs a set of example steps using example data.

### `src`

This directory contains the meaty parts of the code. By organising the code into logical sections, we make it easier to understand, maintain and test. Moreover, tucking the complex code out of the way means that users don't need to understand everything about the code all at once.

* `data_connections.py` handles reading data in and writing data back out.
* `processing` folder contains the core business logic.
* `utils` folder contains useful reusable functions (e.g. to set up logging, and importing configuration settings from `config.toml`)
* `write_excel.py` contains functions relating to the final part of the pipeline, any exporting or templating happens here. This is a simplistic application of writing output code to an Excel spreadsheet template (.xlsx). A good example of this application is: [NHS sickness absence rates publication](https://github.com/NHSDigital/absence-rates). We highly recommend to use [Automated Excel Production](https://nhsd-git.digital.nhs.uk/data-services/analytics-service/iuod/automated-excel-publications) for a more in depth Excel template production application.

Note that we never store passwords or any sensitive credentials in the repo to prevent the situation where it can mistakenly committed into the git. There are several ways to deal with the secret, keys and passwords such as using Git Hooks or final cleansing process before publishing.

## Further Reading

This is a really big topic and we don't want to replicate material that you can find elsewhere. Here are links to some resources that will give you as much detail as you want on this topic.

- [Packaging your Python project](https://packaging.python.org/tutorials/packaging-projects/)

- [Packages and modules from the official docs](https://docs.python.org/3/tutorial/modules.html#packages).
  _Good for understanding on how to organise and import sub-packages._

- [Why we share code as a .whl file](https://packaging.python.org/discussions/wheel-vs-egg/)
