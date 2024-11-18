---
title: Unit testing

tags: 
  - Testing
  - Unit testing
  - Test Driven Development (TDD)
  - Python
  - PySpark
---

#

Tests are functions which make logical assertions. If all assertions are correct then the test passes, if at least one assertion is incorrect then the test fails. Tests are a useful metric for deciding if an application has met its requirements.

Unit tests test a single piece of functionality, this functionality is delivered by a single unit of code such as a method. The philosophy behind unit tests is that if the functionality of the smallest units of the program can be guaranteed, then it is significantly more likely that the project as a whole is succeeding in delivering its functionality.

## Benefits of testing

When discussing the benefits of testing this guide will use the example field definitions to show testing in the context of RAP. For example take the field `"CREATININE_DATE"` we want another field `"CREATININE_DATE_FLAG"` to be set to 1 when there is a date value in `"CREATININE_DATE"` and 0 otherwise. We write some PySpark code to achieve this:

```python
creatinine_date_flag = (
              F.when(F.col("CREATININE_DATE").isNotNull(), 1).otherwise(0)
              )
```

What are the benefits of writing a test for this small piece of code?

### General Benefits

1. It confirms for us that the code we have written has been successful in delivering the field definition we want. We could of course do this manually, but writing tests also gives other benefits.
2. Tests persist as functions and can be re-run over and over; this is cumbersome with manual testing. This future-proofs our code. If we write our field definition code and it passes the test then we know it works. If in future when we re-run our tests we see that the test now fails then we know that a fundamental part of our program has been broken. Tests allow us to catch bugs early.
3. Tests provide an additional kind of documentation. As was mentioned in the introduction the goal of unit tests is to test a single piece of functionality. Therefore what a collection of tests passing describe is not that our code is good but rather that our code is delivering the desired functionality of the program. By viewing the results of our testing and seeing which test functions pass we are able to see what the planned and delivered functionality of the project is and what considerations have been made.
4. Tests improve general code quality not just correctness. Unit tests should be testing for a smallest unit of functionality and that functionality is typically delivered by a function in our code. If we struggle to write a unit test because we can't figure out what functions to use then our code is not modular enough and that we should break down our processing steps in our code into more functions.
5. Tests allow us to run smaller parts of code in isolation. This means that we could check to see if all the code we wrote for each of our field definitions is delivering its desired functionality. If instead we tried to run the whole program to do this it would be hard to tell if issues were arising because our code delivering the function was wrong, or because some other part of the program is causing an issue.
6. Tests are simple to write. They often use a repeated pattern of code and for such a small amount of effort a huge reward is reaped.

### Test-driven development

Test driven development (TDD) is a developmental approach in which tests are written before the code is, and then development begins. This may seem obtuse but the benefit is that it forces us to design our tests first based only on the desired functionality that the program should deliver. This leads to a couple of things:

1. If all of our tests pass then we know we have delivered all the functionality the program needs.
2. We have to break down our project and write functions to deliver these units of functionality, rather than writing tests for our functions.
3. It prevents us from having tunnel-vision when it comes to code. As our attention will always be brought back to our tests which are based on the higher-level context of the functionality the project should deliver.
4. It forces us to make sure that we understand the goals of the project before we start writing code.
   While a perfect TDD approach can be hard to achieve, maintaining its general goals will keep a project more focused. Field definitions provide an excellent example of where TDD could be useful. To apply TDD we would need to properly plan out our field definitions before hand (perhaps by looking at pre-existing SQL code if we are transitioning to PySpark). We can then write tests for each of these field definitions with the expected values we have planned to show that they are a fundamental part of the project. Initially all these tests will fail but over the course of development more will pass until we know that all of our field definitions have been implemented according to our initial plan.

### Migration

Whether we follow TDD or not our collection of tests will grow as we notice the requirement for more functionalities in the project. When the project is completed we should ideally have a complete suite of tests which all pass, and which covers all the planned functionality of the project. If at a later date our project needs to be migrated to a new domain we will still have all of our tests. Re-running our tests after migration will help reveal two things:

