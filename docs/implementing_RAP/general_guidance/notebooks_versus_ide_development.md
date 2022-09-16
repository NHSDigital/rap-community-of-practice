# Notebooks vs IDE development

## What is this guide for?

This guide compares common tools used by data analysts/scientists when developing code:

1. Notebooks, such as Jupyter or Databricks - this guide will focus primarily on the latter
2. Integrated Development Environments, or IDEs, such as Visual Studio Code, PyCharm, Emacs

Specifically this guide compares writing notebooks in browser-based environments (such as Jupyter or Databricks) with writing text-based files (e.g. Python files with a .py extension) in IDEs: some IDEs do support notebooks, either in-built or configurable through plugins, e.g. Jupyter notebooks in Visual Studio Code, but we'll not consider those here.

At the end of this guide, the reader have a better understanding of the relative pros/cons of developing in browser-based notebooks versus IDEs and when/why they might choose one over the other for a given project.

### What if I don't have a choice?

This guide assumes you have a choice! Clearly, in some cases / projects, due to pre-existing infrastructure limitations, this choice is made for you.

Hopefully this guide will still prove useful for two reasons:

1. You can refer back to it in future projects when you have more flexibility
2. You can use the information to support requests for more / improved options when it comes to tooling

## Why should I care?

Software development is a key skill for data professionals seeking to implement reproducible pipelines. A core component of the development process is the tool used to actually develop the code.

The appropriate tool(s) will support the work being done - e.g. by spotting syntax errors or potential bugs - while inappropriate tools may prove a hinderance - e.g. autocompletion designed for a different language to the one being written.

Crucially, the choice of development tools can have consequences for many aspects of the project including, but not limited to:

- **Implementation of deliverables**: are you producing a software package or a piece of analysis? Who is the target audience? How will they interact with the outputs?
- **QA / review & testing processes**: how will your outputs be reviewed / checked? Will your code need to be updated and reviewed again later? Will everything be supervised by a human or do you need automated checks?
- **Reproducibility**: how will someone else reproduce your work? Are there any risks based on the tools you've used? E.g. think of notebook cells run out of order
- **Delivery speed & timescales**: do you need to quickly produce some charts / statistics? Will your project benefit from a longer time to set up over the lifespan?

More on these points below.

Ultimately, while there is not necessarily a 'right' or 'wrong' choice, it is worth taking the time to consider the options and pick the most appropriate tool for the job.

## External links

