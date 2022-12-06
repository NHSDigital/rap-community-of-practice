# Levels of RAP

To help analyst teams implement RAP, we've created a maturity framework we call the 'levels of RAP'.

## The 'Levels of RAP' Maturity Framework

There are three levels:

1. [Baseline](#baseline-rap---getting-the-fundamentals-right) - **RAP fundamentals** offering resilience against future change.
2. [Silver](#silver-rap---implementing-best-practice) - **Implementing best practice** by following good analytical and software engineering standards.
3. [Gold](#gold-rap---analysis-as-a-product) - **Analysis as a product** to further elevate your analytical work and enhance its reusability to the public.

The levels of RAP maturity framework helps teams balance BAU delivery, resourcing constraints and other organisational objectives alongside RAP implementation.

## Which level should I aim for?

The Baseline level is designated as the _minimum standard of a RAP_.

Silver and Gold RAP help external users reuse code and support moving to a fully-automated solution. However they often require significant time and investment in upskilling.

Many teams will aim for Baseline RAP in their first RAP attempt, and aim for Silver or Gold RAP for further releases. The different levels allow teams to tackle capabilities iteratively, rather than all at once. Initially aiming for Baseline or Silver RAP means that teams see some of the immediate benefits of RAP while having the time needed to learn new skills.

It's important to balance the work required to implement RAP and the benefit you'll get (e.g. time & resource-saving); in other words, match the RAP level to the product. For example, some ad-hoc analysis products probably do not need to aim for silver or gold RAP.

> The levels of RAP are the outcome of discussions with the cross-government RAP group, with input from team leads, the head of the Analytics Function, the head of Data Science, the Chief Statistician, the Statistics Regulator at NHS Digital.

## Baseline RAP - getting the fundamentals right

In order for a publication to be considered a reproducible analytical pipeline, it must at least meet all of the requirements of Baseline RAP:

- [ ] Data produced by code in an open-source language (e.g., Python, R, SQL).
- [ ] Code is version controlled (see [Git basics][1] and [using Git collaboratively][2] guides).
- [ ] Repository includes a README.md file (or equivalent) that clearly details steps a user must follow to reproduce the code (use [NHS Open Source Policy section on Readmes](https://github.com/nhsx/open-source-policy/blob/main/open-source-policy.md#b-readmes) as a guide.
- [ ] Code has been [peer reviewed][9].
- [ ] Code is [published in the open][4] and linked to & from accompanying publication (if relevant).

## Silver RAP - implementing best practice

_Meeting all of the above requirements, plus:_

- [ ] Outputs are produced by code with minimal manual intervention.
- [ ] Code is well-documented including user guidance, explanation of code structure & methodology and [docstrings][10] for functions.
- [ ] Code is well-organised following [standard directory format][5].
- [ ] [Reusable functions][6] and/or classes are used where appropriate.
- [ ] Code adheres to agreed coding standards (e.g PEP8, [style guide for Pyspark][3]).
- [ ] Pipeline includes a testing framework ([unit tests][7], [back tests][8]).
- [ ] Repository includes dependency information (e.g. [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files), [PipFile](https://github.com/pypa/pipfile/blob/main/README.rst), [environment.yml][12]).
- [ ] [Logs][11] are automatically recorded by the pipeline to ensure outputs are as expected.
- [ ] Data is handled and output in a [Tidy data format](https://medium.com/@kimrodrikwa/untidy-data-a90b6e3ebe4c).

## Gold RAP - analysis as a product

_Meeting all of the above requirements, plus:_

- [ ] Code is fully [packaged](https://packaging.python.org/en/latest/).
- [ ] Repository automatically runs tests etc. via [CI](https://github.com/skills/continuous-integration)/CD or a different integration/deployment tool e.g. [GitHub Actions](https://docs.github.com/en/actions).
- [ ] Process runs based on event-based triggers (e.g., new data in database) or on a schedule.
- [ ] Changes to the RAP are clearly signposted. E.g. a changelog in the package, releases etc. (See gov.uk info on [Semantic Versioning](https://github.com/alphagov/govuk-frontend/blob/main/docs/contributing/versioning.md))

[1]: ../training_resources/git/intro-to-git.md
[2]: ../training_resources/git/using-git-collaboratively.md
[3]: ../training_resources/pyspark/pyspark-style-guide.md
[4]: ../implementing_RAP/how-to-publish-your-code-in-the-open.md
[5]: ../training_resources/python/project-structure-and-packaging.md
[6]: ../training_resources/python/python-functions.md
[7]: ../training_resources/python/unit-testing.md
[8]: ../training_resources/python/backtesting.md
[9]: ../implementing_RAP/code-review.md
[10]: ../training_resources/python/python-functions.md#documentation
[11]: ../training_resources/python/logging-and-error-handling.md
[12]: ../training_resources/python/virtual-environments/conda.md
