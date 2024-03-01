---
title: Code review

tags: 
  - Code reviews
  - Workflow
---

#

[![link to code quality comic image](https://imgs.xkcd.com/comics/code_quality.png)](https://xkcd.com/1513)

## Why should I care?

Code review is one of the most important practices that a team can adopt. The benefits include:

- Ensuring the overall code health of the codebase is improving over time.
- Sharing knowledge and building skill across the team.
- Reducing turnover risk by gradually making the team familiar with all aspects of the code.
- Reduce the likelihood of breaking the code by making sure a second pair of eyes has checked.

## Questions to ask during code review

- Does the code work as expected?
- Does the work actually meet the acceptance criteria in the user story?
- Is the code well structured or would it benefit from redesign/refactoring?
- Could the code be made simpler? Is this level of complexity justified?
- Would another developer be able to easily understand and use this code when they come across it in the future?
- Does the code include appropriate tests?
- Does the code follow our style guides?

These questions are not intended to be comprehensive but rather to give you a starting point for the discussion.

## Other considerations

- Code should be reviewed with someone _after_ submitting a merge request and _before_ merging to the destination branch. The reviewer should consider whether the code needs to be refactored or redesigned.

- Code review is not about more experienced people telling others what to do. Code review should be
  reviewed by everyone in the team - that is how we develop together. In fact, you will often get
  more benefit from a situation where a less experienced analyst reviews the code of a more experienced
  person.

- Be kind. The process is intended to be a constructive dialogue where both parties leave more knowledgable than they began. Your discussion will be most effective if undertaken in the spirit of collaboration, not criticism.

- Code review takes time. You should ensure your sprint planning gives this important process the time it deserves.

- You should expect that code review will lead to several requests for changes. A key point here is that there is no such thing as “perfect” code — there is only better code. Reviewers should not require the author to polish every tiny piece of a merge request before granting approval. Rather, the reviewer should balance the need to make forward progress compared to the importance of the changes they are suggesting. Instead of seeking perfection, what a reviewer should seek is continuous improvement.

## Quality assurance checklist

This checklist from the ONS best practice team might be a useful guide for thinking about code review: [Quality assurance checklist for analysis and research guidance](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html). You do not need to tick every box but rather use them as a prompt.
You can also view our own checklist in the [Quality Assuring Analytical Outputs][1] file.

## External links

- [Atlassian Code Reviews](https://www.atlassian.com/agile/software-development/code-reviews)

[1]: ./quality-assuring-analytical-outputs.md
