# What does government policy say about RAP?

!!! tip "TLDR"
    - RAP is not just a good idea - it's fast becoming the **required** way of working with data
    - The government, the Civil Service, and the NHS have all released documents pushing for the RAP way of working
    - These include The Goldacre Report, Data Saves Lives, and the Civil Service RAP Strategy
    
??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[What is RAP?](what_is_RAP.md)|Helpful|Knowledge of RAP principles will help you understand why the government is pushing for it|

![Image showing a military officer pointing at you. The caption reads: "YOUR COUNTRY NEEDS YOU - TO RAP"](../images/your-country-needs-you-to-rap.jpg)
{: .align-centre}

The government wants you to adopt RAP principles in your analytical work.

This is highlighted in a number of policy, strategy, review, and other documents pushing for the use of RAP in the UK public sector.

Read on to find out how RAP is not just a good idea - it's fast becoming the **required** way of working with data.

## The Goldacre review

[Better, broader, safer: using health data for research and analysis](https://www.gov.uk/government/publications/better-broader-safer-using-health-data-for-research-and-analysis/better-broader-safer-using-health-data-for-research-and-analysis) aka "The Goldacre Review" is a 2022 report led by Prof. Ben Goldacre, offering guidance on how the NHS can better use, manage, store, and access its data. The 220-page report urges the adoption of RAP working principles, and offers detailed recommendations on how to do so. The report was fully supported by the Secretary of State for Health.

**Key quotes:**

The NHS can and should rapidly adopt RAP working practices, both for service analysis and for research.
{: .pquote .pquote--blue .pquote--inline .pquote--serif}

- The principles of RAP are excellent, well thought through, and reflect a strong basic **minimum standard**.
- Promote and resource “Reproducible Analytical Pipelines” (RAP, a set of best practices and training created in GDS and ONS) as the minimum standard for academic and NHS data analysis.
- Data Controllers should require RAP and open code sharing from data users.
- TREs (Trusted Research Environments) themselves should be built on principles of RAP and open code.

## Parliamentary Questions

On 10 May 2022, Labour MP for Newcastle Upon Tyne Central [tabled a written question for parliament](https://questions-statements.parliament.uk/written-questions/detail/2022-05-10/243) on the use of RAP to the Department of Health and Social Care:

*"To ask the Secretary of State for Health and Social Care, what steps he taking to promote and resource reproducible analytical pipelines as the minimum standard for academic and NHS data analysis, as recommended in the Goldacre review."*

The question was answered on 24 May 2022 by Gillian Keegan, Conservative MP for Chichester, who replied:

*"We are currently considering the recommendations of the Goldacre review. However, many of the review’s recommendations are aligned with existing programmes, such as facilitating Reproducible Analytical Pipelines (RAP) within the National Health Service and promoting RAP through NHS analyst communities."*

![Screenshot of a parliamentary question in which Chi Onwurah, Labour MP for Newcastle Upon Tyne Central asks "To ask the Secretary of State for Health and Social Care, what steps he taking to promote and resource reproducible analytical pipelines as the minimum standard for academic and NHS data analysis, as recommended in the Goldacre review." The reply from Gillian Keegan, Conservative MP for Chichester was: "We are currently considering the recommendations of the Goldacre review. However, many of the review’s recommendations are aligned with existing programmes, such as facilitating Reproducible Analytical Pipelines (RAP) within the National Health Service and promoting RAP through NHS analyst communities." ](../images/chi-onwurah-pmq-rap.png){width="650"}
{: .align-centre}

## Data saves lives

[Data saves lives: reshaping health and social care with data](https://www.gov.uk/government/publications/data-saves-lives-reshaping-health-and-social-care-with-data/data-saves-lives-reshaping-health-and-social-care-with-data), is a policy document released in 2022 laying out the government's plan to use data in healthcare.

**Key quotes:**

Recommendation 7: promote and resource ‘Reproducible Analytical Pathways’ (RAP, a set of best practices and training created in ONS) as the minimum standard for academic and NHS data analysis
{: .pquote .pquote--blue .pquote--inline .pquote--serif}

- ...we will explore the impact and benefits of modern, open working methods of data management and analysis such as Reproducible Analytical Pipelines (RAPs), which is particularly recommended by the Goldacre review
- As we foster an increasingly open culture, **we will progressively ask for more open-source ways of working** in our procurement and contracts, with clear policies that build towards open by default across the NHS.
- We will begin to make new source code that we produce or commission **open and reusable by default** (with clear exceptions) and publish it under appropriate licences to encourage further innovation
- All accredited NHS secure data environments must adhere to a policy of open-working, support code-sharing and facilitate use of technology that supports this, such as RAPs.
- Recommendation 17: embrace modern, open working methods for NHS data analysis by **committing to Reproducible Analytical Pipelines (RAP) as the core working practice** that must be supported by all platforms and teams; make this a core focus of NHS analyst training.

## Secure Data Environment policy guidelines

The [Secure data environment for NHS health and social care data](https://www.gov.uk/government/publications/secure-data-environment-policy-guidelines/secure-data-environment-for-nhs-health-and-social-care-data-policy-guidelines) policy guidelines expand on the recommendations made in Data Saves Lives pertaining to how secure data environments should be implemented. It includes RAP in its definition of the "Five Safes" - specifically under Safe Projects, as publishing our code is needed for the public to understand how we're using their data.

**Key quotes:**

Code developed in secure data environments must be published in the open unless there is a specific rationale for not doing so.
{: .pquote .pquote--blue .pquote--inline .pquote--serif}

- Secure data environments must support open working, ensuring that code developed in these environments is reusable [for example] using the Reproducible Analytical Pipelines (RAP) strategy.

## Civil service RAP strategy

The Civil Service RAP team produced a [strategy report](https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/) outlining why and how government departments should adopt RAP working principles.

**Key quotes:**

Embedding RAP as the default approach to analysis in government is an essential step on the way to digital transformation of analysis.
{: .pquote .pquote--blue .pquote--inline .pquote--serif}

- ...we know that giving analysts the capability needed for RAP **improves efficiency** and the **quality** of their products.
- We have shown that RAP delivers improved efficiency and quality for analysis. RAP forms a core part of digital transformation and supports the delivery of other government initiatives.

## Government open source guidance

One of the key RAP principles is transparency - sharing and reusing code. This speeds up the development of analytical processes, as you're not continually reinventing the wheel. If an existing solution exists elsewhere, why write one again from scratch?

In 2017, the government released guidance on this in a document called [When code should be open or closed](https://www.gov.uk/government/publications/open-source-guidance/when-code-should-be-open-or-closed). Spoiler alert: it should almost always be open.

**Key quotes:**

- You should keep some data and code closed, including: keys and credentials, algorithms used to detect fraud, unreleased policy.
- **You should open all other code.**

## Proposed NHS open source policy

Colleagues in the NHS created a [proposed policy](https://github.com/nhsx/open-source-policy/blob/main/open-source-policy.md) to inform why, how and when staff across NHS England should publish their code openly.

**Key quotes:**

All new source code that we produce or commission should be open and reusable by default: such that anyone can freely access, use, modify, and share the relevant code for any purpose.
{: .pquote .pquote--blue .pquote--inline .pquote--serif}

- It is almost impossible for staff across the NHS to communicate either best practice or effective solutions to common problems without a framework in place. Open source code offers that framework.
- Any open code can be reused by our developers to **reduce costs**, avoid duplication of effort, generally **increase staff efficiency**, make system changes more quickly and pursue the best approaches, not just those locally available.
