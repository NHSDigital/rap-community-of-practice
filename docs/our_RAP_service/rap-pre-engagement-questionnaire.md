---
title: RAP Pre-engagement Questionnaire

tags: 
  - Preparing for RAP
  - RAP engagements
---

#

!!! tip "TLDR"
    - These questions will help you plan out your RAP engagement.
    - They focus on what the current situation is, what needs doing, why, and when it will be classed as done.

??? question "Why should we care?"
    - By thoroughly scoping out a piece of work, prior to starting, it might identify potential pitfalls, or opportunities.
    - This document should help RAP champions set expectations, especially when "disengaging" at the end of an engagement.

??? success "Pre-requisites"
    * Some information on what someone might need to be familiar with before they can use this page

    | Pre-requisite                                            | Importance | Note                                                                                      |
    |----------------------------------------------------------|------------|-------------------------------------------------------------------------------------------|
    | [Levels of RAP](../introduction_to_RAP/levels_of_RAP.md) | Necessary  | Knowing the levels of RAP allows you to understand what to aim for                        |
    | [Building Team Capability](building_team_capability.md)  | Helpful    | Provides context for this checklist: what your team will need to do RAP                   |
    | [Support Models](support-models.md)                      | Helpful    | Helps you understand the different ways in which RAP champions can help analysts do RAP   |
    | [Typical Engagement Flow](typical-engagement-flow.md)    | Helpful    | An example of how an engagement might go - might help RAP champions to plan out their own |
    | [Thin Slice Strategy](thin-slice-strategy.md)            | Helpful    | Describes how to take an existing pipeline and remake it into a RAP                       |

This is checklist is aimed at **helping RAP Champions plan out an engagement with a team** to help them make a RAP pipeline.

It's a good idea to go through this checklist with the subject matter experts of the pipeline which needs transforming, so that there are fewer surprises further down the line.

**Before diving into RAP**, it's highly recommended that colleagues familiarise themselves the [elements of baseline RAP](..//introduction_to_RAP/levels_of_RAP.md), and do some introductory training - this will mean any engagement will be far more efficient.

!!! note
    See [Thin slice Strategy](thin-slice-strategy.md) and [Typical Engagement Flow](typical-engagement-flow.md) for more information on how to do engagements, [support models](support-models.md) for to resource and the trade-offs involved in RAP engagements.


| **Theme**            | **Sub-theme**     | **Question**                                                                                                      | **Tips**                                                                                                                            |
|----------------------|-------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Overall**          | **Start point**   | What situation are we starting with?                                                                              | How does the current process work, at the high level.                                                                               |
|                      | **Aim**           | What is the end goal?                                                                                             | Examples include they want to get it to baseline, and train up their team                                                           |
|                      | **"The ask"**     | What do they need from us?                                                                                        | That is, why can't they do the above themselves? not enough resources, not enough skills?                                           |
|                      | **Shutdown**      | Who would own this once the project is over?                                                                      | Good to get an idea of this right at the start - so handover is considered from day 1.                                              |
|                      |                   | What is the plan for ongoing support?                                                                             | For example, follow up / drop-in sessions? Analysts will hit snags after the engagements - they need to know where to turn for help |
| **Engagement model** |                   | Which type of [support model](support-models.md)? (for example, RAP team leads, analyst team leads, RAP champion) |                                                                                                                                     |
| **Resource**         | **RAP Champions** | Who?                                                                                                              | Which of your available RAP champions will be working on this? How will they balance this alongside any other commitments?          |
|                      |                   | For how long?                                                                                                     | For how long? A default time period for engagements is 2 months, but they might need to be shorter or longer.                       |
|                      | **Analyst team**  | Who?                                                                                                              | who will be working on this project?                                                                                                |
|            |  | What is their FTE availability and for what period of time, for instance 2 months? | 
|  |  | What is the level of technical skills and experience in the analyst team? | This should be related to the technology of choice (Python, SQL, and so on) |
|  |  | If pre-engagement training, who, when and for how ? |
|  |  | How well do the team understand the process which needs RAPifying?  | For example, do they have a diagram which shows the major steps? Are technical details of those understood? Are there any black boxes? |
|  | | What happens after the engagement finishes? | (Hint: hopefully they will train others and make more pipelines |
| | | Pair programming? | [Pair programming](https://www.techtarget.com/searchsoftwarequality/definition/Pair-programming#:~:text=Pair%20programming%20is%20an%20Agile,code%20and%20test%20user%20stories.) means two people working together on one task. This sounds wasteful, but can result in better code being written, and more learning taking place.|
|  | **Both**  | Upcoming deadlines for non-RAP stuff? | Other deadlines might derail the RAP work - so good to know about them |
| **Support from other teams** | **Data Management** | Is the pipeline that makes the "base asset" trusted and assured? | The RAP will consume and build on the "base asset" table - if this isn't assured, then the RAP outputs won't be assured. |
| | | Do we have access to data management SMEs? |
| | **Information Asset Owners** | Good to know who these people are in case there are any issues with the data, or if more info is needed on its providence, use, etc. | |
| **Existing pipeline / publication** | **Access** | What is needed to get access to any of the required data, storage and systems? | We need to arrange access promptly. |
| | | Any other access requirements? | Such as network drives, fileshares, gitlab repos, etc. |
| | **Information governance** | What direction is this done under? Which Unified Register asset numbers are used? | |
| | **Platform** | Which analytical environment are they using? | We need to know what tools and setup they're using. |
| | | Longevity of the Platform? | Is this platform sticking around? Is there a more future proof one you could use? |
| | | Plan in place for future moves to new analytical environments? | Have they thought what will happen when eventually the current environment is replaced? |
| | **Outputs** | Excel outputs, CSVs (do they follow [Open Data Standards for CSVs](https://github.com/NHSDigital/open-data-standards)? | This is important for consistency, to allow easier reuse|
| | **Existing Work** | **Any other RAP pipelines in the team?** 	| These can act as a useful template. |
| | | **Can the [RAP package template](https://github.com/NHSDigital/rap-package-template) be used?** 	| This is a great starting point to ensure your work is consistent with that of your colleagues. |
| | **[Thin slice](./thin-slice-strategy.md)** | What will the measures and breakdowns (if applicable!) be? Or otherwise, how could you chunk up the work into the thin slice approach? | |           	|

## Further Reading

- [Are you ready for RAP?](../implementing_RAP/rap-readiness.md)
