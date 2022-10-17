# Logging and error handling

Logging and error handling are two concepts that will improve the reliability and maintainability of your code. These big topics could each be given their own chapter but here we try to show how the combination of simple logging and simple error handling can be easy to implement while offering substantial benefits.

## What is logging?

Logging is a way to track events that occur when your code runs. The logs will show when different parts of your code was run and what the result was. For example, my `ingest_data.py` module ran at 08:44 on 2021-09-17 and found 3,452,521 rows of data.

You can think of logging as the next evolution of the `print` statement. When writing code interactively, we use print statements to understand what is happening at each step. By replacing these print statements with logs, we are able to permanently track what is happening in these interesting parts of the code.

Python’s standard library "[logging](https://docs.python.org/3/library/logging.html)" includes a flexible built-in logging module, allowing the developer to create different configurations to fulfil their logging needs. For example, the log can be categorised based on levels of severity and the users might select the destination (in console, files, remote server, or email).

## What is error handling?

Error handling provides a way for us to try to handle problems in our code in a constructive manner. Error handling works hand-in-hand with logging to improve code reliability.

When our code fails for some reason, we usually see an error message on screen and the running of the code stops. That error message is known as an exception. Exceptions are objects which represent errors which contain information about the kind of error and where it was caused.

As a developer, I can often anticipate what parts of my code are likely to have errors. For example, parsing a .csv file where we expect a certain list of column headers. By using error handling at these points in the code, I can make the code
[fail gracefully](https://stackoverflow.com/questions/497952/how-to-make-python-gracefully-fail) while writing an informative error message to my logs.

In this way we improve visibility of the functioning of our code. If the code runs every night at midnight but has failed last night, then our error handling and logging should tell me exactly what has gone wrong.

## Logging in Python

Python comes with a standard "[logging](https://docs.python.org/3/library/logging.html)" library that gives us the capabilities to:

- Diagnose an issue during development or debug bigger problem
- Track what is going on in the system for better monitoring
- Control what output is created and how it looks

You can read the official python [logging tutorial](https://docs.python.org/3/howto/logging.html) for instructions on how to customise and adapt the logger.

As a basic example - here is the code to set up a logger:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"./reports/logs/{time.strftime('%Y-%m-%d_%H-%M-%S')}.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
```

The `format` argument describes how we want our log to look. Here we include the time, the name of the file that is running, and a custom message that we will specify when we use the logger. The `handlers` argument sets up two outputs for the log - one copy of the log info will be written to a file (the FileHandler) and another copy will be printed on screen (just like a print statement).

We can then use the logger to keep track of what is happening in the code by passing in informative messages:

```python
 logger.info("Step 1: Import all the input data from MSSQL database")
```

The resulting logs might look something like this:

```
2021-08-02 15:43:13 - __main__ - INFO - Step 1: Import all the input data from MSSQL database
2021-08-02 15:43:14 - diabetes.utilities.processing_steps - INFO - Read and prepare input data
2021-08-02 15:43:15 - diabetes.utilities.data_connections - INFO - Loading 100 rows from dev.NDA_DEMO_E3_202021...
2021-08-02 15:43:16 - diabetes.utilities.data_connections - INFO - Loading 100 rows from dev.NDA_BMI_E3_202021_...
```

You can see that the information we described in the `format` argument is captured here. We could go further and include additional useful info:

- Filename where the log was triggered (`filename`)
- Function name where the log was triggered (`funcName`)
- Line number where the log was triggered (`lineno`)
- Process ID of the process where the log happened (`processName`)

You can find a full list of things to add in the [docs](https://docs.python.org/3/library/logging.html#formatter-objects).

### Video tutorial: Logging demo

!!! Info "Internal to NHS Digital"

    This video can be found internal to NHS Digital within the RAP community of practice MS Teams page under:

    Files > COP video tutorials > Error Handling

## Error handling in Python

Error handling using try/except is useful and powerful. When python hits an error, it produces something called an exception. An exception is an object that tries can tell you something about what has gone wrong. There are many different types of exceptions - see the full list [here](https://www.tutorialsteacher.com/python/error-types-in-python).

To get started with error handling however, the simplest way is to start with a block of code like below:

```python
input = 'some text'
try:
    int(input)
    logger.info('input converted to integer')
except ValueError as e:
    logger.exception(f'Could not convert {input} to integer. Got error message:\n\n{repr(e)}')
```

Here we try to run our code and write a message to the log if it works. If the code fails then an exception will be raised - and our code writes that exception to the log so we can examine it later. The important thing is that by combining simple logging with simple error handling, you have really substantially improved the ease with which your code can be run and monitored. You have identified a part of the code where something is likely to go wrong and you have added some guard rails.

This is bad practice as instead of handling the specific errors the code could throw out we instead try and ignore them. Lets say our code can throw out a `ValueError`, a `ZeroDivisionError`, and a `KeyError`. Instead of catching a general `Exception` which provides no control over how each of the exceptions are handled we should instead do the following:

```python
try:
    # Some problematic code that could raise different kinds of exceptions
except ValueError as e:
    print('Found a value error!')
    print(repr(e))
    exit()
except ZeroDivisionError as e:
    print('Found a division by zero error!')
    print(repr(e))
    exit()
except KeyError as e:
    print('Found a key error!')
    print(repr(e))
    exit()
```

Alternatively if we really did want to handle all of those exceptions in the same way we should _still_ not use the generic `Exception` class. The reason for this is that if someone reads our code it is very unclear what kinds of errors the code can create, it is better to list all the errors as a tuple to provide a form of documentation like so:

```python
try:
    # Some problematic code that could raise different kinds of exceptions
except (ValueError, ZeroDivisionError, KeyError) as e:
    print('Found an error!')
    print(repr(e))
    exit()
```

### Error handling dos and don'ts

#### Don't raise a generic exception

Raising a generic exception is bad practice:

```python
raise Exception('Error I encountered')
```

The problem with raising a generic exception like this is that it is difficult to catch correctly. For example:

```python
a = 1
b = 0
try:
    a/b
    raise Exception('Error I encountered')
except Exception as e:
    print('Caught error with message: ' + repr(e))
```

While we would expect our code to catch our raised exception and print 'Caught error with message: Error I encountered', it would actually instead print that it encountered a `ZeroDivisionError`. The reason for this is that `ZeroDivisionError` is a sub/child class of `Exception`, it is encountered first so is caught first. There is also a flip-side to this which causes another issue when raising a generic `Exception`:

```python
try:
    raise Exception('Error I encountered')
except ValueError:
    exit()
```

While child classes of `Exception` are caught by an except block which catches errors of type `Exception` the same is not true the other way around. The raised `Exception` will not be caught by the except block here as it is not of type `ValueError`.

As a general rule of thumb avoid using the generic `Exception` class at all. It is often tempting to write code like this:

```python
try:
    # Some problematic code that could raise different kinds of exceptions
except Exception:
    print('Found an error!')
    exit()
```

#### Don't lose the stack trace

The stack trace (a log of where the error occurred and how it occurred), is incredibly important and is one of the most useful features of exception objects. When an exception is created it has a stack trace. For example:

```python
def a():
    return b()

def b():
    c()

def c():
    raise Exception('Don\'t call me!')

a()
```

The code above will obviously raise an exception. That exception will contain within it a stack trace showing that an exception was raised by function `c`, but it will also show the steps leading up to that: `Exception <- c <- b <- a <- a()`. This is very useful for debugging.

There are cases when writing try/except statements where we want to catch an exception, log some message, and then raise the exception again. For example we may have a function that could create a `ZeroDivisionError`, inside that function we use a try/except to catch the exception and log a message about it. However, we don't want the function to return any value as the division failed, so instead we want to raise the exception again so that the code that called the function knows it failed:

```python
def divide_two_numbers(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        print('Division failed because of: ' + repr(e))
        raise ZeroDivisionError

# In use:
a = 1.0
b = 0
try:
    result = divide_two_numbers(a, b)
except ZeroDivisionError:
    print('Division failed can\'t continue')
    exit()
```

This is _wrong_. The specific place this is wrong is here:

```python
raise ZeroDivisionError
```

Doing this raises a new ZeroDivisionError, which loses the stack trace of the original raised exception. Instead to re-raise the exception do the following:

```python
except ZeroDivisionError:
    # Do stuff
    raise
```

#### Don't let the program continue if it can't

It is a common mistake to view try/catch statements as a way of 'fixing' or avoiding an error. However, often an exception does signal that the program needs to terminate. The pseudocode below is an example of a common mistake pattern:

```python
my_file = None
try:
    my_file = open_file(path_to_my_file)
except:
    print('Couldn\'t find the file!')
print(my_file.contents())
```

This is a common case where just because an exception has been caught, that doesn't mean the error has been handled. The potential error is the file not being found, the try/catch acknowledges this but then the program moves on as if nothing has happened. This means that inevitably the final print statement will produce another error as it tries to use a `None` value. Instead the following should have been done:

```python
my_file = None
try:
    my_file = open_file(path_to_my_file)
except:
    print('Couldn\'t find the file!')
    exit()
print(my_file.contents())
```

This is a very basic example but this topic is well covered by the official python [error handling tutorial](https://docs.python.org/3/tutorial/errors.html) and so you can look there for an in-depth summary.

There is a balance to be found in applying both logging and error handling. For most code you don't need or want everything wrapped up like this - it becomes messy. Pay attention to places where your code interfaces with anything external.
<br/>

### Catching errors in PySpark

See our downloadable guide on [logging and error handling in PySpark][1]

## Further reading

- [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html "https://docs.python.org/3/howto/logging-cookbook.html")[](https://docs.python.org/3/howto/logging-cookbook.html#formatting-styles "https://docs.python.org/3/howto/logging-cookbook.html#formatting-styles")
- [Logging HowTo](https://docs.python.org/3/howto/logging.html "https://docs.python.org/3/howto/logging.html")
- [Logging in Python](https://realpython.com/python-logging)
- [General guide on errors and error handling](https://docs.python.org/3/tutorial/errors.html)
- [Page which provides a large list of errors that can be encountered](https://docs.python.org/3/library/exceptions.html)

[1]: ../pyspark/logging-and-error-handling.md
