---
title: Data Classes

tags: 
  - Data Classes
  - Config
  - Python
  - PySpark
---

#

by Alistair Jones

!!! tip "TLDR"

    - Classes are used for storing data and code that acts upon that data.
    - Functions forget what happens in each call, while the state of a class stores information between calls to the classes' methods.
    - Data classes are a special type of class that are useful for passing parameters around a pipeline

## Introduction

This is a brief guide into the what, why and how of 'data classes' - which are a special type of classes in Python.

The page provides a high-level overview of classes, aiming to serve as a jumping-off point rather than replicating the vast quantities of [documentation about classes](https://docs.python.org/3/tutorial/classes.html) on the internet.

The primary focus is on data classes and how they can benefit Reproducible Analytical Pipelines. 


## What is a class?

A class is essentially a reusable template for storing data and code which acts upon that data.

Consider what happens when we call a Python function: usually it will take some input data, do something with that data and possibly return some output.

In general, a function forgets about what happens between calls, so if we called it again with the same arguments we'd get the same result, again and again. 

Classes are slightly different - there are two principal concepts:

- The state of a class represents the data it stores - for example, a class representing a person might have 'name', 'dob' and 'address' stored within its state
- The methods of a class contain code that use and modify the state of a class.

See [this page](https://www.w3schools.com/python/python_classes.asp) for a tutorial to help with getting started with classes in Python.


## Why should I care about classes?

Classes are a convenient way to program when you need to keep track of state information.

It is perfectly fine not to use them and indeed for many scenarios they can unnecessarily increase complexity and can contribute towards to [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code)!

But when you find yourself passing the same data around the same set of functions again and again, then classes might help to reduce duplication and avoid repetition. 


## What is a 'data class'?

A data class is a special type of class in Python. As the name suggests, data classes are typically used as containers for passing data around different parts of a pipeline or program - they don't usually have much logic defined in methods, rather they are used to pass data between functions. 

_(Note that here the term "data" is meant broadly - not just the tabular data that you get from your database (though it could be), but also any value, parameter, or variable that you might need to put in your code.)_

In a Reproducible Analytical Pipeline, we usual have some parameters that need to be passed together to different parts of the pipeline, such as the start and end dates for a publication.

If our functions for field definitions, creating tables, etc, all need to access these parameters, one way would be to have the same parameters provided multiple times in function arguments:

```py
from datetime import date

def my_first_function(start_date: date, end_date: date):
  # some interesting logic

def my_second_function(start_date: date, end_date: date):
  # some other interesting logic
```

_(You may note that this example makes use of type hints, which are incredibly useful and necessary for explaining and using data classes. However, for brevity, type hints will not be covered in depth here - for more information, [read this](https://dev.to/dev0928/what-are-type-hints-in-python-3c2k).)_

For a small number of parameters, and a small number of functions, this is probably fine. But imagine what this starts to look like as the number of parameters increases, as does the number of functions - there starts to be lots of repeated code, which is both harder to read and more prone to errors!

## Example: using data classes to store parameters

With data classes, we can rewrite the above as follow:

```py
import dataclasses
from datetime import date
@dataclasses.dataclass

class PublicationDates:
  start_date: date
  end_date: date
 
  def my_first_function(publication_dates: PublicationDates):
    # some interesting logic
    # access the start_date attribute via `publication_dates.start_date` 
    # access the end_date attribute via `publication_dates.end_date` 

  def my_second_function(publication_dates: PublicationDates):
    # some other interesting logic
    # access the start_date attribute via `publication_dates.start_date` 
    # access the end_date attribute via ` publication_dates.end_date`
```

Notice now that instead of two arguments, we have one - just the `PublicationDates` data class. 

Someone who wanted to use these functions could then do so as follows:

```py
start_date = date(2023, 1, 1)
end_date = date(2024, 1, 1)
my_publication_dates = PublicationDates(start_date, end_date)

my_first_result = my_first_function(my_publication_dates)
my_second_result = my_second_function(my_publication_dates)
```

Although the benefits may be limited for this contrived example, we can see that:

1. The intent is clearer when we read our function - rather than just having independent parameters called `start_date` and `end_date` we immediately know that these variables are a pair, representing the publication start and end dates, since they are contained together within the data class.
2. Since `my_publication_dates` is passed to both functions, we now have a single argument for each function, so the code is easier to read and there is less room for error (e.g. it's not possible to mix up our `start_date` and `end_date` . This doesn't make a huge difference in this example with two functions and two parameters, but imagine what happens as the pipeline gets bigger.

## Validations using data classes

A great feature of data classes is that after they are created, a special function - called `__postinit__` runs that you can use to do things like run validations or checks, or to derive additional attributes. 

For example:

```py
import dataclasses
from datetime import date

@dataclasses.dataclass
class PublicationDates:
  start_date: date
  end_date: date

  def __postinit__(self):
    # Raise an error if start date less than end date
    assert self.start_date < self.end_date, "Start date was not less than end date!"

good_publication_dates = PublicationDates(start_date=date(2022, 1, 1), end_date=date(2023, 1, 1)) # This will be fine
bad_publication_dates = PublicationDates(start_date=date(2023, 1, 1), end_date=date(2022, 1, 1)) # This will raise an AssertionError
```

So now, in addition to the benefits we had previously, we can also have checks and validations running at the time that we define our parameters  - rather than individually within each function, or via creating another function to do these checks that we need to remember to call - the logic is built into how the parameters are defined! This also makes it clearer to someone who wants to use these parameters that there are constraints on the values.

You don't have to define a `__postinit__` method but it can be useful in certain situations!

## Further reading

- [Data classes guide on Data Quest](https://www.dataquest.io/blog/how-to-use-python-data-classes/)
- For NHSE Employees, see this [video walkthrough](https://nhsd-confluence.digital.nhs.uk/download/attachments/483240713/Classes%20in%20RAP%20projects%20demo-20230413_103354-Meeting%20Recording.mp4?api=v2&modificationDate=1681382735402&version=1) of how data classes could be used to improve RAP projects, with examples from the National Diabetes Audit RAP project.