1. If our migration failed our tests failing should pinpoint what, if anything, is now broken in the project.
2. If our migration appears to have succeeded our tests failing will pinpoint functionality that is now broken in the project that we would otherwise have missed.

## How to design tests

It is important to take the step of designing and planning tests before you write them. Writing a bad test which doesn't accurately reflect the design of the project can do more harm than good.

### What should the test(s) be about?

The first thing to be settled is what the test should be testing. Always keep in mind is that what is being tested should be the desired functionality of the program rather than testing code that has been written. For example the wrong process would be:

1. I have written the field definition `registrations_denominator` in the diabetes RAP project code.
2. I expect this code to return a data frame with a new `"REGISTRATIONS"` field with values set to 0 when no NHS number is present and 1 if one is present.
3. I should write a test using this definition with these values.

This is bad as the focus has shifted from what the project should be delivering in terms of functionality, to instead being about what we think the expected values of some abstract function/definition should be. We need to focus on functionality.

In the case of unit tests this functionality should be the smallest units of functionality that need to be delivered. For example we might propose the following:

1. In the RAP diabetes project there are a number of field definitions.
2. We need to guarantee this core functionality should work.
3. We should write a test to check if all of our field definitions are correct.

This is incorrect. The functionality can be broken down into smaller units, for example:

1. The RAP diabetes project needs a definition for a registrations field.
2. The RAP diabetes project needs a definition for a creatinine date flag field.
3. The RAP diabetes project needs a definition for a ... field.
4. ...
5. We need to write tests for each of these core units of functionality.

We have now identified several pieces of functionality that need to be tested. Always keep in mind that a unit test only tests for that one piece of functionality; it should not test for the interaction between different parts of the program.

### How many tests and what data should the tests use?

Once we have identified our functionality to test we need to determine how many tests we need to demonstrate that functionality has been delivered. It is important to note two general practices around unit tests:

1. The code for the test itself is as short as possible while still being readable.
2. The test only makes one logical assertion (check if an input leads to the expected output). Too many logical assertions obscure the goal of the test and the test should instead be split into multiple tests.

Based on these features we will need a unit test for each case the functionality needs to handle. There are typically three kinds of cases:

1. Expected cases. Cases where the input is 'good' and our code delivers the expected output.
2. Erroneous cases. Cases where the input is 'bad' and our code handles this in some way (such as by throwing an exception) and exits gracefully.
3. Edge cases. Cases where the input is likely to require special handling by our function (extreme cases).

Lets take the example of sorting a list. We have identified that our project needs to support the small unit of functionality to sort a list of integers into ascending order. We can identify some cases to test quickly:

| Type of case | Behaviour                                                                                    |
| ------------ | -------------------------------------------------------------------------------------------- |
| Expected     | A list in ascending order should be returned unchanged                                       |
| Expected     | A list in descending order should be returned in ascending order                             |
| Expected     | A list in a random order should be returned in ascending order                               |
| Erroneous    | A list that contains a null/none value should throw an exception                             |
| Erroneous    | A list that contains data of the wrong type (string, float etc) should throw an exception    |
| Edge         | An empty list should not throw an exception, and an empty list should be returned            |
| Edge         | A list with repeated values should be sorted like normal with repeated values interchangeable |

We have now identified 7 unit tests for this piece of functionality. The process of figuring out cases has also elucidated two more things:

1. The input data to our tests has been outlined as well as the expected results.
2. We have made our design decisions more explicit and open. For example our two edge cases could be seen as erroneous cases by someone with a different view. They may want lists which are empty/contain repeated values to throw an exception rather than be treated as correct.
3. Because our tests reflect our design the only acceptable result for our tests is all of them passing. We cannot ignore a failed test as it means our code does not live up to our design.

It is also debatable if we need all three of our expected cases and whether one would just do. This is generally up to how much test coverage you feel a feature needs but it is important to note that you should not have tests which repeat themselves and you should not have tests which test for the same thing as this will make your collection of tests cluttered.

### What should the test be named?

It is important in general to have good function names but this is especially true in the case of unit tests. There are some reasons for this:

