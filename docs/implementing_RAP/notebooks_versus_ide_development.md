# Development tools

## What is this guide for?

This guide compares common tools used by data analysts/scientists when developing code:

1. iPython notebooks, such as Jupyter or Databricks - this guide will focus primarily on the latter
2. Integrated Development Environments (IDEs), such as Visual Studio Code, PyCharm, Spyder

Specifically this guide compares writing notebooks in browser-based environments (such as Jupyter or Databricks) with writing text-based files (e.g. Python files with a .py extension) in IDEs.

At the end of this guide, the reader have a better understanding of the relative pros/cons of developing in browser-based notebooks versus IDEs and when/why they might choose one over the other for a given project.

??? Question "What if I don't have a choice?"

    Clearly, in some cases / projects, due to pre-existing infrastructure limitations, this choice is made for you.

    Hopefully this guide will still prove useful as:

    1. You can refer back to it in future projects when you have more flexibility
    2. You can use the information to support requests for more / improved options when it comes to tooling

## Why should I care?

A core component of the development process of a reproducible analytical pipeline is the tool used to actually develop the code.

The appropriate tool(s) will support the work being done - e.g. by spotting syntax errors or potential bugs - while inappropriate tools may prove a hindrance - e.g. autocompletion designed for a different language to the one being written.

The choice of development tools can have consequences for many aspects of the project including, but not limited to:

- **Implementation of deliverables**: are you producing a software package or a piece of analysis? Who is the target audience? How will they interact with the outputs?
- **QA / review & testing processes**: how will your outputs be reviewed / checked? Will your code need to be updated and reviewed again later? Will everything be supervised by a human or do you need automated checks?
- **Reproducibility**: how will someone else reproduce your work? Are there any risks based on the tools you've used? E.g. think of notebook cells run out of order
- **Delivery speed & timescales**: do you need to quickly produce some charts / statistics? Will your project benefit from a longer time to set up over the lifespan?

Ultimately, while there is not necessarily a 'right' or 'wrong' choice, it is worth taking the time to consider the options and pick the most appropriate tool for the job.

## Notebooks vs. IDEs

The table below gives a summary of the features of notebooks compared to IDEs. For more details on each point see the detailed breakdown in the following sections.

| Feature                                              | Notebooks | IDEs |
| ---------------------------------------------------- | :-------: | :--: |
| Interactive outputs (tables, plots, etc)             |     O     | X\*  |
| Storytelling and sharing results                     |     O     |  X   |
| Benefits out-of-the-box (minimal configuration)      |     O     |  X   |
| Deterministic outputs (i.e. same result every run)   |     X     |  O   |
| Supports modular code structure & packages           |     X     |  O   |
| Supports unit testing frameworks                     |     X     |  O   |
| Nice version control (e.g. readable git diffs)       |     X     |  O   |
| Autocomplete / auto-formatting & syntax highlighting |     X     |  O   |
| Compatible with sharing code external to NHS Digital |     X     |  O   |

