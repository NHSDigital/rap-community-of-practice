# Technical Working Setup & Best Practices

> **Note:** This guide (and most of this repository) is written primarily for Python development but some parts are generally applicable to other languages.

When you are developing a codebase (perhaps for the first time), especially a [RAP][1] codebase, that uses [functions][2] stored in [different directories][3], it can be tricky to know how to easily edit code, experiment with different sections of the pipeline, test other people's changes and debug errors.

This guide includes sections on:

- [What you will need to get started](#what-you-will-need-to-get-started)
- [A typical workflow](#typical-workflow), including [how to develop code](#tips-for-how-to-write-code)
- [Debugging tips](#debugging)

> If you run into issues with anything in this guide, one of the best places to find answers is by searching for your problem on [StackOverflow](https://stackoverflow.com/).

## What is this guide for?

Setting up a technical working environment is a skill that takes **time and energy to learn**, and so it may be tempting to stick to "out-of-the-box" solutions such as the interactive platform on your Python training course, Google Collab, or Jupyter. These are great tools for prototyping, learning and experimenting, but **there are many [pitfalls][4] to relying solely on "out-of-the-box" solutions**.

At the end of this guide, the reader should feel more comfortable setting up and using their own technical development environment.

> Your employer/educator may have restricted your ability to change any part of your technical working environment. If this is the case, then hopefully this guide will at least help your understand more about your current setup.

## What you will need to get started

You will need the following, either on your local machine, or on a [virtual machine that you will need to connect to](#code-should-generally-not-run-on-your-local-machine). How to set up and connect to a virtual machine is **_not_** in the scope of this guide.

- A working [Python](https://www.python.org/downloads/) installation. We recommend using the [Anaconda Python distribution](https://docs.anaconda.com/anaconda/) if you are going to use a [conda environment][5].
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

??? note info "This may need to be configured the first time you use it"

    ```bash
        git config --global user.name "Your Name Here"
        git config --global user.email youremail@example.com
    ```

### Code should generally not run on your local machine

Your local machine refers to your computer processing power on your laptop itself. Logging into a platform that allows you to access virtual computation, using AWS or similar _does not_ count as a local machine, that is what we call a 'virtual machine'.

Using a virtual machine ensures:

- Confidentiality: many projects at the NHS involve sensitive data and needs to be protected, which means only working with it in a secure computing environment.
- Computing Power and Scalability: We can use computing resources with more power than a single laptop, and scale them up and down as needed.
- Collaboration: Working with others in a shared environment can help reproducibility, especially at the start of a project.

However, this does not mean that your local machine cannot be used for code development, as long as nothing sensitive is contained in the code.

## Typical Workflow

There is no 'right' or 'wrong' choice when it comes to workflow, and it is important that you feel comfortable with the tools you use to develop your code. It is also important that the workflow supports the needs of the project.

However, there are a lot of different setups and when you are new to Python/code, it can be reassuring to follow a suggested workflow, which we have included below.

**TL;DR**: aim to start analytical pieces of work in notebooks. As the codebase / pipeline grows, refactor the code into functions and classes contained within modules alongside a full test suite - this will help ensure that the outputs are reproducible and the code is maintainable, and it will be necessary when it comes to automating pipelines in production

!!! Tip

        If you do use interactive notebooks (i.e. Jupyter notebooks, .ipynb files), make sure \*.ipynb is added to your [.gitignore file][6] so that all interactive python notebooks are not tracked. Read more about why in this [guide][4].

### Starting a project

Here is a workflow to get you up and running with any new data science project. (Example code either shown or available via the links provided)

1.  Log in to virtual network. (_optional, but [recommended](#code-should-generally-not-run-on-your-local-machine)_)
2.  [Create a new conda environment][7] for your project and install any packages you know you will need
3.  [Activate your conda environment][8]
4.  Create a new directory (folder) for your project in your preferred location
5.  Navigate inside the directory in the [terminal][9], and [initialise][10] the Git repository

        cd your-project-name
        git init

6.  Open the directory in [VS Code, or an editor of your choice][11]

        code .

7.  Create a `README.md` and give your project a title
8.  Create a [`.gitignore`][6]. There is a useful VS Code [extension](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore) for setting up your `.gitignore` file.
9.  Prototype code using [interactive cells][12] and/or [notebooks][13]
10. Write code in .py files, separating out [functions][14] into [modules][3] (directories) where appropriate
11. Test functions in interactive console
12. Use [linters][15] to make any formatting corrections
13. Export your package requirements & dependencies to an [environment.yml][16] file

        conda env export --from-history --no-builds  | grep -v "prefix" > environment.yml

14. [Git add and commit][10] the files you have created
15. Create a new repo on GitHub or GitLab then follow the instructions to push your code from your project directory to that repo, this will probably look something like:

        git remote add origin https://www.github.com/yourname/your-repo-name.git
        git push origin main

And now you're ready to go.

### Working on an existing project

When you are working on an existing project, many of the above steps are no longer needed, and you may need to add in a few extras. (Example code either shown or available via the links provided)

1.  Log in to virtual network. (_optional, but [recommended](#code-should-generally-not-run-on-your-local-machine)_)
2.  Navigate inside the directory in the [terminal][9]

        cd your-project-name

3.  [Activate your conda environment][8]
4.  Check the current state of the project and make sure you're on the right branch for what you're doing using `git status`
5.  (Make sure your local version of the project is up to date with GitHub using `git pull`). _Optional as you're likely the only one working on your branch_
6.  Open the directory in [VS Code, or an editor of your choice][11]
7.  Prototype code using [interactive cells][12] and/or [notebooks][13]
8.  Write code in .py files, separating out [functions][14] into [modules][3] (directories) where appropriate
9.  Test functions in interactive console
10. Use [linters][15] to make any formatting corrections
11. If you've added any new packages, make sure to update your [environment.yml][16] file:

        conda env export --from-history --no-builds  | grep -v "prefix" > environment.yml

12. [Git add and commit][10] the files you have changed
13. [Git push][10] the staged changes
14. When you are ready to create a pull/merge request, you will need to check that your working branch is up-to-date with the main branch and [deal with any merge conflicts][17]. (_optional, only create a pull request once you are happy with your changes and want them to be reflected in the main branch_)

        git pull origin main

15. Create a [pull/merge request][18] (_optional, see above_)

### Tips for how to write code

_Intended as broad advice for people who may not be very confident in Python and are nervous about 'breaking' an existing codebase_.

- **You can't really break anything if you've version controlled it properly**. You can always revert back to a previous point in the codebase history.
- **Your code doesn't have to be clean while you're developing it**. When they are just starting to get to grips with RAP, some people can be nervous about writing code that isn't all contained in functions, or otherwise "nice and clean". It is totally ok for your code to start out messy. Ideally you would make commits frequently when your code is a bit nicer, but to test and try out, messy code is completely fine.
- **Get something working, and then refine it**. The most important thing is that you get the output that you want. Then you can go back and refine your code. You can figure out where you've repeated code which should indicate that you can make use of, or create new functions.
- **Don't attempt everything all at once**. If you have to write a piece of code that produces a calculated output in a particular format for multiple years and regions, start simple! Start with the output, and maybe start with just one year and one region. Then plug in the formatting, and then expand to other years and regions.

## Debugging

It is much easier to debug code to run through it **step-by-step** on a sample of the data. This is especially true when you are trying to run code made up of different functions coming from different modules.

- Interactive tools such as [interactive cells][12] and [notebooks][13] can provide an easy way to do this. Interactive cells have the benefit of being insertable within the code being developed itself, whereas at other times it's helpful to create an entirely new jupyter notebook to put bits of code in and interrogate each output.
- Another common strategy is to create a **blank Python file**, such as `temp.py`, and only include the bits of code that you want to run, perhaps making use of interactive cells without changing the body of code that is version controlled.
- You can also **insert breakpoints**, using `breakpoint()` in your code, to only run code up to a specified point, which helps you to interrogate your variables to figure out why something isn't working. To proceed to the next breakpoint, type `continue` into the terminal.
- An alternative to manually inserting breakpoints is built-in debuggers, something that most IDEs offer, including VS Code. However these can debuggers can require a steep learning curve and it can sometimes hinder progress initially to use them.

If you do want to use any of these strategies, it's important to make sure that:

- temp.py is added to your .gitignore file
- all jupyter notebooks are automatically ignored. You can do this by adding `*.ipynb` to your .gitignore. This means that all files with the `.ipynb` extension will not be tracked.
- any interactive cells you create are not committed into your codebase. This is not as important as the previous two points, and is more best practice than something to avoid at all costs, but it is advisable, especially when working on collaborative projects to not commit anything interactive as you cannot be sure that the cells will operate in the same way on somebody else's machine due to the setup required.

## Acknowledgements

Inspiration has been drawn from:

- [Step-by-Step Guide to Setting Up a Professional Data Science Environment on Windows](https://www.projectdatascience.com/step-by-step-guide-to-setting-up-a-professional-data-science-environment-on-a-windows/)
- [My Computer Setup for Data Science](https://data36.com/computer-setup-data-science/)
- [The Definitive Data Scientist Environment Setup](https://whiteboxml.com/blog/the-definitive-data-scientist-environment-setup)
- [Setup a Data Science Environment on your Computer](https://www.datacamp.com/tutorial/setup-data-science-environment)
- [VS Code documentation](https://code.visualstudio.com/docs/)

[1]: ../introduction_to_RAP/why_RAP_is_important.md
[2]: ../training_resources/python/python-functions.md
[3]: ../training_resources/python/project-structure-and-packaging.md
[4]: ./notebooks_versus_ide_development.md
[5]: ./tools.md#conda-environment
[6]: ../training_resources/git/intro-to-git.md#the-gitignore-file
[7]: ../training_resources/python/virtual-environments.md#how-to-create-a-new-virtual-environment-using-conda
[8]: ../training_resources/python/virtual-environments.md#how-to-activate-an-environment
[9]: ./tools.md#the-terminal
[10]: ../training_resources/git/intro-to-git.md#common-basic-commands
[11]: ./tools.md#code-editing
[12]: ./tools.md#interactive-cells-in-vs-code
[13]: ./tools.md#interactive-python-notebooks
[14]: ../training_resources/python/python-functions.md
[15]: ./tools.md#linting-in-vs-code
[16]: ../training_resources/python/virtual-environments.md#conda-environment
[17]: ../training_resources/git/using-git-collaboratively.md#resolving-merge-conflicts
[18]: ../training_resources/git/using-git-collaboratively.md