1. Test suites grow to be very large, and test code is difficult to read.
2. Team members who have not written some of the tests need to run the test suite and understand the result.
3. Sometimes non-programmers/those not as involved in development need to run the test suite and understand the result.

Therefore when naming a test we need to describe what functionality the test is for, what kind of data is being used as input, and what is the expected output. There is no set method for naming tests but a good starting point is to simply describe the test as if you were explaining it to someone with knowledge of the programs domain but not much programming knowledge. This generally leads to clear test names. Here are some more specific tips for writing test names:

- Make sure every word in the test name is separated by an underscore. A test called `dividingTwoNumbersIsInvalidWhenDividingByZero` is difficult to read compared to `dividing_two_numbers_is_invalid_when_dividing_by_zero`.
- Don't worry too much about conforming to a specific test naming scheme such as '\[method name\]\_Should\[expected result\]\_When\[conditions\]'. While a scheme can make test names more uniform it doesn't necessarily make them more readable. The thought you should always have when naming the test is to simply explain what the test is testing for as if you were explaining it to someone with basic knowledge of the project.
- Try to avoid using the function name in the test such as `divideTwoNumbers_invalid_when_dividing_by_zero` as this suggests you are testing a function rather than trying to get the function to deliver the desired functionality. Something like `division_by_zero_is_invalid` is a much better test name.
- When using pytest always prepend `test_` at the start of your test's name.
- Drop hopeful language such as `should` or `will` and instead just describe the desired functionality.
- Avoid technical jargon where possible, words such as `returns` in a test name make it difficult for someone with less programming knowledge to understand the goal of the test.

While keeping these tips in mind is beneficial don't stress too much about following them exactly, and it is ok to ignore some or all of them as long as you come up with a test name that quickly conveys what the test is about.

## How to write unit tests

This guide will not focus on all the basic setup and features of pytest as this is better covered in external resources (one of which can be found at the top of this guide). There are however some other tips for actually writing tests that can be helpful.

### Test suites (where to put your tests)

Your test functions will obviously be stored in a file but having all of your tests in one file can become messy. At some point we need to plan how to organise and lay out our tests in order to make best use of them. In a RAP project you will typically have three kinds of tests:

- Unit tests which have been covered in this guide.
- Integration tests which test the interaction between modules of the program (occurs after unit testing).
- Backtesting used to check how successful the pipeline is on historical data.

These three classes of tests need to be separated out. The simplest way to do this is to have a subfolder in your main tests folder for each fo these kinds of tests, and then within these subfolders have Python files containing the tests:

- "tests":
  - "unittests":
    - unit test code
  - "integration"
    - integration test code
  - "backtesting"
    - backtesting code

We may also want to separate out our tests further into domains. For example we could have all of our unit tests in one file in the unit tests subfolder. Alternatively we may have several files for unit tests for different parts of the project. For example in the diabetes RAP we have:

- `test_data_connections.py`
- `test_field_definitions.py`
- `test_schema_definitions.py`

The goal with separating out tests like this is to make our collection of tests as readable and as uncluttered as possible. A final pattern which is useful to follow to keep test collections tidy is to contain the unit test functions themselves in a class related to the functionality they deliver. For example in the diabetes RAP we have the following:

```python
class TestCholesterolNumerator(object):
  """
  cholesterol_numerator = (
  F.when((F.col('AGE') >= 12) & (F.col("CHOLESTEROL_DATE").isNotNull()), 1).otherwise(0)
  )
  """
  @pytest.mark.usefixtures("spark_session")
  def test_valid_invalid_age_returns_correct_chol_numerator(self, spark_session):
  ...
  @pytest.mark.usefixtures("spark_session")
  def test_valid_invalid_cholesterol_date_returns_correct_chol_numer(self, spark_session):
```

(Test function bodies omitted for brevity).

The functionality we are testing for is a `cholesterol_numerator` field definition so we create a class for this functionality called `TestCholesterolNumerator`. We have identified we need two tests to guarantee this functionality so we write these tests as we normally would but put them within the `TestCholesterolNumerator` class. This makes it clear what functionality each test relates to.

## External links

- [Guide covering all the core features of pytest](https://realpython.com/pytest-python-testing/)
