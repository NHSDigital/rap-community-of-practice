---
title: Making Code Discoverable using Github Topics.

tags: 
  - Git
  - Version control
  - GitHub topics
---

#

[comment]: <> (this is a mkdocs material style admonition - it will look better on the website)
!!! tip "TLDR"
    - Apply topics to each of your published repos following the ontology described below
    - Focus initially on topics related to technique and domain - these are what people are usually most interested in
    - Then, you add even more value by adding other topics. 
    - There is a [website](https://nhsengland.github.io/open-health-statistics/) which scans github for NHS github repositories and displays them by topic - making it easier to find useful code

[comment]: <> (this is a mkdocs material style admonition - it will look better on the website)
??? question "Why should we care?"
    - Applying topics for your repos will make it much easier to for you and others to find and reuse useful bits of code
    - Using a common ontology will make the topics more useful - we will all be speaking the same language

[comment]: <> (this is a mkdocs material style admonition - it will look better on the website)
??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |**None!**||Anyone can do this -though you need to [have published some code on github already](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/how-to-publish-your-code-in-the-open/)|

A key aim of RAP is to not only automate our pipelines, but to **re-use useful code in other work**. This relies on us publishing the code as publicly as possible, and then making it easy to find these useful bits of code. Topics in github can help with this, however we will get the most benefit from topics by using a common topic vocabulary to describe our GitHub code repos.

The topic ontology described in this guide will ensure our code can be searched by:

- language and tech used
- what methods were used
- whether or not the code is recent or old (and if it still updated)
- what kinds of data the code was used with and where it came from

[comment]: <> (this is a mkdocs material style admonition - it will look better on the website)
!!! warning "The Differences between 'topics' and 'tags'"
    In GitHub, tags and topics are different:
	    
	- **Topics** are labels applied to whole repos which describe them, like keywords. Each repo can up to twenty, and github is good at searching and sorting results by topics.
	- **Tags** are labels applied to specific commits within a git repo, and it's how releases are made, e.g. v0.1.0 might be a tag applied to a specific commit locking in that this commit is Version 0.1.0.

## Topics

Our aim with topics is to allow people to find code which might be useful to them, so they can reuse it. With this in mind, they usually want to know what kind of data the code was used on, in which language, if it was using the compatible datastructures (e.g. pandas, or pyspark) and how recently it was made / updated (people are less trustworth of ancient, dead code).

When applying topics to your code:

-  we suggest starting with the priority 1 categories below, e.g. Domain Area and Technique, first, as these are people tend to be most concerned with
- stick to the topics suggested below - this will ensure we get the most benefit out of them. If there are too many, it becomes meaningless. If there are important ones missing, raise an issue against this github repo with your suggestion for new topics

| Priority | Category | Description | Example topics |
|---|---|---|---|
| 1 | Domain Area/ Datasets/ Data source | People will want to know what data these techniques have been applied to, if any. This might inspire them to do something similar, or highlight areas for collaboration. | secondary-care<br/> primary-care<br/>hospital-episode-statistics<br/> gpdpr<br/> civil-registration-of-deaths<br/> gdppr<br/> artificial (perhaps if it was using artifical data) |
| 1 | Technique | People will want to know what kinds of data processing, analyses, etc. were done - this might be quite broad as it should cover the sorts of resuable code chunks people might want to look at. | clustering<br/> forecasting<br/> classification<br/> regression<br/> statistical-disclosure-control<br/> deduplication<br/> entity-resolution<br/> record-linkage<br/> summarisation<br/> data-cleansing<br/> data-validation<br/> hyperparameter-tuning<br/> artificial-data-generation<br/> etc. |
| 2 | Technology | If I want to re-use someones Python or R code, and they made it using a different data structure to me, that might cause problems, hence it's important to describe them | _dplyr_<br> _numpy_<br> _notebook_<br> _pandas_<br> _polars_<br> _pyspark_<br> _pytorch_<br> _scipy_<br> _sklearn_<br> _sparklyr_<br> _sqlalchemy_<br> _sqlalchemy-orm_<br> _tensorflow_<br>  etc. |
| 2 | Language | People often want to know if the code is using a language they know/use, and though GitHub can sometimes correctly identify the language used in the repo, if you have a lot of documentation or use certain languages (such as SQL), it can struggle. | python<br/> r<br/> sql |
| 2 | Maturity | People might want to know if a codebase is made to a high standard, or by people who are just starting out. | _baseline-rap_<br/> _silver-rap_<br/> _gold-rap_ |
| 2 | Opt-out of re-use | A tag for those people who want to publish their code, but make it clear that it is not optimised for re-use. | not-optimised-for-reuse |

## Using topics to find useful repos (and code)

You can search for repos by topic within github using the search bar (e.g., [as seen here](https://github.com/search?q=topic%3Anhs&type=repositories), with tips on github search syntax [here](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)) or [you can use this helpful website](https://nhsengland.github.io/open-health-statistics/github-topics.html) which gathers the repos and topics from the various NHS organisations on GitHub.