- [Quality Assurance of Code for Analysis and Research][2]
- Referenced below:
  - [Importing Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/4.x/examples/Notebook/rstversions/Importing%20Notebooks.html)
  - [%run command in Databricks](https://docs.databricks.com/notebooks/notebooks-use.html#run-a-notebook-from-another-notebook)

## Comparison

This section provides a high-level checkbox summary of the features provided by notebooks compared to IDEs, followed by a more detailed ellaboration on each point in the summary.

### Summary

The table shows a quick summary of the features of notebooks compared to IDEs. For more details on each point see the detailed breakdown in the following sections.

| Feature                                              | Notebooks | IDEs |
| ---------------------------------------------------- | :-------: | :--: |
| Interactive outputs (tables, plots, etc)             |     O     | X\*  |
| Storytelling and sharing results                     |     O     |  X   |
| Benefits out-of-the-box (minimal configuration)      |     O     |  X   |
| Deterministic outputs (i.e. same result every run)   |     X     |  O   |
| Supports modular code structure & packages           |     X     |  O   |
| Supports unit testing frameworks                     |     X     |  O   |
| Nice version control (e.g. readable git diffs)       |     X     |  O   |
| Autocomplete / autoformatting & syntax highlighting  |     X     |  O   |
| Compatible with sharing code external to NHS Digital |     X     |  O   |

\*See [Interactive cells in IDEs](#interactive-cells-in-ides)

#### Key

| Label | Description                     |
| ----- | ------------------------------- |
| X     | Unavailable / hard to configure |
| O     | Built-in / easy to set up       |

## Why use notebooks over IDEs?

### Sharing notebooks can lead to accidental PII disclosure!

Since notebooks are bundled with outputs from the most recent run, you will need to be extremely careful about accidental PII disclosure if you are sharing notebooks. For this reason using notebooks is not compatible with the 'Open Code' project. If you want to share your code with external users you should avoid notebooks. See the [open code guide for more info][1].

### Interactive outputs

One primary **feature of notebooks of any flavour is the interactivity**: code is written in (preferably small) snippets within cells, and each cell has its own output; often the output is interactive in some way - e.g. tables where the user can scroll through and select rows and columns, plots which can be zoomed or panned, and so on.

This functionality is **particularly useful in the exploration, analysis and prototyping phases** of a project, where the aim is to understand a dataset, either from a high level with visualisations or by digging deeper into some of the row-level data.

Interactivity simply isn't possibly in the same way with scripts/modules/etc in an IDE, which makes notebooks a good choice for analytical work, especially earlier on in the project timeline.

### Storytelling

Related to the interactivity of cell outputs, **notebooks offer a great way to tell stories with data**. Since (depending on the environment) cells can contain different types of code, from Python, R and SQL to Markdown, and cells containing code can be hidden to reveal only their outputs, it is possible to create a fully interactive, code-free presentation of analysis.

So for projects where presenting findings to stakeholders is a key components, notebooks offer a lot of functionality that will help support the analysts during delivery. Notebooks can even by exported as HTML files and the full analysis shared online (i.e. embedded in a webpage) or offline (i.e. as a static file).

### Quick & easy set up

Another nice benefit of notebooks is that they are generally set up to work out of the box. Whether opening a notebook in Databricks or Jupyter, the full development environment is often already their in a fairly complete form, enabling the users to get connected to the data and get started working right away.

IDEs on the other hand either come in two flavours: big,feature-heavy ones like Visual Studio (not code) take a lot of set up and plugins to get going; lightweight ones like Atom or Visual Studio Code are often little more than text editors out-of-the-box. While IDEs ofter almost limitless customisability (you can even write your own themes and extensions for a lot of them!) and powerful, development-enhancing functionality, they often take more time to get set up in the first place.

**IDEs also require you to have an adequate environment available** for them to be installed and used. This can be a problem, for instance, at NHS Digital, since installing software to local machines is often prohibited. Thus, in some cases, not only do you need to set up and configure the IDE to get the benefits, you also need to sort out the appropriate environment to install and use it in the first place.

**Notebooks can be much quicker and simpler to get started with** (especially if they are already set up for you!) allowing teams to start delivering on analytical projects straight away.

## Why use IDEs over notebooks?

### Deterministic / reproducible outputs

One of the key features of a RAP is the _R_: reproducibility.

When operating in tandem, two key drawbacks of notebooks are:

1. Cells are run in the order determined by the user
2. Cells share a _global scope_: variables, functions etc available within one cell are also available (for reading **and** writing) within others in the same notebook

Taken together, this allows downstream cells to impact upstream results.

![](../../images/notebook_cells_working_order.PNG#smallimg) ![](../../images/notebook_cells_broken_order.PNG#smallimg)

_It worked the first time (left), but not the second (right)!_

**This is bad for reproducibility**: it is possible for two analysts to generate different results from the same notebooks, based on the order in which cells are executed; moreover, in long notebooks it can be hard to spot that this effect is happening or from where it originated.

Writing a script within an IDE, on the other hand, makes it very difficult for this to occur - **scripts operate as DAGs**: the same set of logical steps will be executed in the same order every time the script runs.

For data pipelines which are intended to be rerun multiple times, potentially by different systems/users, scripts adhere to the RAP principles more readily than notebooks.

### Modular code & packages

It is easy in an IDE to write reusable pieces of code as classes and functions and to separate these out into (clearer named!) files and folders: this helps make larger projects more manageable and improves readability.

This is more challenging with notebooks, because importing functionality from notebooks can be complicated:

- Jupyter notebooks require quite a bit of arduous coding gymnastics to perform what in Python files would be simple imports ([importing Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/4.x/examples/Notebook/rstversions/Importing%20Notebooks.html))
- Databricks provides a magic `%run` command, which is essentially equivalent of inserting all the cells from the notebook being run into the current notebook ([%run command in Databricks](https://docs.databricks.com/notebooks/notebooks-use.html#run-a-notebook-from-another-notebook))

A note on Databricks specifically: it seems simple to import code across notebooks and thus to be able to break down longer notebooks into smaller, more manageable chunks. However, there is a catch: when `%run` is called, the two notebooks - the parent notebook where run is called and the child that is being run - share the same scope; this means that any variables, functions etc available for reading and writing in the cells of one notebook are available for reading and writing in the cells of the other.

![](../../images/databricks_notebook_parent_run.PNG#smallimg) ![](../../images/databricks_notebook_child_run.PNG#smallimg)

_The parent (left) errors because the child (right) causes hidden changes within the scope_

At best, this makes the code harder to understand, because after the `%run` there can be references to objects that are hidden in the child notebook. At worst, **this can introduce unintended side effects and lead to bugs**.

For larger projects, **writing code in a modular structure within an IDE improves code quality, readability and maintainability** compared to having extensive notebooks.

Another benefit relating to modularity is the ability to build packages: Python packages are essentially a collection of files bundled together containing the code and its dependencies. To build a Python package that other developers can install, use of other packages like `setuptools` or `poetry` is required. Unfortunately, these tools offer poor support for notebooks, so if one of the deliverables for a project you're working on is the code packaged up in a way that others can reuse and implement in their projects, then an IDE workflow is realistically the only way to achieve this.

### Support for unit testing

Hopefully, other pages in the RAP guides have conveyed the need for unit tests, along with some best practices when implementing them; this guide will not rehash these points. Assuming unit tests will be implemented in the project, this is much easier to do with scripts in an IDE compared to notebooks.

Partly, tests are easier to implement in an IDE workflow due to the modular structure mentioned above: code can be broken down into functions and classes contained within small, manageable files and subdirectories; this enables each test to only interact with the relevant part of the code and makes debugging easier.

Tests are harder to implement in notebooks because testing frameworks, such as unittest and pytest, do not properly support notebooks. While testing is possible in a notebook workflow, it is far from ideal, since it is hard to isolate code in each cell and thus to trace back sources of bugs.

### Nice version control

**Notebooks are inherently difficult to review and audit** through version control software like git: they are stored in a complicated (JSON) format internally, which enables is rendered nicely on screen for the user when viewed through the tool (e.g. Jupyter / Databricks), but it is hard to see differences between versions through tools like git.

![](../../images/git_diff_notebook.PNG#bigimg)

_Git diff from a (simple!) Jupyter notebook: lots to look at!_

**Text files (usually what is written in IDEs) are simple to version control** because it is easy to compare a line in the file between two given versions, since everything is designed to be read by humans. This makes it easy to understand what has changed between each version of a file and to rollback to previous versions if required.

![](../../images/git_diff_python_file.PNG#bigimg)

_Git diff from a Python file: much clearer!_

### Supports actually writing code

Where notebooks focus on analytical work, IDEs are designed for software development: they offer numerous features to support the person writing the code, through features like autocompletion and autoformatting to syntax highlighting and linting. IDEs can be configured to spot potential syntax errors and bugs at the time of writing, which makes spotting them much easier.

**IDEs often make writing code simpler and easier** by taking many of the tedious and monotonous away from the developer, often with the result that **code is faster to write, easier to read and of higher quality**. While some such features exist in notebooks, such as autoclosure of brackets and quotations, the scope of the functionality is quite limited.

### Interactive cells in IDEs

Some IDEs offer ways to use [Jupyter-like cells](https://code.visualstudio.com/docs/python/jupyter-support-py#_jupyter-code-cells) within scripts/modules: special comments in the code (e.g. VSCode and Spyder use `# %%`) are used to mark different 'cells'; the IDE or some extensions (e.g. the Python extension in VSCode) will identify these comments and allow code within a cell to be run 'interactively'; results from running interactive cells are stored in an IPython kernel that the IDE is running, but **no outputs are saved within the code or the metadata** as they with Jupyter notebooks.

Using interactive cells in IDEs can offer a nice balance for analysts implementing RAP in their working practices:

- Interactive cells allow for data [exploration and analysis through code](#interactive-outputs)
- But, since the cells are marked out by comments, the code is still a module or script, rather than a notebook
- This comes with all the [benefits of an IDE workflow](#why-use-ides-over-notebooks), without [risking accidental PII disclosure](#sharing-notebooks-can-lead-to-accidental-pii-disclosure).

## Where do I go from here?

Hopefully, it is clear that there is no 'right' or 'wrong' choice when it comes to workflow: rather it is a question of which workflow is going to better support the needs of the project.

As mentioned above, there is also a question of constraints: sometimes the tools available cannot be modified or added to.

Since this guide is targeting data analysts / scientists seeking to implement RAP practices, a recommended workflow that takes the best of working in notebooks and IDEs would be to

1. Start analytical pieces of work in notebooks, thus benefitting from the flexibility and interactivity - especially during the early phases of projects and when results need to be presented to wider audiences
2. As the codebase / pipeline grows, refactor the code into functions and classes contained within modules alongside a full test suite - this will help ensure that the outputs are reproducible and the code is maintanable, and it will be necessary when it comes to automating pipelines in production

The ONS best-practice team list [some of the problems with notebooks][2]:

> Notebooks are inherently difficult to review and audit through version control software like git. Simple text files like scripts can be version controlled easily as you can see which lines of text change from one version to another. Notebooks store their internal workings in a much more complicated format, hence seeing the changes from one notebook to another as differences line by line is not possible in common version control tools.

> Furthermore, defining and keeping functions within notebooks is prohibitive to testing. It is not simple to test individual cells of a notebook with standard external tooling.

> Lastly, one of the key issues with notebooks when they are used as methods for running a pipeline is the ability to run cells out of order. In practice this means that a user can accidentally execute the steps of the analysis in the wrong order causing issues and different results. As such, notebook results may not always be reproducible.

> [...]

> In short, notebooks are not suitable for modularising analysis pipelines [...] they should not be used as the main method of actually generating outputs

See also this video by Joel Grus: [I don't like notebooks](https://www.youtube.com/watch?v=7jiPeIFXb6U).

[1]: ./how-to-publish-your-code-in-the-open.md
[2]: https://best-practice-and-impact.github.io/qa-of-code-guidance/modular_code.html?highlight=notebooks#:~:text=Think%20carefully%20about%20whether%20notebooks%20are%20a%20suitable%20way%20to%20organise%20your%20code%23

<br></br>

<style>img[src*="#bigimg"] {
   width:100%;
}
img[src*="#smallimg"]{
    width:45%;
}
</style>
