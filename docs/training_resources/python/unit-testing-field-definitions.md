---
title: Unit testing field definitions

tags: 
  - Unit testing
  - Testing
  - Field Definitions
  - Python
  - PySpark
---

#

This section focuses on one specific application of unit testing that is very relevant to analysts; testing the definitions of different fields (columns). One of the biggest burdens on stats teams is to maintain accurate definitions of fields over time as the specifications change. This drift in definitions is also one of the biggest sources of errors in stats publications. In the worst cases you may find that a field is defined in dozens of locations across a code-base. Each of these needs to be updated each time a change happens - leading to burden and risk.

Here we show that by separating the definitions of fields from the context in which you create those fields, you can easily maintain and manage those definitions over time. Moreover, these atomic field definitions become very easy to include in unit tests. In this way you can use simple data examples to ensure your outputs are accurate.

This is _not_ a general guide to unit testing. That guide is called '[unit-testing.md][1]'.

## Field definitions and how to use them

As was previously mentioned analysts will typically have several planned definitions for certain fields/columns of data. What can happen with these definitions is that they become repeated throughout the code base whenever they are needed; this leads to long messy code that is hard to maintain. More specifically having these definitions in many locations leads to two issues arising if the specification for one of these definitions changes:

1. The task of updating the old field definition with the new one in every place the old one occurred is time-consuming and annoying. Furthermore, the process of updating this definition in many locations can lead to bugs and inconsistencies which we have no way of checking for.
2. We have no consistent way of checking if our definition is correct if it occurs in many places in the code.

Instead of having field definition code in many places throughout the code base it would be preferable to have the code which defines the field in one place, and then re-use that definition. What this would mean is that if a change in specifications occurred then all we would have to do is change the code of that initial definition rather than the code in every place it is used. PySpark provides a very tidy way of doing this, which has been used in the diabetes RAP:

```python
foot_denom = (
    F.when((F.col('AGE') >= 12), 1).otherwise(0)
)

cvd_admission = (
    F.when(F.col('NHS_NUMBER').isNotNull(), 1).otherwise(None)
)

no_cvd_on_statins_40_to_80 = (
    F.when((F.col('CVD_ADMISSION').isNull()) &
    (F.col('IHD_VALUE').isNull()) &
    (F.col('STATIN_FLAG') == 1) &
    (F.col('AGE') >= 40) &
    (F.col('AGE') <= 80), 1).otherwise(0)
)
```

In the code above three field definitions are given:

- A `foot_denom` field which has a value of 1 if the 'AGE' column has a value of 12 or more, otherwise has a value of 0.
- A `cvd_admission` field which has a value of 1 if there is a value in the 'NHS_NUMBER' field otherwise has a null value (None).
- A `no_cvd_on_statins_50_to_80` field which has a value of 1 if: - The 'CVD_ADMISSION' and 'IHD_VALUE' columns both have a null value. - And the 'STATIN_FLAG' column has a value of 1. - And the 'AGE' column has a value between 40 and 80 inclusive. - Otherwise `no_cvd_on_statins_50_to_80` has a value of 0

With our fields defined we can now re-use them without having to write out their logic every time we do so. For example:

```python
my_dataframe
    .withColumn('FOOT_DENOM', foot_denom)
    .withColumn('CVD_ADMISSION', cvd_admission)
    .withColumn('NO_CVD_ON_STATINS_50_TO_80', no_cvd_on_statins_50_to_80)
```

In the code above several columns are added to the existing table (dataframe) `my_dataframe`. The first parameter in `withColumn` is what the name of the column will be in the table, the second parameter is one of our pre-defined field definitions. In the diabetes RAP all of our field definitions are kept in one file called `field_definitions.py`. Our field definitions can be re-used like this anywhere they are needed. This also solves the first issue mentioned before, as now if the specification of one of these field definitions changed all we would need to do is change the code that occurs in the first example (the initial definition/the code in `field_definitions.py`).

## Testing field definitions

There is still the second issue to deal with; namely how do we know our field definition is correct? Another benefit of breaking out atomic field definitions into the smallest units they can be is that we can now apply unit tests to them.

Why should we bother to write these unit tests? Especially for something as simple as our field definitions.

Unit tests test for functionality not code. This means that we base the expected output of a unit test on our design. This is well suited to field definitions as it means our metric for whether or not our field definitions are correct is based on our initial design decisions. We can then setup these tests with static data. All of our field definitions tests passing means all of our field definitions are correct. This also future-proofs our code. If someone makes a change to a field definition by mistake the test for it will fail and we will catch bugs early.

