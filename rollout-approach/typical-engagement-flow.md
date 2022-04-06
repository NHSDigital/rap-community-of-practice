Many people ask about what a typical engagement with the RAP team might look like. Since every team is different and since the service is still in a formative state, there is no really typical engagement. 

Nevertheless, the text below lays out the type of activities that occur in across the engagement. The approach described is the [support model](./support-models.md#1-rap-team-leads-development) where the RAP team leads the development as this is our most frequent approach. 

## Initial outreach

- Hear about RAP through show-and-tells, internal advertising, slack, etc.
- Have a look over the [RAP Community of Practice](https://github.com/NHSDigital/rap-community-of-practice) pages to get a sense of what it is all about.
- Reach out to the [RAP team](mailto:datascience@nhs.net) for a chat
- Together with someone from the RAP team, walk through the [levels of RAP](../what-is-RAP.md#levels-of-rap) page and consider the team's scale of ambition.

- If you are keen to proceed, pass the request to the RAP product owner for prioritisation and resourcing
- Get a start date in the calendar. Think about publication timing, team capacity, etc. to choose a good time. 


## Setting the foundation
- Identify a publication/product that needs taking through RAP process
- Identify people in the publication team who will learn RAP process (PO and min 2 analysts)
- Identify people in the RAP team to support the publication team through RAP transition
- Set up a Jira board for tracking work and confluence space for documenting learning, agreed decisions
- Teams meet and ice breaker session to get to know each other. Set out the plan for the engagement, review roles and responsibilities, lessons learned from previous projects, etc. 


## Getting stuck in
- Pair up analysts from publication and RAP teams. These coding buddies will work collaboratively for the rest of the project. 
- Identify the ['thin slice'](./thin-slice-strategy.md) of the publication that we will aim to replicate in the first phase.
- Identify training needs of the publication team through conversations
- Dedicated training. The content is tailored to the specific team but a typical sequence might look like:
    - [Concept of a thin slice and how to choose the thin slice](./thin-slice-strategy.md)
    - Access to off-the-shelf interactive training for self-led training
    - [Pyspark style guide](../pyspark/pyspark-style-guide.md)
    - [Version control](../development-approach/02_using-git-collaboratively.md)
    - [Writing good functions](../python/python-functions.md)
    - [Unit tests](../development-approach/04_unit-tests.md)

- Buddy pairs work to replicate the thin slide outputs
- Set up automated code testing once the numbers are correct
- Group code review of buddy pair code as a learning exercise
- Decide how to structure code for publication as a whole
- Portion out the rest of the publication to be replicated i.e. geographical breakdowns
- Each analyst takes a portion at a time working independently to produce using RAP standards seeking buddy support as needed
- Set up QA and RS checks pre-publication

## Being transparent
- Publish code on github
- Add a link to the code repository in the publication and a link to the publication in the code repository
- Show and tell in NHS D on what we have learned, documents added to github

## Close-down
- Do a review with the RAP team to confirm that we've met all the elements of baseline RAP (or silver/gold)
- Do a user-research session with the RAP team to suggest improvements to the service for those who come later
- Take some time to reflect on the process internally as a team and consider how you plan to take forward the work.