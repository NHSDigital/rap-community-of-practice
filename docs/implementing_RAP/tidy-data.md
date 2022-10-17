# Tidy Data

Adopting inconsistent data formats leads to a huge amount of wasted effort and can actually lead to very complex code. By adopting **tidy data format** for your work you can both improve your service to users and simplify your own production pipeline.

## Reference for this guide

[Hadley Wickham's original paper on tidy format (pdf)](https://vita.had.co.nz/papers/tidy-data.pdf)

## Tidy data: Why should I care?

> "Tidy datasets are all alike but every messy dataset is messy in its own way" - Hadley Wickham

Teams spend a huge amount of effort reshaping and organising data to meet different needs. Tidy data is an attempt to align on a consistent shape for data that can meet most analytical use cases.

By doing as much intermediate data processing as possible in tidy format, you can often achieve huge improvements in code complexity and difficulty of maintaining code.

Note that adopting tidy data for stats production does not mean that your outputs need to be formatted this way. In fact, it is straightforward to get from a consistent tidy format to any unique format you require.

A common bad practice in stats production is to combine data production and data formatting in the same steps. Teams will calculate statistics and at the same time organise that data to match an excel table. This is a natural thing to do as you write code with your output table in mind but this approach leads to multiple problems:

- Code often gets repeated for different tables - increasing the burden of updating the code each year and increasing the likelihood of errors.
- Code is messy and difficult to maintain. Code should do one thing only - either produce the data or format the data.
- Once the data has been formatted it becomes less useful for other analysts since it is not machine readable. Before another team can use the data, they need to reformat it.

Tidy data offers a consistent format for data analysis purposes that is easy for analysts to produce, easy for humans to interpret, and easy for statistical tools like python and R to read. Tidy data offers more flexibility for readability and simplicity for data analysis purposes, as opposed to 'messy' or non-tidy data that can be have its own structure and rules. Tidy data involves "structuring datasets to facilitate analysis."

Having a consistent way of storing data, like in the tidy format, allows for analysts to easily use the same tools of analysis in a universal way, for example R or Python. Then, time is spent on producing all kinds of published outputs from the tidy structure, other pieces of analysis and data visualisation outputs such as dashboards.

An example of how tidy data enables analysts is that keeping this consistent form of storing data allows analysts to apply longitudinal methods to large datasets that hold years worth of data, critical for healthcare analytics and research.

## What is tidy data

- [See Hadley Wickham's excellent book for a great explanation](https://r4ds.had.co.nz/tidy-data.html)

It can be confusing in a large dataset which data is an observation (e.g. all measurements for a specific patient across all attributes) and which data is a variable (i.e. the values for a specific type of attribute so the treatment type or the results of a treatment).

There are several conventions on how a tidy dataset is structured but the most common one follows Codd's 3rd normal form (Codd, 1990):

- Each variable forms a column
- Each observation forms a row
- Each type of observational unit forms a table

Example of tidying up your data

A 'messy' or non-tidy dataset displaying results to treatments applied to patients:

| Patient_ID | Treatment A | Treatment B |
| ---------- | ----------- | ----------- |
| 1          | N/A         | 3           |
| 2          | 11          | 5           |
| 3          | 9           | 12          |

The same data but in a tidy format:

| Patient_ID | Treatment | Measured_Variable |
| ---------- | --------- | ----------------- |
| 1          | a         | N/A               |
| 2          | a         | 11                |
| 3          | a         | 9                 |
| 1          | b         | 3                 |
| 2          | b         | 5                 |
| 3          | b         | 12                |

Notice how on this table:

- Each measured variable (i.e. Treatment, Measured Variable) has its own column.
- Each observation/measurement forms a row.
- The treatment variable observations form a table of their own, ordering the dataset in a way that connects to the next subtable (i.e. Treatment b).

## How to tidy your data

It's easy to imagine tidy data with a small scale dataset however with real world data things can be trickier. Tidy data follow a similar structure but messy data are unique in their own 'messiness'.

In the subsection above, an example of a messy dataset was transformed to a tidy format. Messy data will rarely be that simple and obviously structured in several different ways, depending on what the data is measuring. This subsection will cover the most common issues with messy data and how to apply the tidy format for each example:

**_Note:_**
_It's perfectly valid and understandable to have your own structured way of presenting data in your published outputs, like in the table below (Occupation and Salaries). You should only format your data like this as a final output step - after producing your data in tidy format. Tidy data focuses not so much on the data formatting perspective but on the data production side, as tidy data enables the analyst to focus on analytical questions and not on data processing._

!!! Info "Internal to NHS Digital"

    How to transform your tidy data into a publication style output example: **From tidy to publication output**.

    This video can be found internal to NHS Digital within the RAP community of practice MS Teams page under:

    Files > COP video tutorials > From tidy data to publication

### 1. BAD: Column headers as values, not as names

Using values instead of names as a column header is a quite common form of messy data, however it can be useful for specific cases and computations. In the table below, is an example of various occupations and number of people for each occupation and salary:

| Occupation   | <£20k | £21k-£30k | £31k - £40k | £41k - £50k | £50k + |
| ------------ | ----- | --------- | ----------- | ----------- | ------ |
| IT           | 20    | 30        | 60          | 40          | 20     |
| Teacher      | 30    | 40        | 50          | 40          | 35     |
| Doctor       | 20    | 40        | 50          | 25          | 40     |
| Software Dev | 10    | 10        | 25          | 25          | 55     |
| Solicitor    | 25    | 25        | 60          | 30          | 50     |

In order to transform the table above into a tidier format, the columns are transformed into rows and into 2 columns/variables, one for income and one for number of people (example showing first rows for IT):

| Occupation | Income      | Count |
| ---------- | ----------- | ----- |
| IT         | <£20k       | 20    |
| IT         | £21k - £30k | 30    |
| IT         | £31k - £40k | 60    |
| IT         | £41k - £50k | 40    |
| IT         | £50k +      | 20    |
| Teacher    | ...         | ...   |

You can see that the data goes from wide to long.

### 2. BAD: Multiple variables stored in one column

Sometimes a dataset can contain columns which are comprised of multiple underlying variables. In the example table below, data shows an imaginary count of patients in hospitals per region, grouped by gender and age, combined in one column. So for example, m1930 stands for male patients aged 19 to 30 years old.

| Region                   | Year | m018 | m1930 | m3145 | m4665 | m6680 | m81o | f018 | f1930 |
| ------------------------ | ---- | ---- | ----- | ----- | ----- | ----- | ---- | ---- | ----- |
| West Midlands            | 2010 | 2    | 5     | 15    | 20    | 25    | 20   | 4    | 6     |
| London                   | 2010 | 5    | 10    | 15    | 20    | 25    | 40   | 5    | 10    |
| Yorkshire and the Humber | 2010 | 3    | 9     | 8     | 4     | 20    | 23   | 3    | 9     |
| North West               | 2010 | 5    | 10    | 15    | 12    | 17    | 15   | 2    | 8     |

To break apart these columns, different approaches of processing can be used, depending on the column header such as breaking apart the string or if there are separators in the column name (e.g. \_ or - or ;), capitals or any type of expression. The results of processing is show below, where the combined column of age and gender has broken into 2 separate variables and adding an extra column for the count of patients (first rows of West Midlands region):

| Region        | Year | Gender | Age     | Cases |
| ------------- | ---- | ------ | ------- | ----- |
| West Midlands | 2000 | m      | 0 - 18  | 2     |
| West Midlands | 2000 | m      | 19 - 30 | 5     |
| West Midlands | 2000 | m      | 31 - 45 | 15    |
| West Midlands | 2000 | m      | 46 - 65 | 20    |
| West Midlands | 2000 | m      | 66 - 80 | 25    |
| West Midlands | 2000 | m      | 81 +    | 20    |
| West Midlands | 2000 | f      | 0 - 18  | 4     |
| West Midlands | 2000 | f      | 19 - 30 | 6     |

### 3. BAD: Variables stored in both rows and columns

The next example can be confusing to tidy, as variables are stored in both rows and columns, so Weather station, Year, Month across Day1, Day2 columns and so forth, and tempmax/tempmin (Element column) stored in rows:

| Weather station | Date | Month | Element | Day1 | Day2 | Day3... |
| --------------- | ---- | ----- | ------- | ---- | ---- | ------- |
| LS123           | 2018 | 1     | tempmax | 29   | -    | -       |
| LS123           | 2018 | 1     | tempmin | 10   | -    | -       |
| LS123           | 2018 | 2     | tempmax | -    | 28   | 25      |
| LS123           | 2018 | 2     | tempmin | -    | 13   | 13      |
| LS123           | 2018 | 3     | tempmax | 30   | -    | -       |
| LS123           | 2018 | 3     | tempmin | 18   | -    | -       |
| LS123           | 2018 | 4...  | tempmax | -    | -    | -       |

To tidy this, a new column Date needs to be extracted from Year, Month and Day to correspond to each day of observation. Then variables minimum and maximum Temperatures for each date will be stored in two different columns:

| Weather station | Date       | tempmin | tempmax |
| --------------- | ---------- | ------- | ------- |
| LS123           | 2018-01-01 | 10      | 23      |
| LS123           | 2018-02-02 | 13      | 24      |
| LS123           | 2018-02-03 | 13      | 25      |
| LS123           | 2018-03-01 | 18      | 26      |
| LS123           | 2018-04-24 | 17      | 27      |
| LS123           | 2018-05-12 | 19      | 29      |

This table is in a tidy format, there is one row for one day's observations and two new columns, one for each variable of the column Element.

### 4. BAD: Multiple types of observations in one table

The next example is subset of data from the top Billboard songs for each year. This data is not in a tidy format. Weeks 4 - 75 have been edited out for readability purposes. Here, there are several variables, Artist, Song Title, Duration, Date Entered, Week and Rank. (as both are the same for each week the song spent in the billboard.)

| Year | Artist              | Song Title              | Duration | Date Entered | Week1 | Week2 | Week3 |
| ---- | ------------------- | ----------------------- | -------- | ------------ | ----- | ----- | ----- |
| 1966 | The Beatles         | We Can Work It Out      | 3:00     | 1966-01-08   | 5     | 2     | 1     |
| 1966 | The Beatles         | Paperback Writer        | 3:30     | 1966-06-25   | 6     | 3     | 1     |
| 1966 | The Beach Boys      | Good Vibrations         | 3:00     | 1966-12-10   | 7     | 4     | 2     |
| 1966 | The Lovin' Spoonful | Summer in the City      | 3:20     | 1966-08-13   | 3     | 2     | 1     |
| 1966 | Four Tops           | Reach Out I'll Be There | 3:10     | 1966-10-15   | 9     | 3     | 2     |

Transforming this dataset into a tidy version would cause unnecessary duplication of observations (thus cancelling the 1 observation per row norm), in the table below. Imagine if Weeks 4-75 were not removed, so then we would have 72 rows of repeating the same Artist, Song Title and Duration variables. Date Entered has be edited to include the starting week of every week on the billboard:

| Year | Artist              | Song Title         | Duration | Date Entered | Week | Rank |
| ---- | ------------------- | ------------------ | -------- | ------------ | ---- | ---- |
| 1966 | The Beach Boys      | Good Vibrations    | 3:00     | 1966-12-10   | 1    | 7    |
| 1966 | The Beach Boys      | Good Vibrations    | 3:00     | 1966-12-17   | 2    | 4    |
| 1966 | The Beach Boys      | Good Vibrations    | 3:00     | 1966-12-24   | 3    | 2    |
| 1966 | The Lovin' Spoonful | Summer in the City | 3:20     | 1966-08-13   | 1    | 3    |
| 1966 | The Lovin' Spoonful | Summer in the City | 3:20     | 1966-08-20   | 2    | 2    |
| 1966 | The Lovin' Spoonful | Summer in the City | 3:20     | 1966-08-27   | 3    | 1    |

In this instance, it is recommended that the tidy dataset is split into two, one for each observational unit, the song title and the rank of the song:

**Table 1**

| ID  | Artist              | Song Title              | Duration |
| --- | ------------------- | ----------------------- | -------- |
| 1   | The Beatles         | We Can Work It Out      | 3:00     |
| 2   | The Beatles         | Paperback Writer        | 3:30     |
| 3   | The Beach Boys      | Good Vibrations         | 3:00     |
| 4   | The Lovin' Spoonful | Summer in the City      | 3:20     |
| 5   | Four Tops           | Reach Out I'll Be There | 3:10     |

**Table 2**

| ID  | Date Entered | Rank |
| --- | ------------ | ---- |
| 3   | 1966-12-10   | 7    |
| 3   | 1966-12-17   | 4    |
| 3   | 1966-12-24   | 2    |
| 4   | 1966-08-13   | 3    |
| 4   | 1966-08-20   | 2    |
| 4   | 1966-08-27   | 1    |

This approach is useful for tidy data buts lacks in data processing tools' capabilities, so in that case these tables will have to be merged again.

### 5. One type of observational unit in multiple tables

There are datasets that have multiple tables and variables and observational units that are spread throughout those tables. Or these tables change frequently over time. Or there are different approaches to data types, missing data, data formats for each of those tables.

In these cases, it is recommended that each table is 'tidied' up, and then combine each tidy table. To avoid any potential data duplication, adding an extra IDcolumn in each table as well as a column that records the original table/file's name will ensure that each row of data in the merged tidy table is labelled with its source table/file.

## Diabetes tidy data example

!!! Info "Internal to NHS Digital"

    This video can be found internal to NHS Digital within the RAP community of practice MS Teams page under:

    Files > COP video tutorials > Diabetes tidy example

In this video:

- SQL vs PySpark outputs comparison (messy vs tidy data)
- Data shown in suppressed/published form and dummy data