??? Info "Key"

    X: Unavailable / hard to configure

    O: Built-in / easy to set up

    <sub>\*See [Interactive cells in IDEs?](#interactive-cells-in-ides)</sub>

## Benefits of notebooks

Notebooks are a great tool for data exploration and quick ad hoc discovery. However they are not great for collaborative projects, and ==**sharing notebooks can lead to accidental PII disclosure**==.

> Since notebooks are bundled with outputs from the most recent run, you will need to be extremely careful about accidental PII disclosure if you are sharing notebooks.

### Interactive outputs

The primary feature of notebooks of any flavour is the interactivity. Code in notebooks is written in snippets within sections called 'cells' where each cell has its own output; often interactive in some way - e.g. tables where the user can scroll through and select rows and columns, plots which can be zoomed or panned, and so on.

This is **useful for the exploration, analysis and prototyping phases of a project**, where the aim is to understand a dataset, either by creating visualisations or by digging deeper into some of the row-level data.

Interactivity ith scripts/modules/etc in an IDE isn't always possible or especially easy, which makes notebooks a good choice for ad hoc analytical work, especially earlier on in the project timeline.

### Markdown cells

Notebook cells can contain different types of content: Python, R and SQL but also Markdown which allows you to format text. This means you can add additional non-code content to notebooks, for example adding headings, bullet points, inserting images, and many other things. Cells containing code can be hidden to reveal only their outputs so that you can create a fully interactive, code-free presentation of analysis- great for presenting findings to stakeholders.

Notebooks can be exported as HTML files and the full analysis shared online (i.e. embedded in a webpage) or offline (i.e. as a static file). This saves you from having to create a separate report, and manually copying outputs over, and outputs automatically updating if changes are made to the code.

### Quick to get up and running

Notebooks are generally set up to work out of the box, enabling the users to connect to the data and get started working right away.

IDEs on the other hand either come in two flavours: big, feature-heavy ones take a lot of set up and plugins to get going; lightweight ones like Atom or Visual Studio Code are often little more than text editors out-of-the-box. While IDEs offer almost limitless customisability (you can even write your own themes and extensions for a lot of them!) and powerful, development-enhancing functionality, they often take more time to get set up in the first place.

> IDEs require you to have an adequate environment for them to be installed, used and customised (i.e. installing useful extensions). This can be prohibitive, for instance at NHS Digital where installing software to local machines is restricted.

## Benefits of IDEs

The best IDEs incorporate some of the benefits of notebooks, while also allowing better version control, and easier development of reproducible code.

### Deterministic code

For data pipelines which are intended to be rerun multiple times, potentially by different systems/users, **scripts in an IDE adhere to the RAP principles more readily than notebooks**.

In a notebook, it is possible for two analysts to generate different results from the same notebooks, based on the order in which cells are executed. In long notebooks it can be hard to spot this happening or where it originated.

Writing a script within an IDE makes it difficult for this to occur as the same set of logical steps will be executed in the same order every time the script runs.

### Modularisation

In an IDE it's easy to write reusable pieces of code and separate these out into clearly named files and folders that can be imported into the main pipeline. For larger projects, **writing code in a modular structure within an IDE improves code quality, readability and maintainability** compared to having extensive notebooks.

This is more challenging with notebooks, because importing functionality from notebooks can be complicated:

#### Importing code in Jupyter notebooks

Jupyter notebooks require quite a bit of arduous coding gymnastics to perform what in Python files would be simple imports ([importing Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/4.x/examples/Notebook/rstversions/Importing%20Notebooks.html))

#### Importing code in Databricks notebooks

Databricks provides a magic `%run` command, which is essentially equivalent of inserting all the cells from the notebook being run into the current notebook ([%run command in Databricks](https://docs.databricks.com/notebooks/notebooks-use.html#run-a-notebook-from-another-notebook))

When `%run` is called, **the two notebooks share the same scope**; this means that any objects (variables, functions etc.) available for reading and writing in the cells of one notebook are available for reading and writing in the cells of the other.

![Explanation of the %run command being called](../images/databricks_notebook_parent_run.PNG#smallimg) ![Explanation of what the %run command is calling](../images/databricks_notebook_child_run.PNG#smallimg)

_The parent (left) errors because the child (right) causes hidden changes within the scope_

After the `%run` there can be references to objects that are hidden in the child notebook. This can make code **harder to understand, introduce unintended side effects and lead to bugs**.

### Unit testing

> Please see the [unit tests][3] guide for more information about unit testing.

It is much easier to implement unit tests with scripts in an IDE than in notebooks. This is partly due to the [modular structure](#modularisation): code can be broken down into functions and classes contained within small, manageable files and subdirectories; each test then only interacts with the relevant part of the code which makes debugging easier.

Testing frameworks, such as unittest and pytest, do not properly support notebooks. While testing is possible in a notebook workflow, it is hard to isolate code in each cell and thus to trace back errors.

### Version control

**Notebooks are inherently difficult to review and audit** through version control software like [Git][4]. They are stored in a JSON format, which is rendered nicely on screen for the user when viewed through the tool (e.g. Jupyter / Databricks), but which makes it hard to see differences between versions.

![Image showing how Git is viewed in Notebooks](../images/git_diff_notebook.PNG#bigimg)

_Git diff from a (simple!) Jupyter notebook: lots to look at!_

Files in IDEs are generally simpler to version control. It is easy to compare a line in a file between two given versions since everything is designed to be read by humans. This makes it easy to understand what has changed between each version of a file and to rollback to previous versions if required.

![Image showing how Git is viewed in a Python file](../images/git_diff_python_file.PNG#bigimg)

_Git diff from a Python file: much clearer!_

### Package building

Python packages are essentially a collection of files bundled together containing the code and its dependencies.

To build a Python package that other developers can install, use of other packages like `setuptools` or `poetry` is required. Unfortunately, these tools offer poor support for notebooks, so if one of the deliverables for a project you're working on is the code packaged up in a way that others can reuse and implement in their projects, then an IDE workflow is realistically the only way to achieve this.

### Additional features

Notebooks are focused on analytical work, but IDEs are designed for software development: they offer features to support the person writing the code, such as auto-completion & formatting as well as syntax highlighting and linting.

These features can make **writing code in IDEs faster and easier** with the result that **code is easier to read and of higher quality**. While some such features exist in notebooks, such as auto-closure of brackets and quotations, the scope of the functionality is quite limited.

## Interactive cells in IDEs

Some IDEs offer ways to use [Jupyter-like cells](https://code.visualstudio.com/docs/python/jupyter-support-py#_jupyter-code-cells) within scripts/modules: special comments in the code (e.g. VSCode and Spyder use `# %%`) are used to mark different 'cells'; the IDE or some extensions (e.g. the Python extension in VSCode) will identify these comments and allow code within a cell to be run 'interactively'; results from running interactive cells are stored in an IPython kernel that the IDE is running, but **no outputs are saved within the code or the metadata** as they with Jupyter notebooks.

Using interactive cells in IDEs can offer a nice balance for analysts implementing RAP in their working practices. This comes with all the [benefits of an IDE workflow](#benefits-of-ides), without risking accidental PII disclosure.

## External links

- [Quality Assurance of Code for Analysis and Research](https://best-practice-and-impact.github.io/qa-of-code-guidance/modular_code.html#think-carefully-about-whether-notebooks-are-a-suitable-way-to-organise-your-code)
- [Importing Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/4.x/examples/Notebook/rstversions/Importing%20Notebooks.html)
- [%run command in Databricks](https://docs.databricks.com/notebooks/notebooks-use.html#run-a-notebook-from-another-notebook)
- See also this video by Joel Grus: [I don't like notebooks](https://www.youtube.com/watch?v=7jiPeIFXb6U).

## Where do I go from here?

Hopefully, it is clear that there is no 'right' or 'wrong' choice when it comes to workflow: rather it is a question of which workflow is going to better support the needs of the project.

We have created a [suggested workflow][5] that is not intended to be seen as the recommended or best approach, but offers a good starting point for analysts & data scientists looking to get started setting up a workflow.

[1]: ./how-to-publish-your-code-in-the-open.md
[2]: https://best-practice-and-impact.github.io/qa-of-code-guidance/modular_code.html?highlight=notebooks#:~:text=Think%20carefully%20about%20whether%20notebooks%20are%20a%20suitable%20way%20to%20organise%20your%20code%23
[3]: ../training_resources/python/unit-testing.md
[4]: ../training_resources/git/intro-to-git.md
[5]: ../implementing_RAP/technical-workflow.md

<br></br>

<style>img[src*="#bigimg"] {
   width:100%;
}
img[src*="#smallimg"]{
    width:45%;
}
</style>
