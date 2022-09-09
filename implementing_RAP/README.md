# Implementing RAP

These resources are not intended to be prescriptive. There are many ways to accomplish a task and teams have valid reasons for choosing other approaches. We hope that these resources are helpful for teams wanting to adopt good practices that they have heard about but don't know where to start.

This directory holds resources relevant to writing good code in any language.

## General Guidance

One of the most effective practices for quickly improving the capability of a team is **code review**.

- [Learn how to do effective code review to build capability in your team][3]

In NHS Digital we have committed to publishing more and more of our code over time to **improve the transparency** of our analytical work. We have a process in place to publish code safely.

- [Learn how to publish your code in the open][4]

Another topic we encounter frequently is the question of **when to use Jupyter notebooks**. These can be really helpful for exploratory work but also have some serious problems. This guide talks through the situations when you might use notebooks versus standard development tools.

- [Learn about the difference between using notebooks vs IDEs][5]

**Quality assurance** is a big and complex topic. This guide distills the activities listed in both the Aqua book and the 'Duck book' to give a template you can adapt for your own project.

- [Learn about creating the QA plan for your RAP project][6]

Adopting inconsistent data formats leads to a huge amount of wasted effort and can actually lead to very complex code. By adopting **tidy data format** for your work you can both improve your service to users and simplify your own production pipeline.

- [Learn how tidy data can help teams to use a consistent format][7]

It is important to follow coding best practices so that your code is readable and reproducible.

- [Learn how to code following best practices][23]

We have included a guide to help plan how to train your team.

- [Learn how to train your team][24]

## Git

Adopting **version control** is the single most important improvement that most analytical teams can make. This is a hard thing to do as a team but the effort pays off in a multitude of ways. We have two guides - the first explains the basics of using git while the second offers a real life explanation for how you might use it as a team.

- [Learn about the basics of git][8]

- [Learn how to use git collaboratively in your team][9]

## Python

> We are currently updating our minimal Python RAP package template, which is freely available to use via Github: [RAP package template](https://github.com/NHSDigital/rap-package-template).

We have many Python resources including basic operations, functions, structuring, error handling, visualisation and virtual environments.

- [A short primer on Python][10]

- [Learn how functions can improve your Python code][11]

- [Learn how to easily handle file paths in Python][12]

- [Learn how packaging your code can make it easier to share][13]

- [Learn how virtual environments can make your code more reliable][14]

- [Learn about logging and error handling in your code][15]

- [Learn about visualisations in Python][16]

The next guides talk about **testing**. Writing tests can initially seem like more work but the effort pays for itself in time saved debugging. The second guide offers a particularly useful way of deriving fields (columns) that can help in situations where there are a lot of changes to the specifications.

- [Learn how to design and write unit tests][17]

- [Learn about how to write and test field definitions in a way that is easy to understand and maintain][18]

- [Learn how to test that your new pipeline produces the same outputs as your historical code][19]

## PySpark

**PySpark** is a Python module that enables us to make use of distributed processing. It is available principally within the NHS Digital DAE/TRE. We have included a PySpark tutorial and a style guide to help with getting started.

- [Read our style guide for PySpark][20]

- [Work through some starter code in the PySpark tutorial script][21]

- [Read the benefits of using PySpark][22]

## R

The majority of our users use Python however, we have included some resources to make it easier to use R. We have a guide on how to use Git with RStudio as well as some links to external resources and contacts.

- [How to use Git with RStudio][1]

- [External resources][2]

[1]: ./R/git_with_RStudio.md
[2]: ./R/README.md
[3]: ./general_guidance/code-review.md
[4]: ./general_guidance/how-to-publish-your-code-in-the-open.md
[5]: ./general_guidance/notebooks_versus_ide_development.md
[6]: ./general_guidance/quality-assuring-analytical-ouputs.md
[7]: ./general_guidance/tidy-data.md
[8]: ./git/intro-to-git.md
[9]: ./git/using-git-collaboratively.md
[10]: ./python/basic-python-data-analysis-operations.md
[11]: ./python/python-functions.md
[12]: ./python/handling-file-paths.md
[13]: ./python/project-structure-and-packaging.md
[14]: ./python/virtual-environments.md
[15]: ./python/logging-and-error-handling.md
[16]: ./python/visualisation-in-python.md
[17]: ./python/unit-testing.md
[18]: ./python/unit-testing-field-definitions.md
[19]: ./python/backtesting.md
[20]: ./pyspark/pyspark-style-guide.md
[21]: ./pyspark/pyspark-tutorial.py
[22]: ./pyspark/README.md
[23]: ./general_guidance/coding-best-practice.md
[24]: ./general_guidance/training-your-team.md
