---
title: Glossary
tags:
  - Glossary
hide:
  - navigation
---

# 

## Conda

`conda` is also a virtual environment manager for python. Conda does not come pre-installed with python, but instead comes with Anaconda. You can find our advice on [how to use conda here](training_resources/python/virtual-environments/conda.md).

## Git

Git is a version control system which can help with keeping track of changes to code. Git isn't specific to python, and is used almost universally for coding. Git is a program which runs locally on your computer. Where git really comes into it's own, though, is when you use it to help with collaborating on code with others. Github and Gitlab are two websites which help to do this.

You can read more about git on our [introduction to Git](training_resources/git/introduction-to-git.md) page.

## IDE

An IDE (Integrated Development Environment) is a piece of software you can use to write code. You can write code anywhere that you can write plain text, but IDEs are designed to help with the process. It doesn't affect how the code will run, and you can move the code safely between IDEs.
IDEs are packed with useful features like autocompletion, test suites, git integration, linting and more. We recommend Visual Studio Code, but you can also try PyCham, Spyder, or Eclipse - to name a few.

## Pipeline

A data pipeline is a series of steps or processes that are used to collect, process, and transform data from various sources into a format that can be easily used. The pipeline typically includes data ingestion, data cleaning, and some analysis. A good pipeline can automate work as well as improving the quality of the outcomes.

## RAP

RAP stands for Reproducible Analytical Pipelines. The term comes from UK public sector data scientists - you can [read the ONS description here](https://datasciencecampus.ons.gov.uk/capability/data-science-campus-faculty/reproducible-analytical-pipeline-journey/#:~:text=Reproducible%20Analytical%20Pipelines%20are%20programs,impressive%20efficiencies%20in%20your%20teams.). We also have a page on [why RAP is important](introduction_to_RAP/why_RAP_is_important.md)

## Venv

`venv` is a particular package for managing virtual environments in Python, which comes pre-installed with python. We highly recommend using this package, although others are available. See [our page](training_resources/python/virtual-environments/venv.md) for advice on using it.

## Virtual Environments

Virtual environments are a way to ensure that you have maximum control over the code that you're writing and how it will run. Many software packages interact with one another, and not always in a good or predictable way. Virtual environments allow you to develop code like it is being done on a completely clean, separate machine. In a virtual environment, you can install whatever packages you want, at whatever version, without worrying about affecting the other software or projects you might have on your computer.

Best practice recommends that we create a different virtual environment for each project that we work on.