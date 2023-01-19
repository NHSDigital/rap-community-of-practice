# # PySpark starter script
#
# This script contains lots of code snippets to get you up and running in PySpark. I've chosen a
# style that will be familiar to SQL users but that will also be compatible with testing the code.
#
# Note that this script was first written for one team in a specific context so you will not currently
# be able to run the code or follow along. We will try to set up an example with dummy data soon so
# everyone can run this code
#
# The code is now out-of-date so needs updating but hopefully still useful as-is.
#
# ## Setup
# The following section, until code line 60, it is built assuming the presence of AWS Workspace,
# and all relevant packages are installed

import findspark
findspark.init(spark_home=r"C:\Program Files\spark-3.1.1-bin-hadoop2.7")

import toml
import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import dataframe as DF

# First, set up credentials and connections for importing the databases.
# Details not shown here as they will be specific to your setup.
#
# At the start of our script, we type the following to create the spark
# application entry point, the beginning of the spark session for this script.

spark = SparkSession\
    .builder\
    .getOrCreate()

# Set up the connection to read from the different data tables
HES = spark.read.jdbc(url=conn_str_CASU, table='HES_Diabetes_comps_1011to1920', properties=conn_properties)

CCG = spark.read.jdbc(url=conn_str_CASU,  table='core_map.LATEST_GP_CCG_map', properties=conn_properties)

# ## Quick primer on PySpark
#
# Use the .show() method to see the top 20 rows

HES.show()

# `.head()` and `.tail()` will show you the top and bottom rows

HES.tail(15)
#HES.head()


# ## Filtering data - 1
#
# Let's remove records with a 'STATUS_CODE' = 'C'

CCG.filter(F.col("STATUS CODE") != "C").show()

# Notice how the filter text works just like SQL
# This is equivalent to the 'where' clause in SQL
#
# ## Selecting columns
#
# Let's select `CCG Code`, `OPEN_DATE`, `CLOSE_DATE`, and `PRESCRIBING_SETTING`

CCG_2 = CCG.select(F.col('CCG Code'), F.col('OPEN_DATE'), F.col('CLOSE_DATE'), F.col('PRESCRIBING_SETTING'))
CCG_2.show()

# Notice how the .show() is broken into steps compared to line 90 where .show()
# is applied in one line
#
# ## Aggregating data
#
# Group by CCG Code and count number of records per CCG

CCG_Code_count = (
    CCG
    .groupBy(F.col("CCG Code"))
    .count()
    )

# sort by CCG Code descending order

CCG_Code_count.sort(desc(F.col("count"))).show()

# Summing PRESCRIBING_SETTING by CCG Code

CCG_PRESB_SETTING = (
    CCG
    .groupBy(F.col("CCG Code"))
    .agg(F.sum(F.col("PRESCRIBING_SETTING")).alias("Total Prescribing Setting"))
    )
CCG_PRESB_SETTING.show()

# ## Deriving new columns
#
# The .withColumn() method allows you to create new columns
# In this example, we take the `PRESCRIBING_SETTING` field and multiply it. We
# put the results of the multiplication in a new column, `PRE_MULT`

CCG_2 = CCG_2.withColumn('NEW_COL', CCG.PRESCRIBING_SETTING*10)
CCG_2.show()


# ## Renaming columns
#
# You can rename columns with the `.withColumnRenamed()` method:

CCG_2 = CCG_2.withColumnRenamed('CCG Code', 'NEW_CCG_CODE')
CCG_2.show()


# ## Joins - 1
#
# Let's join the two dataframes back together. We will try to join on `CCG.CCG CODE = CCG_2.NEW_CCG_CODE`

CCG_3 = CCG.join(CCG_2,  CCG['CCG CODE'] == CCG_2['NEW_CCG_CODE'], how='leftouter')
CCG_3.show()

# Notice how this time we used `CCG['CCG CODE']` instead of `CCG.CCG CODE`. That is because there is a space in `CCG CODE`
# The two approached are generally equivalent


# ## Joins - 2
#
# Often in SQL we want to join tables, then `select '*'` from table one but only one column from table 2
# Let's see what that looks like

CCG_3 = (
    CCG
    .join(CCG_2,  CCG['CCG CODE'] == CCG_2['NEW_CCG_CODE'], how='leftouter')
    .select(CCG["*"], CCG_2["NEW_COL"])
    )
CCG_3.show()


# ## Method chaining
#
# In the example above, you can see that we combined multiple steps into a
# single query. This feature is one of the best parts of PySpark and is called
# 'method chaining'. The downside of the example above is that it is a very
# long line and is visually complex.
#
# To get around this, the style is to wrap the query over several lines.
# Good practice looks like this:

