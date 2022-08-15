# Pyspark

Pyspark is a flavour of Python that enables us to make use of the distributed processing available in NHS Digital. This enables analysts to run queries against datasets that are far too big to fit in computer memory.

We recommend that analytical teams in NHS Digital should in general use Pyspark for their code. There are a number of reasons for this:

* In NHS Digital we have some very large datasets. Given our tech stack, the best way for us to process these datasets is to use Pyspark. Other options risk running out of memory or disrupting the work of other teams by using compute resource inefficiently.

* If you know that you will need to use Pyspark *sometimes* then it is easier to just use it from the outset instead of trying to adapt Python or R when you run out of memory.

* Pyspark has critical mass in the NHS Digital data engineering community and so there is depth of technical knowledge.

* Pyspark is much easier to learn for people coming from SQL. All the same keywords are used: select, where, group by, etc. This is in sharp contrast to e.g., Pandas which has an extremely steep learning curve for new starters. 

* Choosing one language to support enables us to provide better training and support. 

* Aligning around one language as much as possible means that it is easier for teams to mutually support each other.


**Note: we strongly believe that teams should have the option to use whatever tool they deem right for their situation. We focus our efforts on supporting Pyspark but do not want to prevent teams from choosing another course**


* [Read our style guide for pyspark](pyspark-style-guide.md)

* [Work through some starter code in the pyspark tutorial script](pyspark-tutorial.py)


