---
title: Virtual environments

tags: 
  - Python
  - Virtual environments
  - Pip
  - Anaconda
---

#

## What are virtual environments?

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python environments for each project. This is one of the most important tools that most Python developers use.

## Why use virtual environments?

Virtual environments are a way to make sure your code will run correctly for you and others. By always coding inside a virtual environment, you make it more likely that your work will be usable by others.

If someone tries to run your code but they are using a different version of Python then it might fail. Likewise, if your code depends on some packages but your users have a different version of that package installed that might also fail.

Worse than this - if you have multiple projects then one project depends on 'my_example_library_v1' while another project needs to use 'my_example_library_v2' then both projects will break. Sometimes the code you have might depend on outdated versions of a package as the latest package update introduces bugs and issues. Or, you might have multiple versions of code that need different versions of packages to run.

![xkcd comic demonstrating a messy Python environment](../../../images/python_environment.png)

Virtual environments address these situations by keeping all of the packages and versions for each project separate. I can create a virtual environment called 'project-1-env' that uses Python 2.7 and 'my_example_library_v1'. I can create a second virtual environment called 'project-2-env' that uses Python 3.8 and 'my_example_library_v2'. As you move from working on one project to another, you just need to switch to the environment associated with that work.

It is good practice to always code inside a virtual environment.

## How to create a virtual environment

There are many ways to create virtual environments in python. This guide will go through the essentials for [creating a virtual environment with conda][create-venv-with-conda] and for [creating a virtual environment with venv][create-venv-with-venv].

## What is conda and venv?

Conda is an open source package and environment management system. It was created for Python programs, but it can package and distribute software for any language. The conda package and environment manager is included in all versions of Anaconda and Miniconda. 

- Conda is associated with the Anaconda package repository but, conda can use `pip` and pull from PyPI if needed.

- The advantage of using conda is that you can export and share environments using an `environments.yml` file which specifies the environment completely, including Python version. 

The venv module is part of python’s standard library and supports creating virtual environments, each with their own independent set of Python packages installed in their site directories. 

- Venv is associated with the PyPI package repository.

- The advantage of using venv is that it is ready to use with a fresh install of Python with no prerequisites, whereas to use conda you must first install a version of Anaconda.

!!! note
    
    You may not have a choice about which environment you can use. Your organisation may choose to use one over the other, and this might be dictated by their choice of systems, i.e. if they have chosen to make a "PyPi" mirror using "Bandersnatch", you will need to use venv.

[create-venv-with-conda]: ./conda.md
[create-venv-with-venv]: ./venv.md
