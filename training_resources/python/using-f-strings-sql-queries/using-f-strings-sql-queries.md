---
title: Using Python f-strings to run SQL queries

tags: 
  - Python
  - SQL
  - Pandas
---

#

!!! tip "TLDR"
    - [Python can be used to run SQL strings](#parametrising-sql-queries-using-python-f-strings), and they can be parametrised using [f-strings](#option) to make "dynamic SQL"
    - You can load SQL files with Python, then [run them](#option-2-sql-query-read-from-a-separate-sql-script).
    - You can have Python [run your SQL Stored Procedures](#executing-sql-server-stored-procedures-using-python)

??? question "Why should we care?"
    - If your analytical pipeline is already written in SQL, this allows you to get the benefits of Python, without having to rewrite all that SQL code.
    - Python can be used to help with parametrisation of your SQL code
    - You could use Python to load the data into the database, and then run your SQL script - no need for other tools.

??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[Are you ready for RAP?](../../implementing_RAP/rap-readiness.md)|Helpful|Doing some basic Python training will help you get the most out of this guide.|



In this guide we're going to take a look at what are f-strings in Python and how to use them in conjuction with SQL queries to import data from e.g. SQL Server and assign it to a `Pandas` dataframe.

## Why use f-strings?
F-strings were first introduced in [PEP-498](https://peps.python.org/pep-0498/) and has since taken the cake when it comes to formatting in Python. Key benefits are:

- They offer simple syntax
- They support arbitrary expressions
- Faster performance vs other formatting options such as `str.format()` and `%-formatting`.
- Support for multi-line formatting.

Example of f-strings:
```py
>>> name = "Maria"
>>> age = 39
>>> print(f"Hello, nice to meet you. My name is {name} and I'm {age} years old.")
`Hello, nice to meet you. My name is Maria and I'm 39 years old.`
```

## Parametrising SQL queries using Python f-strings
You can insert SQL script into the Python code, and use f-strings to pass in parameters. So for example you can parametrise the publication year and month and edit those parameters only when running your pipeline, reducing production burden and improving publication speed.

There are two ways to implement and read in data via SQL queries wrapped in f-strings, using `SQLAlchemy`.

### Option 1: SQL query within code (e.g. Python) script
First, we need to create our SQL query, or have our SQL query ready to go e.g.:
```sql
SELECT * FROM [{database}].[{table}]
                    WHERE [PUBLICATION_YEAR] = {year}
                    AND [SPECIAL_LABEL] = {code_value}
```
Second, we need to create a function that will read in a SQL query wrapped in f-strings, database and server information and create a `Pandas` dataframe:
```py
import sqlalchemy as sa # read in sqlalchemy package
import pandas as pd # read in pandas
import pyodbc # import odbc drivers for SQL

    """
    Use sqlalchemy to connect to the NHSD server and database with the help
    of mssql and pyodbc packages

    Inputs:
        server: server name
        database: database name
        query: string containing a sql query

    Output:
        pandas Dataframe
    """
    conn = sa.create_engine(f"mssql+pyodbc://{server}/{database}?driver=SQL+Server", fast_executemany=True)
    conn.execution_options(autocommit=True)
    df = pd.read_sql_query(query, conn)
    
    return df
```
After writing this function, we can now write our SQL query, wrap it in f-strings and save it to a variable. Example:
```py
def create_sql_query(database, table, year, code_value) -> str:
    """Creates a function to select the required fields for the benchmark tool data

    Inputs:
        database: database name as defined in config.toml file
        table: SQL table within database
        year: the chosen year of the publication
        code_value: special value for the purposes of the publication        
    Output:
        SQL query loaded up with parameters for the publication
    """

    query = f""" SELECT * FROM [{database}].[{table}]
                    WHERE [PUBLICATION_YEAR] = {year}
                    AND [SPECIAL_LABEL] = {code_value}
                    """
    return query
```
Notice how we inserted a standard SQL query into a Python f-string format and assigned it to the variable `query`. The when we call this function, all we need to do is insert the arguments for `database`, `table`, `year` and `code_value` and assign the result to a `variable`.
```py
```
Now that we have our query loaded up with our chosen parameters, we can go ahead and create our `Pandas` dataframe:
```py
publication_data = get_df_from_sql(sql_query_for_publication, "SERVER_ADDRESS_111", "NHS")
```
Now that we have the data imported, we can continue with the data processing.

### Option 2: SQL query read from a separate SQL script
Option 2 is similar to option 1 with a slight variation in where the SQL script is stored.

We create a separate file, a `my_sql_query.sql` script and place our SQL query from above within it:
```sql
SELECT * FROM [{database}].[{table}]
WHERE [PUBLICATION_YEAR] = {year}
AND [SPECIAL_LABEL] = {code_value}
```
We then need to read in the SQL query into our working Python script as it's stored in a separate file, contrary to the scenario we had in Option 1.
```py
def read_in_sql_query(sql_file_path: str, **sql_parameters) -> str:
    """Reads in a SQL query file with parameters and fills them with the values provided in the sql_parameters dictionary

    Inputs:
        sql_file_path: the path to the file with query 
        **sql_parameters: parameters and their values that are in the query 
    Output:
        SQL query loaded up with parameters for the publication
    """
    
    with open(sql_file_path,'r') as sql_file:
            sql_query = sql_file.read()
     
    new_sql_query = sql_query.format(**sql_parameters)

    return new_sql_query
```
We can call this function to create our query, from the `.sql` file:
```py

sql_query_for_publication = read_in_sql_file(sql_file_path, **sql_parameters)
```
We can reuse the get_df_from_sql() function from Option 1 to read in the data and create a `Pandas` dataframe:
```py
publication_data = get_df_from_sql(sql_query_for_publication, "SERVER_ADDRESS_111", "NHS")
```

## Write a dataframe to SQL Server database
If you have a dataframe ready to be written in a SQL Server table then you can use the following function:
```py
def write_df_to_server(server, database, df_to_write, table_name) -> None:
    """Writes a pandas DataFrame to a table on a given SQL server using SQL Alchemy.
       Requires mssql and pyodbc packages.

    Parameters:
        database: database name
        df_to_write: df to write to a SQL Server table
        table_name: SQL Server table name

    Returns
        Write to a SQL Server table.
    """
    
    conn = sa.create_engine(f"mssql+pyodbc:/{server}/{database}?driver=SQL+Server", fast_executemany=True)
    conn.execution_options(autocommit=True)
    df_to_write.to_sql(name=table_name, con=conn, if_exists='fail', index=False)
```

## Executing SQL Server stored procedures using Python
First, we create a stored procedure to use as an example:
```sql
CREATE PROCEDURE PatientsNHSERegion
@PatientID nvarchar(100), 
@NHSECode int
AS
BEGIN
    SELECT h.NHSE_code, 
           h.Patient_ID, 
           h.Other_ID 
    FROM hes.table as h 
    WHERE h.Patient_ID = @PatientID
    AND h.NHSE_code = @NHSECode; 
END; 
GO
```
### Option 1: via sqlalchemy
```py
import pandas as pd
import sqlalchemy as sa

query = 'EXEC my_procedure @PatientID:param1, @NHSECode:param2' # add parameters depending on your query
engine = sa.create_engine(f"mssql+pyodbc://{server}/{database}?driver=SQL+Server", fast_executemany=True)
df = pd.read_sql_query(query, engine, params=dict(param1='test2', param2='test3')) # this will store the results in a dataframe
```
### Option 2: via pyodbc
When run in SQL Server, the stored procedure above will produce an output containing results from the above query. To run this via Python, we need to write the following Python script:
```py
import pyodbc as po
 
database = ''
username = '' # username and password might not be required to connect
password = ''

    # Connection string
    cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
            server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()
 
    params = ("1234590", 5150)
 
 
    while row:
        row = cursor.fetchone()
 
    del cursor
 
 
except Exception as e:
    print("Error: %s" % e)
```
Python should successfully execute the SQL Server stored procedure with your parameters, this means the output normally displayed in SQL Server will be printed out in the programming tool used to execute the above Python script, congrats!

## Further resources and references
- [String formatting: Input and output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Executing SQL Server stored procedures via Python (citation for section above)](https://www.mytecbits.com/internet/python/execute-sql-server-stored-procedure)

