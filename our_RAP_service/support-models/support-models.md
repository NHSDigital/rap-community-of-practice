---
title: RAP squad support models

tags: 
  - RAP engagements
  - RAP champions
---

#

Every team approaches RAP from a different starting position - different BAU pressures, different team make-up and coding proficiency, different delivery cadence. We have spent a lot of time trying to figure out how best to support teams to engage with RAP. One of our main take-aways is that the support model of the RAP team should be tailored to the context of the team being supported.

We often identify three competing demands for RAP projects. Each of these goals is valid but would suggest different support models:

| Goal                                                  | Solution                                                                                         | Consequence                                                                                                                                                             |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| We want to build this pipeline as quickly as possible | Accept the most basic code that is functional despite lower code quality                         | Code will be more difficult to run and maintain. Risk that [tech debt](https://en.wikipedia.org/wiki/Technical_debt) may snowball until BAU delivery becomes impossible |
| We want to build the best possible pipeline           | Hire a team of external specialists to do it for us                                              | Risk that the team becomes demotivated or does not understand the code                                                                                                  |
| We want to train our analysts to write good code      | Give analysts lots of defended time away from their day job with high-quality in-person training | BAU delivery will slow down. May not be possible given resource constraints                                                                                             |

![venn diagram](../images/venn_diagram_trade-offs.png)

_Different goals suggest different trade-offs between improvements to code, building capacity in the team, and the resourcing constraints on the RAP team_

We’ve now tried out three different models of support:

1. The RAP team provides technical leadership and training with analysts teams being mentored as part of the project
2. The RAP team provides up-front training but analyst teams lead technical development
3. A RAP champion in the analyst team provides training and technical leadership with support from RAP team

You can think of these models along a spectrum with more hands on support for model 1 and much less support in model 3. The models are described in more detail here and in the section below, some considerations that can guide which approach is best are explained.

### 1. RAP team leads development

In this model, we embedded fully with the team. The RAP team use our expertise to lead the planning and development process. We teach the team how to apply RAP practices to code through input sessions and pair coding. More than this - the analyst team adopts the working practices of the RAP team to also learn the workflow that goes along with these practices, e.g., breaking down code development into appropriately sized chunks of work for a short-lived branch.

This model has worked very well – the analyst team get very good training and the RAP team get to apply their skills to improve the quality of the pipeline.

The problem with this approach is how resource intensive it is as we might expect the RAP team to be embedded with a team for a couple of months. When we have hundreds of publications, this model doesn't scale well unless the teams then cascade their learning to others.

### 2. Analyst team leads development

An alternative approach that we have tried was to offer tailored training and pair-coding support but to leave the technical design and leadership to the analyst team.

A key benefit of this approach is the analyst team was really forced got to grapple with the code and think carefully about how to apply what they had learned from the RAP team. As a result I think they learned more effectively than would have been the case if they were shown.

Conversely, in this model the quality of the code hit a ceiling. The analyst team did an excellent job at picking up skills and applying what they had learned to the code. Nevertheless, the experience to organise an entire codebase is not something that can be taught quickly.

This outcome is peculiar - the team learned more effectively than they would have if given more guidance but also reached an upper limit sooner. One way for us to reconcile these contrasting situations would be to plan another round of engagement with the RAP team once the first round of learning has been consolidated.

The most beneficial activity we undertook in this engagement was pair-coding. Supporting each person individually allowed us to manage the very different skill levels in the team more effectively, making sure each person was learning and making valuable contributions.

### 3. RAP Champion leads with support

The third approach we have used is to identify a highly skilled individual in a team who wanted to lead on development work and then we focus our efforts on supporting that individual.

This has been a very effective approach from the perspective of the RAP team as it is much less resource intensive. By focussing our engagement, we find that we can make faster progress towards a strong code outcome.

The risk of focussing the engagement on one person is that they then assume primary responsibility for cascading the learning to the rest of the team. If they do not have time or inclination then you might end up leaving the rest of the team behind.

The other problem with this approach is that it depends on teams already having that skilled individual.

## Offering a range of support based on the team's situation

In order to choose the right support model for teams, we recommend that the team leads and RAP lead should discuss the considerations below. The discussion can frame the decision about whether to choose a support model that is more or less hands-on.

| Consideration                                      | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                             | Decision |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Prioritise training the team or improving the code | There is a tension between two outcomes of RAP - improving pipelines and training teams. The senior leadership team should make an honest, up-front decision about which to prioritise as this should guide the support model.                                                                                                                                                                                                                     |          |
| Existing development skill in the team             | We have worked with teams at different stages of their learning journey. If the team is new to modern development practices then that would lean towards a more involved engagement from the RAP team.                                                                                                                                                                                                                                             |          |
| Team morale and enthusiasm for change              | Learning and implementing change is hard. For teams where morale is low, we recommend more engagement from the RAP team.                                                                                                                                                                                                                                                                                                                           |          |
| Urgency for rebuilding the pipeline                | In situations where a pipeline is very burdensome or if there is a 'burning-platform' problem then you may choose to prioritise improving the pipeline, with team training coming later. The RAP team can work much faster to rebuild when not delivering training in parallel.                                                                                                                                                                    |          |
| Complexity of the existing pipeline                | For very complex pipelines, the RAP team will be more likely to make effective progress if they can lead development and tackle the pipeline directly. The stats team will likely learn most effectively in this scenario by following along with the refactoring process.                                                                                                                                                                         |          |
| Perceived risk of the existing pipeline            | If there have been a number of errors with a pipeline then you may want more intensive engagement from the RAP team.                                                                                                                                                                                                                                                                                                                               |          |
| Resourcing constraints on RAP team                 | We have seen that there is always more demand for RAP support than can be met. At the same time, spreading the RAP team too thin will lead to poor outcomes and consequently may risk the success of RAP overall in the organisation. You should consider carefully how many engagements the RAP team can support and prioritise publications appropriately. RAP is not a once-and-done process so it makes sense to build capacity out over time. |          |