CCG_3 = (
    CCG
        .join(CCG_2,  CCG['CCG CODE'] == CCG_2['NEW_CCG_CODE'], how='leftouter')
        .select(CCG["*"], CCG_2["NEW_COL"])
    )

# Notice that this time we have put parentheses `()` around the query
# Notice also that we put the `.` at the beginning of each new line
#
# You can extend this chains as long as needed but take care that they don't
# become difficult to follow. Consider splitting this out into discrete,
# logical steps:

"""
CCG_3 = (
    CCG
        .join(CCG_2,  CCG['CCG CODE'] == CCG_2['NEW_CCG_CODE'], how='leftouter')
        .select(CCG["*"], CCG_2["NEW_COL"])
        .filter(...)
        .withColumn(flag1, ...)
        .withColumn(flag2, ...)
        .withColumn(flag3, flag1+flag2)
        ,withColumn('tt_num_3', tt_num_3())
        .join(...)
        .groupBy(...)
    )
"""

# ## PySpark applied to diabetes
#
# ### Prep the data
# We might want to impose a full schema here but for now I'll just fix the dates
# Following the style guide here: https://github.com/palantir/pyspark-style-guide, I will select only the columns I need and will rename/cast them at the same time
# Notice how we make sure that the columns follow correct naming conventions at the earliest possible point. This will avoid workarounds later
#
# ### Coding principles
#
#- Select only those fields you need - avoid 'SELECT *'
#- Rename and cast the data types of variables as early as possible --- nothing should get past the first select statement unless it follows the [NAMING_CONVENTION] for diabetes columns
#- Use the F.function() style. This allows us to understand which version of a function you are using.
#- When joining tables, aim to cut down the table to only the required fields before you join
#
# Set up the connection to read from the different data tables:

NDA_DEMO  = spark.read.jdbc(url=conn_str_DMS,  table='lve.NDA_DEMO_E3_202021',  properties=conn_properties)
NDA_BMI   = spark.read.jdbc(url=conn_str_DMS,  table='lve.NDA_BMI_E3_202021',   properties=conn_properties)
NDA_BP    = spark.read.jdbc(url=conn_str_DMS,  table='lve.NDA_BP_E3_202021',    properties=conn_properties)
NDA_CHOL  = spark.read.jdbc(url=conn_str_DMS,  table='lve.NDA_CHOL_E3_202021',  properties=conn_properties)
NDA_HBA1C = spark.read.jdbc(url=conn_str_DMS,  table='lve.NDA_HBA1C_E3_202021', properties=conn_properties)


# Select the fields that we are interested in.
# Note that we rename some of them using `.alias()`. We want to be sure all
# fields follow the [NAMING_CONVENTION]
# Note that we also change the data type of some of them.

NDA_DEMO = NDA_DEMO.select(
    F.col('NHS_NUMBER'),
    F.col('ORGANISATION_CODE'),
    F.to_date('CREATININE_DATE').alias('CREATININE_DATE'),
    F.to_date('ALBUMIN_DATE').alias('ALBUMIN_DATE'),
    F.to_date('EYE_EXAM_DATE').alias('EYE_EXAM_DATE'),
    F.to_date('FOOT_EXAM_DATE').alias('FOOT_EXAM_DATE'),
    F.to_date('SMOKING_DATE').alias('SMOKING_DATE'),
    F.to_date('ED_OFFER_DATE').alias('ED_OFFER_DATE'),
    F.to_date('ED_ATTEND_DATE').alias('ED_ATTEND_DATE')    
    )

NDA_BMI = NDA_BMI.select(
    F.to_date('BMI_DATE').alias('BMI_DATE'),
    F.col('NHS_Number').alias('NHS_NUMBER'),
    F.col('organisation_code').alias('ORGANISATION_CODE')
    )

NDA_BP = NDA_BP.select(
    F.to_date('BP_DATE').alias('BP_DATE'),
    F.col('NHS_Number').alias('NHS_NUMBER'),
    F.col('organisation_code').alias('ORGANISATION_CODE')
    )

NDA_CHOL = NDA_CHOL.select(
    F.to_date('CHOLESTEROL_DATE').alias('CHOLESTEROL_DATE'),
    F.col('NHS_Number').alias('NHS_NUMBER'),
    F.col('organisation_code').alias('ORGANISATION_CODE')
    )

NDA_HBA1C = NDA_HBA1C.select(
    F.to_date('HBA1C_DATE').alias('HBA1C_DATE'),
    F.col('NHS_Number').alias('NHS_NUMBER'),
    F.col('organisation_code').alias('ORGANISATION_CODE')
    )

# Identify the most recent date for each of the supplementary tables
# Specifically, get the most recent data for each person at each organisation.
# Hence, if Connor attended 12 sessions in three different clinics this year,
# we would end up with three rows for Connor. One row for each clinic he
# attended, showing the date of the most recent visit.

