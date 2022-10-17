# Project and Package structuring

A python package is a way to bundle your code into a single thing that can be shared and reused. If our goal is to be able to share and reuse code across NHS Digital and externally then there are many benefits to packaging code:

- **Shareable**: The most important reason to use packages is that it is the way to share python code. Not using packages runs the risk that other people will not be able to run your code... "It works fine on my machine".
- **Databricks**: It looks likely that packaging code will be the easiest way to get your code onto databricks. (NB: we are keeping a close eye on Data Refinery to answer this question)
- **Reliability**: Packages go a long way to ensuring that other people in your team can open your code and run it without hitting issues.
- **Organised**: Packages allow you to organise your code in logical sections. This makes it much easier to test and to maintain over time.
- **Predictable**: since all packages follow a similar structure, other analysts will be able to quickly understand how you have organised your code. No more hunting through a random directory structure trying to figure out where everything is kept.

This is a tricky topic at first so we recommend asking for some support when you set this up for the first time.

## How to package python code

In order to package your code, you just need to follow the standard templates for python projects. I describe this briefly here but provide links to the comprehensive official guidance below.

Here is an outline of a very basic python project for the Smoking, Drinking, and Drugs publication (SDD):

```txt
SDD/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── sdd/
|   ├── __init__.py
|   ├── main.py
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

Note that the whole directory is called `SDD` but we also have a sub-folder called `sdd`. All of our code lives inside this `sdd` sub-folder. Sometimes you might see the folder that contains all the code called `src` but the other common convention is to name it the same as the overall project.

The README.md file is extremely important as this functions as the package’s landing page. The README provides a bird's eye view of the whole package. You should treat it as the first thing a new starter might read when trying to understand your code. It might contain an overview of the code, details of inputs/outputs, how to install package, ownership, contributing and licence info.

The random-seeming files (setup.py, requirements.txt, etc.) are all involved in dependency management. Your package will depend on certain things being in place in order to run - these files manage those dependencies. Be aware that dependency management is a difficult topic in python and other languages and so over the years many different approaches have fallen in and out of favour. Here, we aim to keep it as simple as possible while still achieving the goal of producing robust, shareable code.

Also note the funny looking `__init__.py`. This file tells python that this code is part of a package. With this file in place you can import functions from the different parts of your code. E.g. `from sdd.example_package.example import my_function`. Again - you can learn more about this in the links below.

Here is another for the diabetes publication so you can see the pattern. We have a more elaborate version of this below.

```
diabetes/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── diabetes/
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
- Once you have the package structure in place, you can install that package on your machine using these two commands:

  ```python
  pip install -e .
  pip install -r requirements.txt
  ```

  Once the package is installed it will be able to identify all the modules inside your code. If you have populated the `setup.py` and `requirements.txt`, python will install all of the bits that your code needs in order to run.

- More importantly, other people can install finished your package from gitlab using `pip install git+path_to_my_repo`. For example `pip install git+https://<domain>/<path>/diabetes_rap`

- Even better, you can bundle all of your code into a single file called a wheel (.whl). This wheel can be shared, stored in an online repository for others to use, or **installed into databricks**.

## Adapting package structure for analytical work

Every python project should follow the standard package structure to help ensure portability and reliability. Nevertheless, there is scope to adapt this structure to fit the workflow of specific projects. The [cookie cutter data science template](https://drivendata.github.io/cookiecutter-data-science/#directory-structure) shows how you can include folders for output data, validation reports, figures, etc.
The figure below shows how we have applied this structure to the National Diabetes Audit code.

```
diabetes
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├───diabetes
│   ├── create_publication.py
│   ├── params.py
│   ├── __init__.py
│   │
│   └───utilities
│       ├── data_connections.py
│       ├── field_definitions.py
│       ├── processing_steps.py
│       ├── __init__.py
|
├───reports
│   ├───input_profile
│   └───output_profile
│
└───tests
    ├───unittests
    │       │   test_data_connections.py
    │       │   test_field_definitions.py
    │       │   test_processing_steps.py
```

Some things to notice about this structure:

- All of the actual code lives inside the `diabetes_code` directory. Everything else at the top level has to do with packaging and testing the code.
- In the diabetes_code repository there are two files: `create_publication.py` and `params.py`. These top level files are the highest level of abstraction and should be the main place where users interact with the code.

  - The `params.py` file contains all of the parameters that we expect to change frequently, e.g. input data.
  - The `create_publication.py` file organises the steps in a simple, easy-to-understand manner that should be readable by anyone, even if they don't know python. In this way, we aim to reduce risk by make the code accessible to new staff.

- The next level down contains the meaty parts of the code. By organising the code into logical sections, we make it easier to understand but also to maintain and test. Moreover, tucking the complex code out of the way means that users don't need to understand everything about the code all at once.
  - The `data_connections.py` file handles reading data in and writing data back out. Since we know that this code will have to migrate to Data Refinery soon, it makes sense to have an interface here. The plan is that when we move to Data Refinery, this should be the only code we need to change.
  - The `field_definitions.py` file contains the definitions for each of the fields (columns) derived in the process. By abstracting these definitions out of the code and making them reusable, we achieve some great benefits. First, it becomes much easier to maintain. When the specifications change next year, we only need to make the change in one location. Next, it becomes much easier to test. We write unit tests for each of these definitions and can then reuse these definitions in many places without increasing risk.
  - The `processing_steps.py` file contains the core business logic of the diabetes data. We could consider breaking this down into further steps.

Note that we never store passwords or any sensitive credentials in the repo to prevent the situation where it can mistakenly committed into the git. There are several ways to deal with the secret, keys and passwords such as using Git Hooks or final cleansing process before publishing.

## External links

This is a really big topic and we don't want to replicate material that you can find elsewhere. Here are links to some resources that will give you as much detail as you want on this topic.

- [Packaging your Python project](https://packaging.python.org/tutorials/packaging-projects/)

- [Packages and modules from the official docs](https://docs.python.org/3/tutorial/modules.html#packages).
  _Good for understanding on how to organise and import sub-packages._

- [Why we share code as a .whl file](https://packaging.python.org/discussions/wheel-vs-egg/)
