# Basic Python Data Analysis operations

## What is this guide about?

Python offers many ways to achieve multiple calculations, computations and operations. For data analysis and data science overall, [Pandas](https://pandas.pydata.org/) is the most commonly used package or library to perform these operations, along with [NumPy](https://numpy.org/).

## Reading in data

To get started with Pandas import:

```py
import pandas as pd
import numpy as np
```

### Loading data from a .csv file

df - dataframe

```py
df = pd.read_csv('your_file.csv')

# or if required to edit headers for example:

df = pd.read_csv('your_file.csv', header=..., na_values=..., sep=..., etc)
```

### Loading data from an Excel file .xlsx

```py
df = pd.read_excel('your_file.xlsx')
```

### Loading data from a SQL table/database

```py
import pyodbc
import pandas as pd


connection_object = pyodbc.connect("Driver={SQL Server};"
    "Server=xxxx;"
    "Database=xxxx;"
    "Trusted_Connection=yes;")

df = pd.read_sql(insert_your_sql_query, connection_object)
```

Add your Server address and Database name in the respective conditions above.

### Loading data from an SPSS file (.sav)

There are two way to import a .sav file. One way:

```py
import pandas as pd

df = pd.read_spss(file_path, convert_categoricals=False)
```

or

```py
import pyreadstat

df, metadata = pyreadstat.read_sav(file_path)
```

The second option creates the dataframe but also captures the metadata of the .sav file, which is useful when running data validation checks.

## Common Operations

There are many ways to perform various operations in Python, depending on the library you are using or the general approach and design you've opted to apply to your code. This guide presents several examples on how to perform common SAS operations using pandas, any suggestions or feedback is welcome.

### Cases

You will soon notice after importing your data from the .sav file that the column headers are not aligned consistently to upper case or lower case, but a mixture of this. To apply lower or upper case to all column headers:

```py
df.columns = df.columns.str.lower()
# or
df.columns = df.columns.str.upper()
```

### Extracting the required columns

To select a column:

```py
# columns to keep
to_keep = ["column 1", "column 2", "column 3", ...]

# create the new table
filtered_df = df[to_keep]
```

### Filter where a variable is not null/missing

To filter rows based on some specific criteria:

```py
# not null
new_df = df[df["my_column"].notnull()]
```

### Joins

```py
# a left join, one column to join on
joined_df = df.merge(other_df, how="left", on="my_column")

# inner join, on multiple columns
joined_df = df.merge(other_df, how="inner", on=["column 1", "column 2"])
```

### Add a new column

```py
# create new table with a new column that adds 5 to each value of another selected column
new_df = df.assign(new_column=df["my column"] + 5)
```

### Sorting variables

```py
# ascending order can be False or True
df.sort_values(by="my column", ascending=False)

# if you want to see missing values first, assign na_position
df.sort_values(by="my column", ascending=False, na_position="first")

# sort by multiple columns
df.sort_values(by=["my column 1", "my column 2", ...])
```

### Transposing columns

There's a few ways to transpose columns:

```py
# set the index of columns
df.set_index(["my column 1", "my column 2", "my column 3", ...], inplace=True)

# using pandas transpose to transpose rows with columns and vice versa
df_transposed = df.T

# using pandas stack() to transpose non-index columns into a single new column
df = df.stack().reset_index()
```

To set the name of the axis for the index or columns you can use `rename_axis()`:

```py
df = df.stack().rename_axis().reset_index()
```

### Grouping by variables

```py
# group by one column
new_df = df.groupby("my_column")

# group by multiple columns

# list of columns to group by
grouped = ["column 1", "column 2", "column 3", ...]]

# return new table with grouped columns
new_df = df.groupby(grouped)
```

### Aggregations

Once we've done the groupings above, add the aggregations:

```py
new_df = df.groupby(grouped).agg(total_sum=("column to be summarised", "sum"), total_count=("column to be counted", "count")).reset_index()
```

### Creating totals per row and per column

```py
# total per column, adds a new row "Column Total"
# this will sum all numeric row values for each column
df.loc["Column Total"] = df.sum(numeric_only=True, axis=0)

# total per row, creates a new column "Row Total"
# this will sum all numeric column values for each row
df.loc[:, "Row Total"] = df.sum(numeric_only=True, axis=1)
```

### Appending totals to a table

When creating different aggregations/groupings which are saved in different dataframes, you can then combine these aggregations into one table. For example, suppose you have calculated the totals for age and gender in different dataframes and you wish to append these results to the final output dataframe.

```py
# list the final output dataframe to store its aggregations
list_df = [df]

# append the calculated totals
list_df.append(calc_totals_df)

# concatenate into a single dataframe
output_df = pd.concat(list_df, axis=0)
```

### Creating derivations

To create a derivation based on the equivalent CASE WHEN SQL operation, there are several ways to do this in python:

```py
# pandas package CASE WHEN
# create the age 11 to 15 derivation
df.loc[df["age"] < 0, "age11_15"] = df["age"]
df.loc[(df["age"] > 0) & (df["age"] < 11), "age11_15"] = 11
df.loc[(df["age"] > 10) & (df["age"] < 16), "age11_15"] = df["age"]
df.loc[df["age"] > 14, "age11_15"] = 15
```

This results in creating a new column "age11_15" in the existing dataframe, based on the CASE WHEN conditions we applied for the new derivation.

```py
# NumPy package CASE WHEN
# create the age 11 to 15 derivation
age11_15 = np.select(
    [
     df['age'] == 10, # WHEN
     df['age'] > 15 # WHEN
     ],
    [
     11, # if age == 10 then assign 11
     15 # if age > 15 assign 15
     ],
    default=df['age'] # ELSE assign "age" column values
    )

# assign the result to a new column
df["age11_15"] = age11_15
```

In the first bracket you assign the "WHEN" part of the condition, second bracket the "THEN", and "default=..." represents the "ELSE" part.

The NumPy option is faster and more efficient whereas Pandas is user friendlier and straightforward in its application. For datasets with only thousands of rows, whichever option you apply won't make a difference.

### Apply a column order

```py
# create a list of the column headers in a specific order
column_order = ["column 1", "column 2", "column 3", ...]

# apply list to dataframe
df = df[column_order]
```

### Exporting the output

```py
# write output to a .csv
df.to_csv("output.csv", ... <multiple parameters that can be inserted>)

# write output to an excel workbook
df.to_excel("output.xlsx", sheet_name="Sheet_name_1", ... <multiple parameters that can be inserted>)

# write multiple sheets from different dataframes
with pd.ExcelWriter("output.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet_name_1")
    df2.to_excel(writer, sheet_name="Sheet_name_2")
```

To check the parameters which can be adjusted for each file export, the pandas documentation provides useful resources. [pandas.DataFrame.to_excel()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) for example.

## Further reading

- [pandas documentation](https://pandas.pydata.org/docs/index.html)
- [NumPy documentation](https://numpy.org/doc/)
- [PEP-8 Python style guide](https://www.python.org/dev/peps/pep-0008/)
