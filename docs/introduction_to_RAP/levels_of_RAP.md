# Levels of RAP

These levels of RAP are the outcome of discussions on the cross-govt RAP group, as well as input from the head of the Analytics Function, the head of Data Science, the Chief Statistician, the Statistics Regulator, and NHS Digital team leads.

These levels aim to offer teams a recommended maturity map for adopting RAP practices. We have seen that teams who skip the early capabilities struggle to make effective progress. These capabilities are independent and so you don't need to adopt all at once. Team leads should balance the BAU delivery, resourcing constraints, and RAP development as fits their agreed objectives.

**In order for a publication to be considered a reproducible analytical pipeline, it must at least meet all of the requirements of _baseline RAP_. Typically teams will go beyond this minimum baseline and we encourage this. The baseline serves to describe the absolute minimum needed to be considered RAP.**

### Baseline RAP - the minimum to be considered RAP

- [ ] Data produced by code in an open-source language (e.g., Python, R, SQL)
- [ ] Code is version controlled. This should be the fundamental basis for all later improvements. [See Git basics][1] and [Using Git collaboratively][2]
- [ ] Code has been peer reviewed and adheres to agreed coding standards. E.g [style guide for Pyspark][3].
- [ ] Code is published in the open. [See process flow for publishing safely][4]
- [ ] Open data published (if there is a publication)
- [ ] The publication should link to the code repo and vice versa (if there is a publication).

### Silver RAP - a recommended middle ground

- [ ] Are all outputs produced by code without the need for manual work?
- [ ] Code is well-organised following [standard directory format][5]
- [ ] Is your code well-documented including user guidance (aka desk notes or runbooks), a README to explain overall code structure and usage, docstrings for functions, commented code, and links to the main publication?
- [ ] Do you use reusable functions where appropriate? [See Python functions][6]
- [ ] Does your code include tests (could be unit tests, regression tests, or automated sense checks as appropriate). [See unit tests][7]
- [ ] Does your repo include dependency management? (i.e. requirements.txt, PipFile, environment.yml or equivalent)

### Gold RAP

- [ ] Is your code fully packaged?
- [ ] Do you run CI/CD on your code?
- [ ] Does your repo include environment management?
- [ ] Does your process run based on event-based triggers (e.g., new data in database) or on a schedule?
- [ ] Changes to the package clearly signposted. E.g. a changelog in the package, server for package versions, etc.

[1]: ../training_resources/git/intro-to-git.md
[2]: ../training_resources/git/using-git-collaboratively.md
[3]: ../training_resources/pyspark/pyspark-style-guide.md
[4]: ../implementing_RAP/how-to-publish-your-code-in-the-open.md
[5]: ../training_resources/python/project-structure-and-packaging.md
[6]: ../training_resources/python/python-functions.md
[7]: ../training_resources/python/unit-testing.md
