# What is RAP and why should I care?
Over time, all analytical work in NHSD will be expected to adopt the working practices of RAP. This adoption will take time and should not be considered as all-or-nothing. There are stages to RAP. Teams can take the journey one step at a time with support from this community. This page lays out the background to RAP and describes what features should be implemented in the journey towards full RAP. 

# Reproducible analytical pipelines
Scientific research has increasingly relied on code to conduct complex statisticial analyses in recent years. As code has become ubiquitous, new ways of working have emerged to ensure that scientific findings are rigorous and reproducible. 

These practices have been applied to government analytic work under the banner of **RAP**. Reproducible analytical pipelines (RAP) bring together a number of good practices to help ensure all published statistics meet the highest standards of transparency and reproducibility.

## Benefits of RAP in NHSD

The NHS Digital [mission statement](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/our-strategy) says:

> Our goal is to maximise the accessibility, quality and utility of health and care data while respecting privacy, transparency and ethics. 


This goal aligns closely with the three main benefits of reproducible research from a scientific perspective [Alston and Rick, 2021](https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/bes2.1801):
> 1. "reproducible research allows others to learn from your work. Scientific research has a steep learning curve, and allowing others to access data and code gives them a head start on performing similar analyses."
> 2. "reproducible research allows others to understand and reproduce a researcher's work."
> 3. "reproducible research allows others to protect themselves from your mistakes."


RAP helps us to 
* improve the transparency and ethics by showing our workings and giving users a way to feed back into our processes.
* improve the accessibility of data by outputting data in a consistent, predictable, and accessible format for users. 
* improve the quality of data by ensuring good coding standards are applied. 
* improve the utility of data by sharing code. This shows users how the data have been produced and allowing them to resuse our code. 
* improve the reliability of data by automating manual steps where possible.


# Levels of RAP

If you want to produce your publication following RAP principles, the first step is to do an internal self-assessment against the maturity levels below. You should consider what level you aspire to achieve and how this aspiration will interact with team resourcing, BAU delivery, and the development of the NHSD Data Refinery platform. The RAP champions group can help you to work through these questions as needed. 
 

# RAP self-assessment
Analytical teams will be given an objective to adopt RAP principles over time. Each team should do an informal self-assessment and consider how they plan to adopt these RAP principles. These capabilities are independent and so you don't need to adopt all at once. Team leads should balance the BAU delivery, resourcing constraints, and RAP development as fits their agreed objectives. 

We have added some guidance on the RAP capabilities listed below but if a topic in unfamiliar it is okay to just say 'I don't know what this is'. 

Once you have completed your self-assessment and thought about the level of RAP you aim to achieve, you should approach the RAP Champion Function to discuss what support will be needed to achieve these goals. 


## Aspiring RAP

- [ ] Are you using version control? This should be the fundamental basis for all later improvements. [See git basics](development-approach/01_intro-to-git.md) and [Using git collaboratively](development-approach/02_using-git-collaboratively.md).
- [ ] Are you using an open source language (e.g. Python, R, etc.) instead of proprietary?
- [ ] Is your code well-organised following [standard directory format](python/project-structure-and-packaging.md)?
- [ ] Does your code adhere to agreed coding standards? [See style guide for Pyspark](pyspark/pyspark-style-guide.md).

## Bronze level RAP

- [ ] Are all of your outputs produced by code without the need for manual work? (NB: outputs means data, statistics, text, figures. We stop short of the CMS tool)
- [ ] Is your code well-documented including docstrings for functions, commented code, a README to explain overall code structure, and links to the main publication?
- [ ] Has your code been peer reviewed?
- [ ] Do you use reusable functions where appropriate? [See Python functions](python/python-functions.md).

## Silver level RAP

- [ ] Have you shared your code publicly on github? [See process flow for publishing safely].
- [ ] Does your code include unit tests and regression tests? [See unit tests](development-approach/04_unit-tests.md).
- [ ] Does your repo include dependency management?

## Gold level RAP

- [ ] Is your code fully packaged? [See How to package your code](python/project-structure-and-packaging.md).
- [ ] Do you run CI/CD on your code?
- [ ] Does your repo include environment management? [See Virtual Environments](python/virtual-environments.md).

<br>

## External links

Here is a good [high-level overview of RAP](https://dataingovernment.blog.gov.uk/2017/03/27/reproducible-analytical-pipeline/). It explains the context of RAP in government statistics and gives some history to the work. 

The GSS have produced a list of the [benefits that come from RAP](https://gss.civilservice.gov.uk/reproducible-analytical-pipelines/benefits-to-government-from-reproducible-analytical-pipelines/).

The [ONS best practice team have a useful website](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html) covering many of the same topics we cover here. Their [best-practice checklist](https://best-practice-and-impact.github.io/qa-of-code-guidance/checklist_higher.html)  is particularly useful.

The Statistics Authority has published this report on [overcoming barriers to RAP adoption](https://osr.statisticsauthority.gov.uk/publication/reproducible-analytical-pipelines-overcoming-barriers-to-adoption/).

The [AQUA book of analytical standards](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government).

Alston, J. M., and Rick, J. A.. 2020. A Beginner's Guide to Conducting Reproducible Research. Bull Ecol Soc Am 102(2):e01801. https://doi.org/10.1002/bes2.1801

There is also a cross-government RAP Champions group that meets occasionally.