BMI_MAX_DATE = (
    NDA_BMI
        .groupBy(F.col('NHS_NUMBER'), F.col('ORGANISATION_CODE'))
        .agg(F.max(F.col('BMI_DATE')).alias('BMI_DATE'))
    )

BP_MAX_DATE = (
    NDA_BP
        .groupBy(F.col('NHS_NUMBER'), F.col('ORGANISATION_CODE'))
        .agg(F.max(F.col('BP_DATE')).alias('BP_DATE'))
    )

CHOL_MAX_DATE = (
    NDA_CHOL
        .groupBy(F.col('NHS_NUMBER'), F.col('ORGANISATION_CODE'))
        .agg(F.max(F.col('CHOLESTEROL_DATE')).alias('CHOLESTEROL_DATE'))
    )

HBA1C_MAX_DATE = (
    NDA_HBA1C
        .groupBy(F.col('NHS_NUMBER'), F.col('ORGANISATION_CODE'))
        .agg(F.max(F.col('HBA1C_DATE')).alias('HBA1C_DATE'))
    )


# Join the max dates to the main table
# The granularity of the main table is (person * organisation). So if Connor
# has attended three clinics this year he will

step_1 = (
    NDA_DEMO
    .join(BMI_MAX_DATE, 
            (NDA_DEMO.NHS_NUMBER        == BMI_MAX_DATE.NHS_NUMBER) & 
            (NDA_DEMO.ORGANISATION_CODE == BMI_MAX_DATE.ORGANISATION_CODE))
    .join(BP_MAX_DATEe, 
            (NDA_DEMO.NHS_NUMBER        == BP_MAX_DATE.NHS_NUMBER) & 
            (NDA_DEMO.ORGANISATION_CODE == BP_MAX_DATE.ORGANISATION_CODE))
    .join(CHOL_MAX_DATE, 
            (NDA_DEMO.NHS_NUMBER        == CHOL_MAX_DATE.NHS_NUMBER) & 
            (NDA_DEMO.ORGANISATION_CODE == CHOL_MAX_DATE.ORGANISATION_CODE))
    .join(HBA1C_MAX_DATE, 
            (NDA_DEMO.NHS_NUMBER        == HBA1C_MAX_DATE.NHS_NUMBER) & 
            (NDA_DEMO.ORGANISATION_CODE == HBA1C_MAX_DATE.ORGANISATION_CODE))
    .select(NDA_DEMO["*"], 
            BMI_MAX_DATE["BMI_DATE"],
            BP_MAX_DATE["BP_DATE"],
            CHOL_MAX_DATE["CHOLESTEROL_DATE"],
            HBA1C_MAX_DATE["HBA1C_DATE"])
)

# Create flag definitions: Add a flag for each of the date fields - 1 if there
# is a date, 0 if there is not

bmi_date_flag = (
    F.when(F.col("BMI_DATE").isNotNull(), 1).otherwise(0)
)

bp_date_flag = (
    F.when(F.col("BP_DATE").isNotNull(), 1).otherwise(0)
)

cholesterol_date_flag = (
    F.when(F.col("CHOLESTEROL_DATE").isNotNull(), 1).otherwise(0)
)

hba1c_date_flag = (
    F.when(F.col("HBA1C_DATE").isNotNull(), 1).otherwise(0)
)

# Create new columns with the flag definitions

step_2 = (
    step_1
    .withColumn('BMI_DATE_FLAG',        bmi_date_flag)
    .withColumn('BP_DATE_FLAG',         bp_date_flag)
    .withColumn('CHOL_DATE_FLAG',       cholesterol_date_flag)
    .withColumn('HBA1C_DATE_FLAG',      hba1c_date_flag)
)

# Now we can calculate the sum of those flags more clearly

flags_to_sum = ['BMI_DATE_FLAG', 'BP_DATE_FLAG', 'CHOL_DATE_FLAG', 'HBA1C_DATE_FLAG'] 

step_3 = (
    step_2
    .withColumn('DATE_COUNT', sum(step_2[col] for col in flags_to_sum))
) 

# We can now create a new field `MAX_DATE` by passing the all of the date fields to the `F.greatest()` method
# To make this more readable we first put all the date fields in a list
# We can then unpack this list using *the_list

dates_list = [ 'BMI_DATE', 'BP_DATE', 'CHOLESTEROL_DATE', 'HBA1C_DATE']

step_4 = (
    step_3
    .withColumn('MAX_DATE', F.greatest(*dates_list))
)

step_4.show()

# Export result to SQL db: write results

step_4.write.jdbc(url=conn_str_CASU, table="output_step_4", mode="overwrite", properties=conn_properties)