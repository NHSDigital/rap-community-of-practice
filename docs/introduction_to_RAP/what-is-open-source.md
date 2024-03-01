---
title: What is open source?

tags: 
  - Open-source
---

#

!!! tip "TLDR"

    - Open source programming languages are generally **free**! This means we can use them, and other analysts can easily reuse our code without the need for costly software licenses.

    - Open source programming languages and tools are widely distributed under various open source licenses - **these may have conditions which you should be aware of**.

    - Open source programming languages and tools often have vibrant and collaborative communities that provide additional libraries (extensions) and documentation (though this isn't always complete).

    - Save time and resources, avoid duplication of effort, and increase efficiency.

??? success "Pre-requisites"

    | Pre-requisite | Importance | Note |
    |---------------|------------|------|
    | [Levels of RAP] | Helpful | Open source is an essential component of Baseline RAP |

## What is an open source programming language?

Open source programming languages are not owned by anyone. They are widely available, usually maintained by a community, and are typically freely distributed under various open source licenses.

For example, [Python] is developed under an OSI-approved open source license, making it freely usable and distributable, even for commercial use. Python's license is administered by the [Python Software Foundation].

It is recommended that we align our practices with [The Technology Code of Practice]. It is a cross-government agreed standard on a set of criteria to help government design, build and buy technology. Specifically, the third point states that we should [Be open and use open source].

Producing data in an open source language is an essential component of Baseline RAP. The Baseline level is designated as the _minimum_ standard of a reproducible analytical pipeline so using an open source programming language is a good place to start adopting RAP practices.

## Why use an open source programming language?

**Licensing and distribution** - Open source programming languages are widely distributed under various open source licenses.

**Collaborative communities** - Resolve common problems using solutions from open source communities.

**Libraries and tools** - There is a vast number of useful open source libraries and tools that are easily accessible and well documented.

**Time and cost** - Open source is free to use! Additionally, code libraries and tools developed for open source programming languages can save a lot of time when writing the source code of a project and lower implementation and running costs.

## What is open source code?

Open source code is provided under a licence that means anyone can freely access, utilise, and modify the code for any purpose.

It means that regardless of who produced it, anyone can contribute to its further development or use it for their own means without paying a licensing fee, or seeking permission from the contributors.

Any open source code can be reused by our developers to reduce costs, avoid duplication of effort, and increase staff efficiency.
**By publishing your code**, and even better **[packaging up your code]**, you add to the body of open source code, **allowing someone else to benefit from your hard work**.

[How to publish your code in the open :material-cursor-default-click:][how to publish your code in the open]{ .md-button }

## Examples of open source projects

**[Splink]** - Splink is a Python package developed by the Ministry of Justice for probabilistic record linkage. It deduplicates and/or links records from datasets that lack a unique identifier. The core linkage algorithm is an implementation of Fellegi-Sunter's model of record linkage, with various customisations to improve accuracy. Check out the publication ['Splink: MoJ’s open source library for probabilistic record linkage at scale'][splink-publication] to find out more.

The package is fully open source and can be found on GitHub. It is accompanied by a set of [interactive demos] to illustrate its functionality, whereby users can run real record linking jobs in their web browser.

**[Coronavirus Dashboard][coronavirus-dashboard-github]** - Public Health England's coronavirus dashboard repository on GitHub contains the frontend source code for the [Coronavirus Dashboard]. It also contains the API service that supplies the latest data for the COVID-19 outbreak in the UK. They have also developed software development kits in several programming languages to facilitate access to the API such as the [Python SDK].

**[NHS.UK frontend]** - NHS.UK frontend contains code to start building user interfaces for NHS websites and services.

**[NHS COVID Pass Verifier]** - The NHS COVID Pass Verifier app is a secure way to scan an individual’s NHS COVID Pass and check that they have been fully vaccinated against COVID-19, had a negative test, or have recovered from COVID-19.

## Further reading

- [Be open and use open source] (GOV.UK)
- [The benefits of coding in the open] (GDS)
- [Open source policy] (NHSX)

[levels of rap]: ./levels_of_RAP.md
[python]: https://www.python.org/about/
[python software foundation]: https://www.python.org/psf-landing/
[the technology code of practice]: https://www.gov.uk/guidance/the-technology-code-of-practice
[splink]: https://github.com/moj-analytical-services/splink/
[splink-publication]: https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale
[interactive demos]: https://github.com/moj-analytical-services/splink_demos
[coronavirus-dashboard-github]: https://github.com/publichealthengland/coronavirus-dashboard
[coronavirus dashboard]: https://coronavirus.data.gov.uk/
[python sdk]: https://github.com/publichealthengland/coronavirus-dashboard-api-python-sdk
[nhs.uk frontend]: https://github.com/nhsuk/nhsuk-frontend
[nhs covid pass verifier]: https://github.com/nhsx/covid-pass-verifier
[how to publish your code in the open]: ../implementing_RAP/how-to-publish-your-code-in-the-open.md
[be open and use open source]: https://www.gov.uk/guidance/be-open-and-use-open-source
[the benefits of coding in the open]: https://gds.blog.gov.uk/2017/09/04/the-benefits-of-coding-in-the-open/
[open source policy]: https://github.com/nhsx/open-source-policy/blob/main/open-source-policy.md
[rap community of practice github]: https://github.com/NHSDigital/rap-community-of-practice/issues
[packaging up your code]: ../training_resources/python/project-structure-and-packaging.md
