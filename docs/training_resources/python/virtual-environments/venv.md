# Venv environment

The venv module is part of python's standard library. It supports creating lightweight virtual environments, each with their own independent set of packages installed in their site directories. A virtual environment is created on top of an existing python installation, known as the virtual environment’s “base” python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

When used from within a virtual environment, common installation tools such as pip will install python packages into a virtual environment without needing to be told to do so explicitly.

## How to create a virtual environment using venv
To create a new venv environment for your project, open a terminal and enter:

=== "Windows PowerShell"

    ```
    py -<python-version> -m venv <venv-directory>
    ```

=== "Linux/macOS"

    ```
    python<python-version> -m venv <venv-directory>
    ```

!!! note

    - The optional `<python-version>` tag specifies the python version you wish the virtual environment to run. If omitted, it will default to the latest python version installed on your system.

    - `<venv-directory>` is required and it specifies the directory in which you want to create your virtual environment.

    - In VS Code you can create a virtual environment by using the command `Python: Create Environment` available in the command pallete `CTRL + SHIFT + P`. This will also automatically install all the packages in a `requirements.txt` file. 

## How to activate a venv environment
To activate a venv environment open a terminal and enter:

=== "Windows PowerShell"

    ```
    <venv-directory>/Scripts/activate
    ```

    !!! note
    
        - On Windows you may be unable to run the activation script due to [execution policy](https://learn.microsoft.com/en-gb/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)

        - If you would like to use the Windows Command Prompt instead, the identification of file paths are specified with a backslash rather than a forward slash. It is recommended to use PowerShell as it can use either method.

=== "Linux/macOS"

    ```
    source <venv-directory>/bin/activate
    ```

## How to deactivate a venv environment
To deactivate the active venv environment open a terminal and enter:

```
deactivate
```

## How to install packages into a venv environment
To install packages to a venv environment using a `requirements.txt` file, first activate the target environment. For example, using Windows PowerShell: 

```
<venv-directory>/Scripts/activate
```

And then enter:

```
py -m pip install -r requirements.txt
```

## External links

- [Installing packages using pip and virtual environments][python-venvs]
- [Python Virtual Environments: A Primer][virtual-env-primer]

[python-venvs]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
[virtual-env-primer]: https://realpython.com/python-virtual-environments-a-primer/

*NHS Digital is not affiliated with any of these websites or companies.*
