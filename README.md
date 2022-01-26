***Warning - this repository is a snapshot of a repository internal to NHS Digital.
This means that links to videos and some URLs may not work.***

***Repository owner: [NHS Digital Analytical Services](https://github.com/NHSDigital/data-analytics-services)***

***Email: datascience@nhs.net***

***To contact us raise an issue on Github or via email and will respond promptly.***

# RAP community of practice
Welcome to the landing page for the RAP community of practice repo. 

You can learn all about Reproducible analytical pipelines (RAP) on our [what is RAP](what-is-RAP.md) page. In a nutshell though, RAP is becoming the standard for publishing analytical outputs in government. RAP combines a number of ways of working that help to improve the reliability, transparency, and speed of statistics publications. Reproducible Analytical Pipelines follow the principles of the [AQUA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) guidelines, which revolve around analysis being reproducible, auditable, transparent, and quality assured. 

The RAP community of practice includes all analysts and data scientists who are interested in adopting the working practices included in [reproducible analytical pipelines (RAP)](what-is-RAP.md). This repo is a central repository for resources and guidance to help teams adopting RAP practices. There is an associated [MS Teams page] where you can introduce yourself, ask for help, or discuss different approaches. Over time we hope to build up a community of people who can self-support and further develop these ways of working.

The community of practice aims to support teams in adopting RAP practices through: 
1. Offering in-person support as teams establish new working practices
2. Producing learning materials that offer reusable templates adapted for the NHSD analytical environment

This work is prompted by the observations that teams can struggle to adopt RAP practices without direct support. While no one element of RAP is particularly difficult, learning several new skills at the same time as delivering BAU is challenging. Teams can struggle to find the defended time to embed these practices. See the Statistics Authority report on [the barriers to RAP adoption](https://osr.statisticsauthority.gov.uk/publication/reproducible-analytical-pipelines-overcoming-barriers-to-adoption/) for more information. Luckily, in NHSD we have strong senior support for RAP and many teams have already begun to adopt many of the practices included in RAP. Consequently, we already have a large pool of skilled, ethusiastic analysts who are willing to help others. These resources also aim to support the goals laid out in the Goldacre report [Bringing NHS data analysis into the 21st century](https://journals.sagepub.com/doi/10.1177/0141076820930666) and to align with Tim Berners-Lee's [Five star data](https://5stardata.info/en/) principles.

## RAP package template
We have built a Python RAP package template and it's freely available to use via Github, [see RAP package template](https://github.com/NHSDigital/rap-package-template).

## Support and training
If your team is embarking upon a RAP journey, you should look at our [what is RAP](what-is-RAP.md) page and try to complete the [self-assessment](what-is-RAP.md#rap-self-assessment). From there, we recommend reaching out for some in-person support. The RAP Champion Function (within the Data Science Skilled Team) can offer support in many forms:
* Reviewing your RAP work and assessing your progress against the [levels of RAP](what-is-RAP.md#levels-of-rap)
* Peer review of code
* Workshops for a specific RAP capability
* Consultancy style engagement where we plan a migration strategy
* Pair coding
* Shadowing another team

If you want to talk about any of this then please reach out on the [RAP community of practice MS Teams] page (internal to NHSD). 

We maintain a list of people who are willing to dedicate some time to support others. Please add your name to the mix if you are willing to support someone else. You don't need to be an expert - just willing to share what you know. 


## Tutorials and resources
As we work alongside teams, we try to produce reusable learning materials pitched at specifically supporting NHSD teams. We try (with partial success) to avoid reproducing guidance that is easily available online. Instead, we link to lots of external resources where you can self-serve. Our focus instead aims to create some bespoke guidance that lays out how you would accomplish these practices in the NHSD setting.

Here are some of the initial resources:

* [Learn about the basics of git](development-approach/01_intro-to-git.md)

* [Learn how to use git collaboratively in your team](development-approach/02_using-git-collaboratively.md)

* [Read our style guide for pyspark](pyspark/pyspark-style-guide.md)

* [Work through some starter code in the pyspark tutorial script](pyspark/pyspark-tutorial.py)

* [Learn how functions can improve your python code](python/python-functions.md)

* [Learn how to design and write unit tests](development-approach/04_unit-tests.md)

* [Learn about how to write and test field definitions in a way that is easy to understand and maintain](development-approach/05_unit-testing-field-definitions.md)

* [Learn how tidy data can help teams to use a consistent format](development-approach/06_tidy-data.md)

* [Learn how packaging your code can make it easier to share](python/project-structure-and-packaging.md)

* [Learn how virtual environments can make your code more reliable](python/virtual-environments.md)

* [Learn about logging and error handling in your code](python/logging-and-error-handling.md)
  
* [Learn about creating the QA plan for your RAP project](development-approach/03_quality-assuring-analytical-ouputs.md)

* [Learn about visualisations in Python](python/visualisation-in-python.md)

* [Learn how to publish your code in the open](development-approach/08_how-to-publish-your-code-in-the-open.md)

* [Learn about the difference between using notebooks vs IDEs](development-approach/07_notebooks_versus_ide_development.md)

These resources are demand-driven so if you want something then please ask on the [MS Teams page]. We would also ask you to contribute if you can improve on any of the resources or can fill in any other gaps. 

The resources are not intended to be prescriptive. There are many ways to accomplish a task and teams have valid reasons for choosing other approaches. Instead the intention of the resources provided here is to offer a way in for teams who want to adopt good practices that they have heard about but don't know where to start.

## Misc
We have taken inspiration from the [NHSD software engineering COP](https://github.com/NHSDigital/software-engineering-quality-framework/blob/master/insights/review.md). It has tons of great material so I encourage you to read and reflect on these working practices.

## Licence
RAP Community of Practice codebase is released under the MIT License.

The documentation is © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

