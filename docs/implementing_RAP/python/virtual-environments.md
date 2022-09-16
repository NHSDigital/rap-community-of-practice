# Virtual environments

## What is a virtual environment and why should I care?

Virtual environments are a way to make sure your code will run correctly for you and others. By always coding inside a virtual environment, you make it more likely that your work will be usable by others.

If someone tries to run your code but they are using a different version of python then it might fail. Likewise, if your code depends on some packages but your users have a different version of that package installed that might also fail.

Worse than this - if you have multiple projects then one project depends on 'my_example_library_v1' while another project needs to use 'my_example_library_v2' then both projects will break. Sometimes the code you have might depend on outdated versions of a package as the latest package update introduces bugs and issues. Or, you might have multiple versions of code that need different versions of packages to run.

Virtual environments address these situations by keeping all of the packages and versions for each project separate. I can create a virtual environment called 'project-1-env' that uses python 2.7 and 'my_example_library_v1'. I can create a second virtual environment called 'project-2-env' that uses python 3.8 and 'my_example_library_v2'. As you move from working on one project to another, you just need to switch to the environment associated with that work.

It is good practice to always code inside a virtual environment.
<br/>

## Conda environment

Conda is a package manager that we use to create and manage our virtual environments.

Conda is bundled with Anaconda, which is a distribution software that contains package managers and applications in R and Python. See [these instructions][install-anaconda] on how to install and setup Anaconda.

You can interact with conda via the Anaconda Prompt for Windows, or in a terminal window for Mac/Linux. By inputting commands in the command prompt you can then create and manage your virtual environments using the conda package manager.

See the [Anaconda user guides][conda-getting-started] for more information on getting started with conda.

## How to create a new virtual environment using conda

To create a new conda virtual environment for your project, open the Anaconda Prompt (Windows) or a terminal window on Mac/Linus and enter:

```
conda create --name myenvironment python=3.9
```

- The `--name` tag specifies a name for the environment: in this example the environment will be named "myenvironment", but you can replace this will something better suited to your project.
- `python=3.9` specifies python version you wish the virtual environment to run, in this case version 3.9.

To check the packages that are installed in the [active environment](#how-to-activate-an-environment), enter:

```
conda list
```

To install a package the active environment:

```
conda install pandas
```

To create an environment, specify the Python version and install multiple packages in **one line**:

```
conda create --name mynewenvironment python=3.8 pandas 3.1.0 flake8 3.9.2 numpy
```

Notice how the versions for pandas and flake8 are specified but no version is given for numpy. This will result in all versions of numpy being installed.

- **TIP:** It is **recommended** to install all packages in one go (e.g. numpy, pandas, pytest etc). Installing 1 package at a time could cause potential package dependecy conflicts (see [Dependency Hell][dependency-hell]).

If you're unsure a specific package is installed in the current environment simply search:

```
conda search flake8
```

For more information on managing environments and other commands such as updating your environment's packages, check out [Managing environments with Conda][managing-conda-envs].
<br/>

## How to activate an environment

The 'active' environment is the one that conda will reference when you enter any commands, e.g. new packages will be installed into the active environment, the installed package list will be based on the active environment, etc.

When you start a new Anaconda Prompt (Windows) or open a new terminal (Mac/Linux), the active current environment is set to `base`.

To activate an environment, enter:

```
conda activate mynewenvironment
```

As above, "myenvironment" specifies the name of the environment and can be replaced with the specific name of the environment you wish to activate.

## How to export and share environments

To ensure reproducibility, it is important that we can export virtual environments and share them alongside the code. In this way, someone else will be able to run your code with exactly the same environment (packages, dependencies etc) as you did. This helps address the classic 'it works on my machine' problem.

There are a few options for how to export environments and recreated environments from exported files.

### Pip requirements.txt

If you followed the [Project structure and package organisation][1] guide, you will have created a `requirements.txt` file in your repository, which specifies all the python packages you wish to install.

- The benefit of a requirements.txt file created with Pip is that anyone with a Python installation should be able to install it (i.e. someone else wouldn't need to have conda installed)
- The drawback is that the requirements.txt file offers an incomplete specification for the environment (for example, it does not specify the python version), so projects using requirements.txt files must be careful to specify any additional dependencies in another way (e.g. via a README).

To create a working conda environment using the requirements.txt file, simply follow the conda environment creation commands from above and instead of the simple package installation, first activate the target environment:

```
conda activate mynewenviroment
```

And then enter:

```
conda install --file requirements.txt
```

### Conda environment.yml

Conda offers a way to export and share environments via a yaml file.

- The benefit of this approach is that the output file gives a more complete picture of the dependencies for a project than a requirements.txt file from Pip.
- The drawback is the someone would need to have conda installed to use your project: if you work in an organisation or team that consistently uses conda then this is not as relevant, but it may be more relevant if you want to distribute you project to others who may not use conda.

To export the active environment:

```
conda env export > environment.yml
```

The resulting file can be used to completely rebuild a conda environment:

```
conda env create --file environment.yml
```

## How to remove an environment

Make sure your environment is not active by typing:

```
conda deactivate
```

This will take you back to the base conda environment. Then to delete your specified environment:

```
conda env remove --name mynewenvironment
```

## Conda help command

Type the following command for a list of helpful terminal commands:

```
conda env --help
```

## See Also

### Using Spyder with conda environments

Spyder is a Python IDE that is bundled with Anaconda during installation. It can be tricky to set up Spyder to work with multiple conda environments: see [this guide][spyder-conda-envs] for instructions on how to do this.

### Using Docker with Data Refinery

[Docker][docker-getting-started] is a container manager that offers many solutions and applications for managing your environments. Currently at NHS Digital we cannot use Docker due to compatibility issues. This may change in the future so we will update the resources on this page accordingly.

## External links

- [Python virtual environments and package][python-venvs]
- [Installing Anaconda][install-anaconda]
- [Getting started with Conda][conda-getting-started]
- [Managing environments with Conda][managing-conda-envs]
- [Conda commands cheatsheet][conda-cheatsheet]
- [List of other package managers][package-managers]
- [Using up Spyder with conda environments][spyder-conda-envs]

[python-venvs]: https://docs.python.org/3/tutorial/venv.html
[install-anaconda]: https://docs.anaconda.com/anaconda/install/index.html
[conda-getting-started]: https://conda.io/projects/conda/en/latest/user-guide/getting-started.html
[managing-conda-envs]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
[conda-cheatsheet]: https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html
[package-managers]: https://en.wikipedia.org/wiki/List_of_software_package_management_systems
[docker-getting-started]: https://docs.docker.com/get-started/overview/
[dependency-hell]: https://en.wikipedia.org/wiki/Dependency_hell
[spyder-conda-envs]: https://github.com/spyder-ide/spyder/wiki/Working-with-packages-and-environments-in-Spyder
[1]: ./project-structure-and-packaging.md
