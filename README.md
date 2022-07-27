***Warning - this repository is a snapshot of a repository internal to NHS Digital.
This means that some links may not work for external readers.***

***Repository owner: [NHS Digital Analytical Services](https://github.com/NHSDigital/data-analytics-services)***

***Email: [datascience@nhs.net](mailto:datascience@nhs.net)***

***To contact us raise an issue on Github or via email and will respond promptly.***

# RAP community of practice
Welcome to the landing page for the RAP community of practice repo. 

**The [Goldacre Review](https://www.gov.uk/government/publications/better-broader-safer-using-health-data-for-research-and-analysis), tasked with finding ways to deliver better, broader, and safer use of NHS data for analysis and research, identified RAP as the essential element to ensure high-quality analysis.** More, Reproducible Analytical Pipelines follow the principles of the [AQUA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) guidelines, which revolve around analysis being reproducible, auditable, transparent, and quality assured. 

You can learn all about reproducible analytical pipelines (RAP) on our [What is RAP](what-is-RAP.md) page. In a nutshell though, RAP is becoming the standard for creating analytical outputs in government. RAP combines a number of ways of working that help to improve the reliability, transparency, and speed of statistics publications. 

The RAP community of practice is open to all analysts and data scientists who are interested in adopting the working practices included in [reproducible analytical pipelines (RAP)](what-is-RAP.md). This repo is a central repository for resources and guidance to help teams adopting RAP practices. There is an associated [MS Teams page](https://teams.microsoft.com/l/channel/19%3aEnoJ_c3NIwcWaLoqHyrbmiui8SI-8lZ1B2SvxNuGbyU1%40thread.tacv2/General?groupId=1c1528d7-030e-48eb-92cf-dc0f6a618ea0&tenantId=50f6071f-bbfe-401a-8803-673748e629e2) where you can introduce yourself, ask for help, or discuss different approaches. You can also ask issues directly by [opening an issue on the repo](https://github.com/NHSDigital/rap-community-of-practice/issues). Over time we hope to build up a community of people who can self-support and further develop these ways of working.

The community of practice aims to support teams in adopting RAP practices through: 
1. Offering in-person support as teams establish new working practices
2. Producing learning materials that offer reusable templates adapted for the NHSD analytical environment

This work is prompted by the observations that teams can struggle to adopt RAP practices without direct support. While no one element of RAP is particularly difficult, learning several new skills at the same time as delivering BAU is challenging. Teams can struggle to find the defended time to embed these practices. See the Statistics Authority report on [the barriers to RAP adoption](https://osr.statisticsauthority.gov.uk/publication/reproducible-analytical-pipelines-overcoming-barriers-to-adoption/) for an excellent discussion of the challenges in rolling out RAP. Luckily, in NHSD we have strong senior support for RAP and many teams have already begun to adopt many of the practices included in RAP. Consequently, we already have a large pool of skilled, ethusiastic analysts who are willing to help others. These resources also aim to support the goals laid out in the Goldacre report [Bringing NHS data analysis into the 21st century](https://journals.sagepub.com/doi/10.1177/0141076820930666) and to align with Tim Berners-Lee's [five star data](https://5stardata.info/en/) principles.

## Support and training
If your team is embarking upon a RAP journey, you should look at our [what is RAP](what-is-RAP.md) page and think about which [levels of RAP](what-is-RAP.md#levels-of-rap) that you want to target. From there, we recommend reaching out for some in-person support. The RAP Champion Function (within the Data Science Skilled Team) can offer support in many forms:
* Reviewing your RAP work and assessing your progress against the [levels of RAP](what-is-RAP.md#levels-of-rap)
* Peer review of code
* Workshops for a specific RAP capability
* Consultancy style engagement where we plan a migration strategy
* Pair coding
* Shadowing another team

If you want to talk about any of this then please reach out on the [RAP community of practice MS Teams](https://teams.microsoft.com/l/channel/19%3aEnoJ_c3NIwcWaLoqHyrbmiui8SI-8lZ1B2SvxNuGbyU1%40thread.tacv2/General?groupId=1c1528d7-030e-48eb-92cf-dc0f6a618ea0&tenantId=50f6071f-bbfe-401a-8803-673748e629e2) page (internal to NHSD). 

We maintain a list of people who are willing to dedicate some time to support others. Please add your name to the mix if you are willing to support someone else. You don't need to be an expert - just willing to share what you know. 


## Tutorials and resources
As we work alongside teams, we try to produce reusable learning materials pitched at specifically supporting NHSD teams. We try (with partial success) to avoid reproducing guidance that is easily available online. Instead, we link to lots of external resources where you can self-serve. Our focus instead aims to create some bespoke guidance that lays out how you would accomplish these practices in the NHSD setting.

Each of the folders has its own README to explain the content:
* [General development practices](development-approach/)
* [Python resources](python/)
* [Pyspark resources](pyspark/)
* [RAP rollout strategy notes](./rollout-approach/)

We also have a minimal Python RAP package template and it's freely available to use via Github: [RAP package template](https://github.com/NHSDigital/rap-package-template).

These resources are demand-driven so if you want something then please raise an issue on the repo or ask on the [MS Teams page](https://teams.microsoft.com/l/channel/19%3aEnoJ_c3NIwcWaLoqHyrbmiui8SI-8lZ1B2SvxNuGbyU1%40thread.tacv2/General?groupId=1c1528d7-030e-48eb-92cf-dc0f6a618ea0&tenantId=50f6071f-bbfe-401a-8803-673748e629e2). We would also ask you to contribute if you can improve on any of the resources or can fill in any other gaps. 

The resources are not intended to be prescriptive. There are many ways to accomplish a task and teams have valid reasons for choosing other approaches. Instead the intention of the resources provided here is to offer a way in for teams who want to adopt good practices that they have heard about but don't know where to start.


## External links
Here is a good [high-level overview of RAP](https://dataingovernment.blog.gov.uk/2017/03/27/reproducible-analytical-pipeline/). It explains the context of RAP in government statistics and gives some history to the work. 

The GSS have produced a list of the [benefits that come from RAP](https://gss.civilservice.gov.uk/reproducible-analytical-pipelines/benefits-to-government-from-reproducible-analytical-pipelines/).

The [ONS best practice team have a useful website](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html) covering many of the same topics we cover here. Their [best-practice checklist](https://best-practice-and-impact.github.io/qa-of-code-guidance/checklist_higher.html)  is particularly useful.

The Statistics Authority has published this excellent report on [overcoming barriers to RAP adoption](https://osr.statisticsauthority.gov.uk/publication/reproducible-analytical-pipelines-overcoming-barriers-to-adoption/).

The [AQUA book of analytical standards](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government).

The Turing Institute has published [The Turing Way handbook to reproducible, ethical and collaborative data science](https://the-turing-way.netlify.app/welcome.html)

There are several slack channels that discuss RAP and related topics: the [govdatascience.slack.com RAP channel](https://govdatascience.slack.com/archives/C6H22U3H9), the [NHS-R community](nhsrcommunity.slack.com), and the [NHS-pycom community](nhs-pycom.slack.com)

Alston, J. M., and Rick, J. A.. 2020. A Beginner's Guide to Conducting Reproducible Research. Bull Ecol Soc Am 102(2):e01801. https://doi.org/10.1002/bes2.1801

The GSS training portal offers an [Introduction to RAP course](https://gss.civilservice.gov.uk/training/introduction-to-reproducible-analytical-pipelines-rap/)



## Misc
We have taken inspiration from the [NHSD software engineering COP](https://github.com/NHSDigital/software-engineering-quality-framework/blob/master/insights/review.md). It has tons of great material so I encourage you to read and reflect on these working practices.

## Licence
RAP Community of Practice codebase is released under the MIT License.

The documentation is © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

