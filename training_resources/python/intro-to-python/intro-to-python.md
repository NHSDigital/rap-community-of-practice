---
title: Intro to Python

tags: 
  - Coding tips
  - Python
  - Virtual environments
  - VS Code
  - PySpark
---

#

!!! tip "TLDR"
    - Python is a general-purpose, open-source programming language, good for data analysis, available on many data platforms
    - [VSCode](https://code.visualstudio.com/) is a good tool in which to develop Python. [PEP-8](https://peps.python.org/pep-0008/) is the widely used style guide.
    - We have guidance on [writing functions](python-functions.md), [data analysis in Python](basic-python-data-analysis-operations.md), [Python functions](python-functions.md), [unit testing](unit-testing.md), and much more in the left-hand sidebar. 


??? success "Pre-requisites"
    |Pre-requisite |  Importance |  Note |
    |--------------|-----------|------------|
    |[Levels of RAP][levels_of_rap] |  Necessary  |Python is a key component of our approach to RAP|
    |[Coding Best Practice][coding-best-practice]| Helpful |Some basic coding skills will help|

## What is Python?

Python is an open-source programming language famous for its ease of use. It has a simple syntax, which is easier to learn and read than most languages. 

It's also considered a 'high-level' language - this means you can get on with making code do what you want it to without worrying about overly technical aspects like assigning chunks of memory. This also has downsides; Python can run slower than other languages. 

Broadly, Python is considered the language of choice for data science, with a growing collection of helpful packages and is a popular choice for the kinds of scripting and automation which we need to do when building Reproducable Analytical Pipelines.

<!-- There's more information about Python available on the [official website](https://www.python.org/) -->

!!! note "Programming Environment"
    You'll need to have somewhere to work where you can run Python code to follow this guide. GitHub codespaces or Google Collab can be a nice tools to get started, however cannot be used for all of your work. It's a good idea to go over the [RAP readiness - resources](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/rap-readiness/#resources) guide to understand what you need (and might be missing) for RAP!

<!-- ## Installation

??? "Linux"
You can install Python via the commandline by entering
`    sudo apt-get install python3
   `
Alternatively, you can use your Linux flavour's package manager if you prefer.

??? "Windows"
There are two ways we can install Python on Windows.

    - The easiest is probably to download the installer [directly from the Python website](https://www.python.org/downloads/). When you run this, **make sure that you tick the option which says 'add to PATH?'**.
    - You can also install Python from the Microsoft Store. To do this, simply open the Store from your Start menu, search for Python, and click install.

??? "Mac"
As with Windows, there are two routes you can follow here.

    - You can download the [Mac installer directly from the Python website](https://www.python.org/downloads/macos/).
    - You could install via the commandline using the Homebrew tool. This involves a couple more steps - find a [guide here](https://docs.python-guide.org/starting/install3/osx/). -->

## Getting Started

You can write Python code in any program that allows you to write plain text. However, this is like running a marathon without any shoes on, uncomfortable and you are likely to run into some issues. Therefore we recommend using an Integrated Development Environment (IDE). IDEs are programs that make developing code much easier by providing a feature-rich toolset with tools such as:

* Editors
* Run-time environments
* Line numbering
* Variable Training
* Debugging tools
* Interpreters
* Auto-correction and suggestion

Whether you're new to coding or an old hand, we recommend using [Visual Studio Code](https://code.visualstudio.com/) (aka VSCode). This has a few benefits: it's feature-rich, lightweight, and works the same across multiple platforms (Windows, Mac, and Linux). It's also already installed on most NHS environments where you might want to write code.

Other IDE's are available, such as Spyder, Eclipse, PyCharm, Sublime, Atom, and more!
Some of our analytical environments use [Databricks](https://www.databricks.com/), in which you can write and execute Python code.

### Python In VSCode

Once you've installed and opened VSCode, you'll want to install the Python extension for VSCode.
![](../../images/extensions_img.png)
You can find the Extensions panel either by clicking the link above, or by pressing `ctrl + shift + x`.
From here you can search for and install the Python extension.
![](../../images/python_extension.png)
If you're familiar with working with Jupyter Notebooks, you can also download the Jupyter extension in the same way.

### Hello World

Now we want to use Python to run a simple script. Create a file called `hello_python.py` (in VSCode, you can just press `Ctrl + N` to make a file). In this new file, write

```
print("Hello World")
```

This is all the code we need to test our Python install. There's a couple of ways you can run this code:

- In VSCode, press `Ctrl + Shift + p`. This will bring up the Command Palette. You can do most things from here - try typing something which you're trying to do, and there's likely a command which will appear. In our case, we want to run the file, so we type `run file` and select the appropriate option - `run file in Terminal`.

![](../../images/vscode_run_file.png)

- As the screenshot shows, we can also run the file by using the keyboard shortcut `Ctrl + Shift + Enter`.

- Alternatively, we can run the same file from outside VSCode. Open a terminal and navigate to the space where you've written your script, then run the command:

```
python -m hello_python.py
```


Whichever method you use, you ought to see `Hello World` printed to the terminal.

### Environments and Packages

It's considered good practice to create a virtual environment for each of your Python projects - [we explain why on this page](virtual-environments/why-use-virtual-environments.md). There are many tools which you can use to create and manage your Python environments; we recommend reading our [guide to conda](virtual-environments/conda.md) and our [guide to venv](virtual-environments/venv.md) and picking one of these two. 

### Data Analysis in Python

Many consider Python to be the language of choice for data analysis. One of the things which makes Python powerful is the wide range of packages and tools available for the language -- this makes it flexible enough to be useful for small-scale analysis, which happens directly on your laptop and for larger projects which use cloud resources. 

To get started with analysis, take a look at our [guide to basic Python data analysis operations](basic-python-data-analysis-operations.md).

If you're using Databricks or otherwise working with large datasets and distributed computing, take a look at the documentation we have on Pyspark in the sidebar. You can start with [our page on what it is](../pyspark/README.md)

### SQL and Python

Whatever the scale of your data, you might need to interact with it via SQL queries. You can generate these using Python too - [check out our guide on how to to so](using-f-strings-sql-queries.md).

### Writing Python Code

There are as many opinions about what constitutes good code as there are coders. It's also always a good idea to adhere to a style guide. 

* For Python, we recommend using [`PEP-8`](https://peps.python.org/pep-0008/), which is also mentioned in our [Levels of RAP][levels_of_rap]
* more specifically, the [Google Python style-guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) (which is also the core of our [Pyspark style guide](../training_resources/pyspark/pyspark-style-guide/) )
* There are tools called **linters** which can be used to check for these styles automatically, such as [Pylint](https://pypi.org/project/pylint/)

Next, you'll want to know [how to structure your Python projects](project-structure-and-packaging.md), [how to write good functions](python-functions.md), and [how to approach unit testing in Python](unit-testing.md).

### Where Now?
You've now you've got Python installed and you've got an editor to work in. There's lots and lots of training resources about how to write Python code, here are some we've found useful:

- [Kaggle introduction to Python][Kaggle-intro-to-Python]
- [Govt Analysis Function Introduction to Python](https://analysisfunction.civilservice.gov.uk/training/introduction-to-python/)
- [freecodecamp](https://www.freecodecamp.org), which has a course tailored to learning [data analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/)

**There's also plenty of resources right here on this site** 

- check out our guide to [Python functions](python-functions.md).

[levels_of_rap]: ../../introduction_to_RAP/levels_of_RAP.md
[coding-best-practice]:../../implementing_RAP/coding-best-practice.md
[Kaggle-intro-to-Python]: https://www.kaggle.com/learn/python
