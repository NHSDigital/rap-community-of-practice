# What is RAP and why should I care?
Scientific research has increasingly relied on code to conduct complex statisticial analyses in recent years. As code has become ubiquitous, new ways of working have emerged to ensure that scientific findings are rigorous and reproducible. 

These practices have been applied to government analytic work under the banner of **reproducible analytical pipelines (RAP)**. RAPs bring together a number of good practices to help ensure all published statistics meet the highest standards of transparency and reproducibility.

Over time, all analytical work in NHSD (and across government) will be expected to adopt the RAP practices. For example, RAP practices are a key element needed in order to meet the standards of quality analysis set out in the [Aqua Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government). This adoption will take time and should not be considered as all-or-nothing. There are stages to RAP. Teams can take the journey one step at a time with support from this community. This page lays out the background to RAP and describes what features should be implemented in the journey towards full RAP. 


### The benefits of RAP in NHSD

The NHS Digital [mission statement](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/our-strategy) says:

> Our goal is to maximise the accessibility, quality and utility of health and care data while respecting privacy, transparency and ethics. 

This goal aligns closely with the three main benefits of reproducible research from a scientific perspective [Alston and Rick, 2021](https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/bes2.1801):
> 1. "reproducible research allows others to learn from your work. Scientific research has a steep learning curve, and allowing others to access data and code gives them a head start on performing similar analyses."
> 2. "reproducible research allows others to understand and reproduce a researcher's work."
> 3. "reproducible research allows others to protect themselves from your mistakes."

RAP therefore helps us to 
* improve the transparency and ethics by showing our workings and giving users a way to feed back into our processes.
* improve the accessibility of data by outputting data in a consistent, predictable, and accessible format for users. 
* improve the quality of data by ensuring good coding standards are applied. 
* improve the utility of data by sharing code. This shows users how the data have been produced and allowing them to reuse our code. 
* improve the reliability of data by automating manual steps where possible.


# Levels of RAP
These levels of RAP are the outcome of discussions on the cross-govt RAP group, as well as input from the head of the Analytics Function, the head of Data Science, the Chief Statisician, the Statistics Regulator, and NHSD team leads. 

These levels aim to offer teams a recommended maturity map for adopting RAP practices. We have seen that teams who skip the early capabilities struggle to make effective progress. These capabilities are independent and so you don't need to adopt all at once. Team leads should balance the BAU delivery, resourcing constraints, and RAP development as fits their agreed objectives. 

**In order for a publication to be considered a reproducible analytical pipeline, it must at least meet all of the requirements of *baseline RAP*. Typically teams will go beyond this minimum baseline and we encourage this. The baseline serves to describe the absolute minimum needed to be considered RAP.** 

### Baseline RAP - the minimum to be considered RAP
- [ ] Data produced by code in an open-source language (e.g., python, R, SQL) 
- [ ] Code is version controlled. This should be the fundamental basis for all later improvements. [See git basics](development-approach/01_intro-to-git.md) and [Using git collaboratively](development-approach/02_using-git-collaboratively.md)
- [ ] Code has been peer reviewed and adheres to agreed coding standards. E.g [style guide for Pyspark](pyspark/pyspark-style-guide.md).
- [ ] Code is published publicly on github. [See process flow for publishing safely](https://nhsd-confluence.digital.nhs.uk/display/DAT/DS_216%3A+Main+diagram)
- [ ] Open data published (if there is a publication) 
- [ ] The publication should link to the code repo and vice versa (if there is a publication).

### Silver RAP - a recommended middle ground
- [ ] Are all outputs produced by code without the need for manual work? 
- [ ] Code is well-organised following [standard directory format](python/project-structure-and-packaging.md)
- [ ] Is your code well-documented including user guidance (aka desk notes or runbooks), a README to explain overall code structure and usage, docstrings for functions, commented code, and links to the main publication? 
- [ ] Do you use reusable functions where appropriate? [See Python functions](python/python-functions.md)
- [ ] Does your code include tests (could be unit tests, regression tests, or automated sense checks as appropriate). [See unit tests](development-approach/05_unit-tests.md)
- [ ] Does your repo include dependency management? (i.e. requirements.txt or conda environment for RDS users. Not possible in DAE) 

### Gold RAP
- [ ] Is your code fully packaged? 
- [ ] Do you run CI/CD on your code? 
- [ ] Does your repo include environment management? 
- [ ] Does your process run based on event-based triggers (e.g., new data in database) or on a schedule? 
- [ ] Changes to the package clearly signposted. E.g. a changelog in the package, server for package versions, etc. 

<br>

