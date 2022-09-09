# Thin-slice strategy for building RAP pipelines

The RAP team at NHS Digital often adopts a 'thin-slice' strategy when we work with teams to migrate legacy pipelines. This guide explains the rationale behind the approach and gives a rough outline of how it plays out in practice

This approach is inspired by DevOps practices in software development where rather than tackling the whole project at once, you build the smallest possible bit of functionality end-to-end.

By building something end-to-end you get a lot of benefits:

- You get to quickly demonstrate progress - good for morale and convincing leaders to keep the project going

- You get to identify major problems at the beginning of the project - e.g. the database doesn't work or the firewall is blocking access. By uncovering these things early you are more likely to be able to solve them and avoid unpleasant surprises right before the end

- You get to understand the shape of the problem. When you first start on a project, you don't know what you are doing. If you work through the project in a linear sequence - then you finally understand how all the parts fit together right at the very end. That leads to poor design. By building something end-to-end you can see how all the parts fit together and make radical improvements and iterations at very low cost.

This strategy is particularly relevant for the work we are trying to do here. We are trying to achieve a number of competing goals and the thin-slice helps us to mediate between them. For example:

| Goal                                                  | Solution                                                                                         | Consequence                                                                                                                                                             |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| We want to build this pipeline as quickly as possible | Accept the most basic code that is functional despite lower code quality                         | Code will be more difficult to run and maintain. Risk that [tech debt](https://en.wikipedia.org/wiki/Technical_debt) may snowball until BAU delivery becomes impossible |
| We want to build the best possible pipeline           | Hire a team of external specialists to do it for us                                              | Risk that the team becomes demotivated or does not understand the code                                                                                                  |
| We want to train our analysts to write good code      | Give analysts lots of defended time away from their day job with high-quality in-person training | BAU delivery will slow down. May not be possible given resource constraints                                                                                             |

Depending on which of these you want to prioritise - do it quickly, do it well, or build capacity - you would take an entirely different approach. All three are valid but each entails negative consequences that need to be acknowledged.

---

## Thin-slice pipeline

In reality, we want some strategy that enables us to mediate between these competing demands to achieve all three outcomes - a high-quality pipeline that is developed quickly and with analysts feeling like they have improved their skills each time.

The thin-slice strategy is the best way I've come up with to do this. It fits well with the support model the RAP team offers - where we work alongside a team who understand the data well. The typical workflow looks something like this:

1.  **Minimal outputs.** We identify some minimal outputs that we will try to replicate for the thin-slice. For example, we will reproduce the national numerator and denominator for one measure.

2.  **Reverse engineer the process.** We look at the existing code and work backwards to identify the minimal input data needed to calculate those outputs.

3.  **Replicate the target outputs.** We try to replicate those outputs as quickly as possible. At this phase we don't focus on code quality. Instead, we try to understand the logic of the process. The goal is just to recreate those numbers. Since we are only dealing with a small subset of the overall publication, we avoid getting totally swamped in complexity. Nevertheless - even this simplified thin-slice can be a substantial challenge. This phase forces us to grapple with a lot of the complexities of the process - e.g., funny joins, complex derivations, or logic that is spread across multiple sections of code. This is the most uncertain part of the process - but that is the whole point. We want to tackle the hard stuff up front.

4.  **Refactor and improve.**
    Once we can accurately calculate the target outputs, we move into a more interesting, iterative mode. We step back and review the end-to-end data flow. We ask ourselves how it can be simplified or reorganised to be easier to maintain. We look for sections of code that could be made into reusable functions. We set up unit tests and regression tests where appropriate. We discuss on style and naming conventions. Eventually the whole team converges on a consensus.

    - This **design phase** is iterative. We might review and improve the code several times before we decide to move forward. We often draw the analogy with writing the text for a publication. You would not publish the first draft of your publication - instead you go through several rounds of review and rewriting. Why would we treat our code any differently?

    - In short - we give ourselves the time and space to make this thin-slice as good as we can possibly make it. Because this is such a small sliver of the overall project, it does not take long to make these improvements. Usually you only need to change a tens of lines of code rather than thousands.

    - By doing this design phase collaboratively, we gain a few very important benefits:

        - First, it gives both teams a chance to contribute different elements. The publication team bring an expert understanding why the process works a certain way while the RAP team bring experience of similar processes across multiple projects.
        - Next, because the publication team is actively contributing to overall design decisions, they end up owning the code. They understand every decision that went into the final makeup of the code. This is totally different to the situation where a super-advanced coder writes some opaque, complex code and then just throws it over the fence. In that situation you are terrified to change anything in case you break it.
        - Finally, because we all do this together, we emerge from this process with a shared understanding of how we are going to write code.

    - Once our improvements to the thin-slice pipeline start to tail off, we should think about how we expand the thin-slice to include all of the other fields and breakdowns in the publication.

5.  **Scaling out from the thin-slice.**
    We now move out of the thin-slice phase to start building out the rest of the pipeline/publication. We try to choose the next fields strategically. E.g., we tackle a breakdown (a group-by) next, then a complex derived field, and then a field that requires joining some reference data. Again - the goal is to drive out any tricky bits as early in the process as possible.

    Once we are sure that the whole team is working effectively, we add each of the remaining fields and breakdowns to the backlog. Analysts pick up these tickets and tackle them in sequence.

    The tickets are considered complete when the new field gives the same outputs as the historic outputs and when another analyst has completed peer review on the code.

    This phase tends to go remarkably quickly. This is because (1) we already tackled all the hard bits up front and (2) everyone is working from a high-quality template - the thin-slice code. This is also a really good phase for cementing the learning in the team since now each person is working individually but repeating the same logic multiple times as they add lots of fields.

---

## FAQs

- What is the difference between a 'thin-slice' and an MVP?

  - The thin-slice is the minimal piece of functionality that allows us to build an end-to-end pipeline. This early phase of development is helpful for training a team and improving code quality. The thin-slice is therefore motivated by helping the delivery team to deliver effectively. It does not represent something to be delivered to customers.

    By contrast, a minimal viable product (MVP) is the most basic thing that a team could deliver to customers. MVP has a really peculiar meaning in the context of a pipeline migration since the 'minimal' thing to be delivered will typically be the full publication.

- What happens if rebuilding the pipeline uncovers errors in the existing pipeline (and hence published statistics)?

  - It is a near certainty that some minor errors will be discovered as part of any migration. This is particularly the case for building RAP pipelines since you are adding additional tests and safeguards to spot errors.

    We consider this a natural and important opportunity to improve the publication. We sit down with the team and discuss where the issue may have arisen and how we can prevent it in the future.

    Likewise, if there is an opportunity to make a substantial improvement to an existing publication we address that in collaboration with the team. We do not hold too tight to the idea of replicating historical outputs but instead aim for a pragmatic approach.

- What happens if we discover more problems after we have moved out of the thin-slice phase?

  - You will almost certainly discover more problems after the thin-slice phase. Hopefully the high code quality that comes from the thin-slice phase will make it more easy to resolve the problem, e.g., by refactoring the code.

- How would this strategy work in a situation where you were working on a brand new project, rather than migrating a legacy pipeline?

  - The same logic would apply. By identifying a very small piece of functionality and trying to implement it end-to-end, you will get a better sense of the problem.
