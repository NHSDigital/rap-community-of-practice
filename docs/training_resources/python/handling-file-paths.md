# Handling file paths

## What is pathlib?

pathlib is a built-in (python-3) package for handling filesystem paths.

pathlib offers helpful ways to perform a variety of operations, including:

- Specifying paths to files / folders using simple, clear syntax
- Traversing the filesystem (i.e. getting the parents / children of a given file / folder)
- Composing paths based on constituent elements (e.g. by extending a root path to a folder with a subfolder / file name)

See [How do I use it?](#how-do-i-use-it) for examples illustrating the above.

## Why should I care?

The key strengths of pathlib include:

- **Simplicity**: pathlib objects are easy to create, extend and reuse
- **Functionality**: pathlib offers functionality that storing paths inside strings does not, including
  - Getting file names and stems (aka names without extensions)
  - Getting the names of parent folders
  - Accessing the name of the current working directory
  - Listing the contents of nested folders
- **Reusability**: pathlib is OS-agnostic, meaning code will work with both Windows and Linux filesystems

## How do I use it?

The steps below show briefly how to make use of pathlib.

This is by no means an exhaustive walkthrough for everything you can do with pathlib - for more information, see the [pathlib-docs](https://docs.python.org/3/library/pathlib.html).

## Getting started

Import pathlib or pathlib2 (the python-2 backwards compatible version)

```python
import pathlib
```

In pathlib, `pathlib.Path` objects are the key components. You can define
Path objects and access attributes / methods to perform a wide variety of
operations

For example, you can access the current working directory with the `cwd` attribute.

```python
# Print the current working directory (cwd)
print("CWD:", pathlib.Path.cwd())
```

Pass strings to Path constructor to create a Path object

```python
# . is the current directory
cwd_path = pathlib.Path(".")
print("CWD (again):", cwd_path)

# Use resolve to get the absolute path!
cwd_abspath = cwd_path.resolve()
print("Absolute CWD:", cwd_abspath)

```

### Path attributes

The following examples show how pathlib makes it easier to extract specific attributes of a path.

#### Example: absolute path to the current file

```python
# Note: __file__ is a global python variable
this_file_path = pathlib.Path(__file__)
print("Path to file:", this_file_path)
```

#### Example: get the file name

```python
print("File name:", this_file_path.name)
```

#### Example: get the file name without extension (aka the stem)

```python
print("File stem:", this_file_path.stem)
```

#### Example: get the parent directory

```python
print("Parent folder:", this_file_path.parent)
```

To see all the options (there are many!) use `help(pathlib.Path)` or see the [pathlib-docs](https://docs.python.org/3/library/pathlib.html).

### Path composition

pathlib helps with traversing the directory tree.

- Slashes join elements of a path.

```python
path1 = pathlib.Path("parent")
print("Path 1:", path1.resolve())

path2 = pathlib.Path("child")
print("Path 2:", path2.resolve())

path3 = path1 / path2
print("Path 3:", path3.resolve())
```

- `..` indicates the parent directory

```python
path4 = path1 / path2 / pathlib.Path("..")
print("Path 4:", path4.resolve())  # This should be the same as path1
```

Only the first element needs to be a path - the rest can be strings!

```python
path1 = pathlib.Path("parent")
print("Path 1:", path1.resolve())

path2 = path1 / "child"
print("Path 2:", path2.resolve())

path3 = path2 / ".."
print("Path 3:", path3.resolve())  # This should be the same as path1
```

### Reading a file

The `open` method on the `Path` object can be used to access a file.

```python
file_path = pathlib.Path("..") / "data" / "example.txt"

with file_path.open("r") as file:
    content = file.read()
    print(content)
```

### Example: load data into pandas DataFrame

pathlib Paths are accepted by most pandas methods for reading data. This example shows how to do this for a real RAP project:

```python
import pandas as pd
import pyreadstat  # needed to parse sav files in spss
import pathlib2  # This is just a backwards compatible pathlib!

# https://realpython.com/python-pathlib/

# Add parameters
BASE_DIR = pathlib2.Path(r"\\<path>\Publication\RAP")
PUPIL_DIR = BASE_DIR / "Inputs" / "PupilData"
PUPIL_FILE = "SDD2018 - Stage 14 - 290519.sav"
PUPIL_DATA_PATH = PUPIL_DIR / PUPIL_FILE

pupil_data = pd.read_spss(PUPIL_DATA_PATH)
```

## External references

- [pathlib-docs](https://docs.python.org/3/library/pathlib.html)
