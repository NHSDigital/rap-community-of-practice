---
title: Basic Python Data Analysis operations

tags: 
  - Python
  - Data analysis
  - Pandas
  - Numpy
---

#

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
```

### Extracting the required columns

To select a column:

```py

```

### Filter where a variable is not null/missing

To filter rows based on some specific criteria:

```py
```

### Joins

```py

```

### Add a new column

```py
```

### Sorting variables

```py


```

### Transposing columns

There's a few ways to transpose columns:

```py


```

To set the name of the axis for the index or columns you can use `rename_axis()`:

```py
df = df.stack().rename_axis().reset_index()
```

### Grouping by variables

```py

# list of columns to group by
grouped = ["column 1", "column 2", "column 3", ...]]

```

### Aggregations

Once we've done the groupings above, add the aggregations:

```py
new_df = df.groupby(grouped).agg(total_sum=("column to be summarised", "sum"), total_count=("column to be counted", "count")).reset_index()
```

### Creating totals per row and per column

```py
df.loc["Column Total"] = df.sum(numeric_only=True, axis=0)

df.loc[:, "Row Total"] = df.sum(numeric_only=True, axis=1)
```

### Appending totals to a table

When creating different aggregations/groupings which are saved in different dataframes, you can then combine these aggregations into one table. For example, suppose you have calculated the totals for age and gender in different dataframes and you wish to append these results to the final output dataframe.

```py


```

### Creating derivations

To create a derivation based on the equivalent CASE WHEN SQL operation, there are several ways to do this in python:

```py
df.loc[df["age"] < 0, "age11_15"] = df["age"]
df.loc[(df["age"] > 0) & (df["age"] < 11), "age11_15"] = 11
df.loc[(df["age"] > 10) & (df["age"] < 16), "age11_15"] = df["age"]
df.loc[df["age"] > 14, "age11_15"] = 15
```

This results in creating a new column "age11_15" in the existing dataframe, based on the CASE WHEN conditions we applied for the new derivation.

```py
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

```

In the first bracket you assign the "WHEN" part of the condition, second bracket the "THEN", and "default=..." represents the "ELSE" part.

The NumPy option is faster and more efficient whereas Pandas is user friendlier and straightforward in its application. For datasets with only thousands of rows, whichever option you apply won't make a difference.

### Apply a column order

```py

```

### Exporting the output

```py


    df1.to_excel(writer, sheet_name="Sheet_name_1")
    df2.to_excel(writer, sheet_name="Sheet_name_2")
```

To check the parameters which can be adjusted for each file export, the pandas documentation provides useful resources. [pandas.DataFrame.to_excel()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) for example.

## Further reading

- [pandas documentation](https://pandas.pydata.org/docs/index.html)
- [NumPy documentation](https://numpy.org/doc/)
- [PEP-8 Python style guide](https://www.python.org/dev/peps/pep-0008/)
