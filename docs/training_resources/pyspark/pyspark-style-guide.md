---
title: PySpark style guide

tags: 
  - PySpark
  - Spark
  - Coding tips
  - Code style
  - SQL

hide:
  - toc
---

#

## Introduction

We tend to use PySpark interleaved with python. That means we follow standard Python organisation of modules, functions, tests, etc., but where we do data manipulation we drop to PySpark.

PySpark gives you many ways to accomplish operations. We do not lay out all of the different options here because it would be confusing. Instead, these examples give you the single approach that we have chosen to use. it is perfectly valid for you to choose a different way.

We avoid using pandas or koalas because it adds another layer of learning. The PySpark method chaining syntax is easy to learn, easy to read, and will be familiar for anyone who has used SQL.

There does not yet seem to be a style convention for PySpark so we have adapted [this style guide](https://github.com/palantir/pyspark-style-guide).

You can also find a tutorial script containing lots of code snippets here.

## In-built PySpark functions

Using functions is preferred to writing spark SQL to support testing and encapsulation. This preference is not a rule.

PySpark makes a lot of use of functions imported from spark.sql.functions library. Almost any function that you might find in SQL should be available in this library. The [docs contain the full list of functions](https://spark.apache.org/docs/latest/api/sql/index.html).

Our convention is to import these all under F:

```python
from pyspark.sql import functions as F
```

Then you would use the functions like:

```python
F.col()

F.max()

F.datediff()
```

### Reading a table

To get started we will usually want to read a table from a database into a DataFrame.

```python
df = spark.table('my_database.my_table')
```

### Select

The Spark equivalent of SQL's SELECT is the `.select()` method. This method takes multiple arguments - one for each column you want to select. These arguments can either be the column name as a string (one for each column) or a column object (using the df.colName syntax). If you are using Spark version before 3.0 then do this:

```python
df = (
    df.select(F.col(‘AGE’), F.col(‘CHOLESTEROL’))
)
```

Notice the indentation of the parentheses is different from python. This is following the palantir style guide listed above. This convention become more valuable when we see longer examples.

### Casting data types

Spark differs from SQL in that it is 'schema-on-read'. This means that when you import data into PySpark, it will try to guess the datatypes of your columns unless you explicitly provide a schema.

In general, it is good practice to set the data types as soon as you read in data.

In our approach, we use the initial `.select()` statement to (1) rename columns to follow our naming convention and (2) cast data types where necessary. This ensures everything is tidy before we start complex operations.

```python
my_df = (
    my_df.select(
        F.col("NHS_NUMBER").cast("String").alias("NHS_NUMBER"),
        F.col("BirthDate").cast("Date").alias("BIRTH_DATE"),
        F.col("Appointments_count").cast("Integer").alias("APPOINTMENTS_COUNT")
        )
)

```

### Filter

The `.filter()` method is the Spark counterpart of SQL's WHERE clause.:

```python
my_df = (
    my_df.filter(F.col(‘MY_VALUE’) >= 4)
)
```

### Renaming columns

Changing a column name is simple:

```python
df = (
    df.withColumnRenamed(‘old name’, ‘NEW_NAME’)
)
```

For example:

```python
diabetes_data = (
    diabetes_data.withColumnRenamed(‘Birth_date’, ‘BIRTH_DATE’)
)
```

### Aggregations

The syntax for aggregation is very similar to SQL, but with a different order:

```python
df = (
    df
    .groupby(F.col(‘YEAR’))
    .agg(
        F.sum(F.col(‘SALES’)).alias(‘TOTAL_SALES’),
        F.min(F.col('SALES')).alias('MIN_SALES'),
        F.max(F.col('SALES')).alias('MAX_SALES')
        )
)
```

Note how alias() is used to rename the aggregations.

### Method chaining

Method chaining is one of the nicest features of PySpark as it allows you to do one operation after another in a very readable manner.

You have already seen lots of examples of method chaining in this guide but here we address it directly.

Here is an example that contains many of the operations you might want to perform on a dataset:

```python
df2 = (
    df1
    .select(F.col(‘FIELD_ONE’), F.col(‘FIELD_TWO’))
    .filter(F.col('FIELD_TWO') > 10)
    .agg()
)
```

Notice that we have put parentheses '()' around the entire query and we put the '.' at the beginning of each new line

This approach contrasts to using the other common approach of having backslashes in the code. E.g. **(DON’T DO THIS)**

```python
df2 = df1 \
    .select(‘FIELD_ONE’, ‘FIELD_TWO’) \
    .filter(‘FIELD_TWO > 10) \
    .agg()

```

It is recommended the chain lines to be no more than 6-7 lines. Try to avoid long chains and opt to break the code into logical steps.

### Joins in PySpark

You should **always explicitly specify the type of join** in PySpark. If you do not specify the type of join in PySpark then it will default to inner join. Explicit is better than implicit. Even if the aim is to do an inner join, always specify the ‘how’ part of the join:

Here is an example of good practice where we specify a left join:

```python
df_3 = (
    df_1
    .join(df_2, on=’NHS_NUMBER’, how=’left’)
    .select(df_1[*], df_2['FIELD_1', 'FIELD_2'])
)
```

Notice above how the joining field ‘on’ condition is also specified. In situations where you need to join on multiple fields do this:

```python
df_3 = (
    df_1
        .join(df_2,
            (df_1.NHS_NUMBER == df_2.NHS_NUMBER) &
            (df_1.CCG == df_2.CCG),
            how=’left’)
        .select(df_1[*], df_2['FIELD_1', 'FIELD_2'])
)
```

In the example above, the single joining field ‘on’ condition has been replaced with the multiple joining field conditions.

### Add a new column: `.withColumn()`

To simply add a new column to your dataset:

```python
df = df.withColumn("MyNewColumnName", <insert your conditions here>)
```

Suppose you want to add a new flag to your data (Yes = 1, No = 0), when a patient has had a chest x-ray or not:

```python
df = (
    df
    .withColumn("X-RAY_FLAG", F.when(F.col("X-RAY_DATE").isnotNull(), 1)
    .otherwise(0))
)
```

This will result to an extra column in the dataset that contains the flag values we just assigned with the (case) F.when condition.

### Adding values to new columns

If you want to create an empty column never use ‘NA’ or a blank string ‘ ‘ to fill in the rows of said column. Instead use None:

```python
df = df.withColumn(‘MyEmptyColumnName’, F.lit(None))
```

Or, here's an example where two new columns are created with the constant values of 1 and 2 in each column respectively.

```python
df = (
    df
    .withColumn(‘MyColumnName1’, F.lit(1))
    .withColumn('MyColumnName2', F.lit(2))
)
```

### PySpark inside a Python function

We can create functions like in python, same logic applies, but instead using PySpark style:

```python
def group_by_and_count_column(data: df, column_name: str):
    “”
    Groups by specified column and returns count per grouping and sorts by descending order.

    Args: dataset we are reading from & the column we wish to group by

    Returns: groups from column and count
    “””


    return result
```

### Reordering columns using a list

To reorder columns in a table, create a list of the columns in the order you wish them to be:

```python
columns_order = ["NHS_NUMBER", "CCG", "APPOINTMENT", "APPOINTMENT_DATE", etc]
```

And then apply to the dataframe:

```python
new_df = (
    old_df.select(*columns_order)
)
```

The asterisk is required to unpack the list in the select statement.

### Operations across multiple columns using a list

Suppose you have flag columns in your dataset, whether a patient has attended an appointment or not, or a patient has completed a course of treatment. You can sum each of the flags on a record level by using a list and by adding an extra column using `.withColumn()` to the dataset with the sum result for each record:

```python
flags_sum = ["APP_ATTENDED", "TREATMENT_COMPLETE"]
```

After creating the list of flags we can now proceed to the final step:

```python
new_df = (
    old_df
        .withColumn("PATIENT_SCORE", sum(old_df[item] for item in flags_sum))
)
```

Now you have a new column called PATIENT_SCORE that contains the sum of the specified flags for each Patient/row of data.

### Passing in column definitions to `.withColumn()`

To add derivations and fields definitions to the final processing table, simply follow the `.withColumn()` logic as before:

```python
final_table = (
    previous_step_df
        .withColumn("SMOKING_NUMERATOR", smoking_numerator)
        .withColumn("TOTAL_NUM_PATIENTS", sum_of_patients)
        .etc
)
```

The 2nd argument of `.withColumn()` is a variable created at a separate step in the workflow, for example:

```python
smoking_numerator = (
    F.when((F.col("SMOKING_VALUE") >= 5) & (F.col("AGE") >= 18), 1).otherwise(0)
)
```

The above field definition is an application of a SQL-like `CASE WHEN` in PySpark.

Field definitions can be complex, with a lot of condition statements and potential dependencies. To learn more about structuring your code and creating field definitions:

- [To learn more about field definitions and how to use them][1]

### Using these field definitions to write test cases with customers

Once you've written your field definitions, next step is to write the unit tests to ensure that the definitions work as intended and are future-proof to bugs and errors:

- [Writing unit tests for field definitions][2]

### Passing in a list of aggregations to apply

To pass a list of aggregations, as in the previous examples, create a variable that contains the specified aggregations:

```python
aggregate_fields = (
    F.sum("REGISTRATIONS").alias("TOTAL_REGISTRATIONS"),
    F.count("NHS_NUMBER").alias("ALL_PATIENTS"),
    F.round(F.sum("REGISTRATIONS") * 100 /F.count("NHS_NUMBER"), 2).alias("REGISTRATIONS_PERCENTAGE"),
)
```

Then apply to the final table to produce the aggregated output:

```python
aggregated_output = (
    final_table
    .agg(*aggregate_fields)
    .<apply other conditions here, i.e. adding new columns or sorting the column order>
)
```

Print the output `aggregated_output.show()`

### Create your own schema

If you wish to create your own custom schema, here's how to do it:

```python
schema = StructType([
      StructField("id",IntegerType(),True),
      StructField("colour",StringType(),True),
      StructField("rate",FloatType(),True),
      StructField("date",DateType(),True)
    ])
```

## Performance - caching and lazy operations

Lazy evaluation in Spark means that the execution will not start until an action is triggered. When we call for an operation to execute, it does not execute immediately. Spark maintains the record of which operation is being called.

## General tips and tricks

1. Try to keep your code in logical structured blocks. For example, if you have multiple lines referencing the same things, try to keep them together. Separating them reduces context and readability.
2. Try to be as explicit and descriptive as possible when naming functions or variables. Strive to capture what the function is actually doing as opposed to naming it based the objects used inside of it.
3. Think twice about introducing new import aliases, unless there is a good reason to do so. Some of the established ones are types and functions from PySpark from pyspark.sql import types as T, functions as F.
4. Avoid using literal strings or integers in filtering conditions, new values of columns etc. Instead, to capture their meaning, extract them into variables, constants, dicts or classes as suitable. This makes the code more readable and enforces consistency across the repository.

## External links

[GSS introduction to PySpark](https://gss.civilservice.gov.uk/training/introduction-to-pyspark)

[Palantir PySpark style guide](https://github.com/palantir/pyspark-style-guide)

[1]: ../python/unit-testing-field-definitions.md
[2]: ../python/unit-testing-field-definitions.md#testing-field-definitions
