# Back testing

## What is back testing and why do I care? <a name="what"></a>

Now that you are writing code in a reproducible manner, and perhaps using Python instead of another language, it is important that the code still produces the same results as the old code. Mistakes can easily be made in translating from one code base to another.

By following the steps in this guide, we can create a set of tests which will check that the outputs of the new code match the outputs of the old code.

First, we need the output from the old code in a CSV, to compare to the CSV which is produced by the new code. This should match the format of the new version, i.e. [tidy data][1]. So you'll need to translate the output of your old code into tidy data format. You can do this by manipulating the output manually (e.g. in Excel), you don't need to waste time modifying your old code base.

## Comparing CSVs

Create a file in your tests folder called `test_compare_results.py`.

In this file, we will write a set of functions which compare the old CSV to the new CSV. These comparisons are easy if we read the CSV files as Pandas Dataframes using `pd.read_csv`:

```Python
import pandas as pd
import pathlib2

TARGET_DIR = pathlib2.Path(<path>)
GTRUTH_DIR = pathlib2.Path(<path>)
target_df = pd.read_csv(TARGET_DIR / 'target.csv')
gtruth_df = pd.read_csv(GTRUTH_DIR / 'gtruth.csv')
```

Pandas Dataframes have some inbuilt attributes which we can now compare. For example, to check that they have the same number of rows and columns, we use `.shape`:

```Python
assert target_df.shape == gtruth_df.shape, 'Target has a different number of rows and/or columns to ground truth'
```

The assert function runs the condition `target_df.shape == gtruth_df.shape`. It does nothing if the condition is True, but raises an assertion error if the condition is False. We can decide what to write as a helpful error message, in this case: `'Target has a different number of rows and/or columns to ground truth'`.

Find out more about Python assert [here](https://www.w3schools.com/python/ref_keyword_assert.asp).

We can write more tests to run various comparisons of the two CSVs, e.g.:

- Check that they have the same column names in the same order:

```python
assert target_df.columns.tolist() == gtruth_df.columns.tolist()
```

- Finally, check the contents of each column are the same.

```Python
for each_col in gtruth_df.columns:
    assert (gtruth_df[each_col].equals(target_df[each_col]))
```

You may think of other tests appropriate to your project.

Now, save your new script, and from the command line, simply type `python test_compare_results.py` to run the script. If any of the tests have failed the error message we composed will be shown.

### Comparing Multiple CSVs

Your code may have multiple outputs which you want to compare to ground truth files.
Here's one way to do it, by iterating through a list of the pairs of CSVs.

```python

files_to_compare = [('target1.csv', 'gtruth1.csv'),
                    ('target2.csv', 'gtruth2.csv'),
                    ('target3.csv', 'gtruth3.csv')]

for (target_filename, gtruth_filename) in files_to_compare:
    target_df = pd.read_csv(TARGET_DIR / target_filename)
    gtruth_df = pd.read_csv(GTRUTH_DIR / gtruth_filename)

    assert target_df.shape == gtruth_df.shape, 'Target has a different number of rows and/or columns to ground truth'

    assert target_df.columns.tolist() == gtruth_df.columns.tolist(), 'Target has different column names to ground truth'

    for each_col in gtruth_df.columns:
        assert (gtruth_df[each_col].equals(target_df[each_col])), 'The contents of the columns are different'
```

## External links

- [Python assert](https://www.w3schools.com/python/ref_keyword_assert.asp)

[1]: ../../implementing_RAP/tidy-data.md