Now when we need to change the specifications for a field definition we go through the following steps:

1. Plan out the adjusted field definition and all the expected values it should output on various inputs.
2. Now we have the design of the adjusted field definition update our tests to reflect it.
3. Rewrite the code defining the field definition so that it passes our test.

We have now solved both of our initial worries with field definitions:

1. Our actual field definition code only occurs in one place so changes in specification are not cumbersome to deal with.
2. We now have unit tests as a metric to make sure our field definitions fulfil our design correctly.

## Choosing data examples to test a field definition

The benefits of unit testing field definitions mostly come back to this idea that unit tests reflect our design. Therefore, one of the most important aspects of designing these tests is to select data that covers all the kinds of cases our field definition needs to deal with.

This process should ideally function like a dialogue between the developer (D) and the responsible statistician (S), and should elucidate the design of the field definition more. For example:

— _S_: "I want a field that has a value of 1 when the column 'AGE' has a value more than 12"<br/>
— _D_: "So any value more than 12 should give 1, what if 'AGE' is less than 12?"<br/>
— _S_: "In that case we can set the value to 0"<br/>
— _D_: "What if the value of 'AGE' is equal to 12?"<br/>
— _S_: "It makes sense to have 1 also in that case"<br/>
— _D_: "What if the value of 'AGE' is 0, should we do something else?"<br/>
— _S_: "0 is still an acceptable value for 'AGE' in this case, so we would still set the value of the field to 0"<br/>
— _D_: "What if age is negative?"<br/>
— _S_: "While that is a strange case I think for this field all we are trying to show is the value of 'AGE' is more than or equal to 12, so we would still set the value of the new field to 0"<br/>
— _D_: "Fair enough, what should we do about a NULL value in the 'AGE' column?"<br/>
— _S_: "That's a trickier case but in my opinion it's the same as a negative age, all that matters is that if the 'AGE' column has a value greater than or equal to 12 we set this field to 1, so for any other value we can set it to 0."
<br/><br/>

There are three kinds of cases to deal with:

- Expected cases where the kinds of values we expect give a normal output.
- Erroneous cases where bad values should be dealt with by our code by throwing out an error.
- Edge cases where certain boundary/extreme values may need to be dealt with in a special way.

Edge cases are the cases that are the most important to define, as they require specific design decisions to be made. Through their dialogue S and D were able to identify a complete range of cases for this new field definition, we can specify example input values as well which we will use in our tests:

| Case type     | Case        | Example input | Expected output |
| ------------- | ----------- | ------------- | -------------- |
| Edge          | AGE < 0     | -1            | 0              |
| Edge          | AGE = 0     | 0             | 0              |
| Expected      | AGE < 12    | 11            | 0              |
| Edge/Expected | AGE = 12    | 12            | 1              |
| Expected      | AGE > 12    | 13, 20        | 1              |
| Edge          | AGE is NULL | None          | 0              |

With these cases outlined a test can actually be written for our new `cholesterol_denominator` field:

```python
class TestCholesterolDenominator(object):
    """
    cholesterol_denominator = (
    F.when((F.col('AGE') >= 12), 1).otherwise(0)
    )
    """
    @pytest.mark.usefixtures("spark_session")
    def test_valid_invalid_age_returns_correct_chol_denom(self, spark_session):
        input_df = spark_session.createDataFrame(
            [
                (-1, '2021-02-13'),
                (0,  '2021-02-13'),
                (11, '2021-02-13'),
                (12, '2021-02-13'),
                (13, '2021-02-13'),
                (20, '2021-02-13'),
                (None, '2021-02-13')
            ],
            ["AGE", "CHOLESTEROL_DATE"]
        )

        return_df = (input_df.withColumn('CHOLESTEROL_DEN', cholesterol_denominator))

        expected = [0, 0, 0, 1, 1, 1, 0]
        actual = [row['CHOLESTEROL_DEN'] for row in return_df.collect()]
        assert actual == expected, f"When checking cholesterol denominator, expected to find {expected} but found {actual}"
```

The `spark_session` is simply a PySpark session which we pass to our tests, this spark session allows us to create static dataframes to test. As we can see in the test above there is a dataframe `input_df` which has all the values needed to cover the cases outlined before.

We the get a new dataframe `return_df` by adding our new field `cholesterol_denominator` to `input_df` using the `withColumn` method. We can store our expected values in a list in the same order as the table above. Finally we can compare the values in our new column with the expected values to assert they are all correct.

We now have a test that can be re-run over and over, that accurately shows whether or not our field definition implemented in our code base actually fulfils it's design.

[1]: ./unit-testing.md
