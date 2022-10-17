# Ready for RAP?

RAPs' yield long-term benefits for the teams that use them. They are robust against errors, staff turnover, and changing outputs; they reduce human effort, computing time, and complexity; they save money through using open-source software, increasing re-usability, and lowering resource requirements.

All of this said, they take a considerable amount of planning and effort up front. When setting out on your RAP building journey, it is very important to make sure that you have the right resources in place, that you have a clear plan, and that you have ample time to both build and deploy your new RAP.

This page aims to serve as a guide for helping you in making these plans and decisions. Below, we have detailed some of the areas which you ought to plan around, and some of the topics within these which are worth considering.

## Skills

Engaging in RAP and re-designing a project will be a learning experience, and significantly upskill your team - but the process will also be made much easier by attaining a minimum level of proficiency before embarking on the RAP project.

Here, we provide a recommended set of minimum criteria.

- [ ] A basic grounding in programming
  > We recommend the training available here: [introduction to programming](https://www.kaggle.com/learn/intro-to-programming)
- [ ] A basic grasp of the open-source languages which we intend to use
  > For Python, we recommend this training: [introduction to Python](https://www.kaggle.com/learn/python) training. For SQL, [this training](https://www.kaggle.com/learn/intro-to-sql).
- [ ] An initial grasp of git: what it is, and what its used for.
  > We provide an [introduction to git][1].

## Resources

Planning up front will make your RAP project much smoother. Here we provide a suggested list of resources which are advisable to line up before embarking on building your RAP.

- [ ] An identified platform.
  > Where will you and your team be writing code? Do you have a way of connecting this environment to the data which your project will need? And then to the destination of your publication, or otherwise? It's important to check that your intended platform can parse the language(s) you intend to write your RAP in, and that it can connect to the necessary systems (such as GitHub, or the NHSD GitLab).
- [ ] Permissions
  > Do all members of your team have the necessary permissions to access the data assets and platforms necessary for your project? **Acquiring permissions can sometimes be very slow** - it's best to try to line up all necessary permissions well before you need to begin actual coding on your project.
- [ ] Knowledge of existing tools and how to use them
  > There are many tools which have been developed for teams just like yours to work more quickly and effectively. We have a curated list of [relevant tools][2].
- [ ] A template for your project.
  > Starting your project from a template will save you a lot of time and effort. We have an [example project template](https://github.com/NHSDigital/rap-package-template) which we would recommend as a starting point.
- [ ] A reasonable amount of contingency planning
  > NHSD members can view some documentation at the 'Risks, Issues, Dependencies & Decisions Log' within the Data Science Skilled Team's confluence page.

## Time Management

Converting a project to meet RAP standards takes a significant amount of time. In the medium and long-term, using RAP's is hugely time-saving, since you will have automated so much of your workflow. But in the short term, setting up that automation is demanding. We advise that you make space for training, building, and managing your RAP project.

- [ ] Time to engage with the training resources
  > As a **very** rough ballpark estimate, expect someone with no coding experience to take ~15 hours to complete the training listed in the [skills](#skills) section; and a further ~8 hours to complete the training we provide e.g. [Python][3], [Git][4], [R][5].
- [ ] Time to create the RAP
  > Designing, coding, and testing your new pipeline is a time consuming process; especially if this is your first RAP project. We recommend making sure that a group of people are working together on this. Time commitments will, of course, depend upon the nature of the project.
- [ ] Time to continue with business as usual
  > Many teams which engage in building a RAP are doing so in order to replace something which already exists, such as a publication pipeline. **It is crucial that you plan for enough resource to continue deploying the current version of your product whilst the RAP is being developed.**
- [ ] Time for management to provide support
  > Your team management may or many not be involved in writing the code for your new RAP. Either way, there will still be significant work for them in managing surrounding issues. One example: a project we worked on had significant issues with the data being supplied; problems which were only revealed by the work of the RAP project. Addressing these issues was not part of the pipeline per se, but the team manager had to devote significant time to fixing the issue nonetheless.
- [ ] Staff availability
  > Do your team members have annual leave coming up? If so, will this create any bottle necks, i.e. for code reviewing?
- [ ] Pressures on team
  > Do you have any deadlines coming up? Will there be any particularly busy periods for your team, in which you won't be able to focus on RAP as much?

## Goals and Planning

Code can always, always be improved. How good is 'good enough' for your project? It's a good idea to set clear goals for yourself at the outset of the project. These can always be revised as you go, but it's good to have a established an established target. This will give you something clear to work towards, and will help you know when to stop developing your RAP and start deploying it. Here is a list of points to consider when setting your goals, and thinking about how your RAP will fit into your team's work going forwards.

- [ ] A target [level of RAP][6] to aim for. Typically, this ought to be baseline RAP.
- [ ] A publication or project which you're aiming to transform.
  > We advise limiting yourself to something small to begin with. It's better to complete something small than to start many things and not finish them. We have further advice about doing this in our [thin slice guide][7].
- [ ] A plan for how you will transition. Once the RAP project is ready for use, you will need to swap out the pre-RAP version for the new pipeline. This might involve, for example, giving your customers advance warning of any new formats you will be publishing data in.
- [ ] How will you put your team's new skills to use once this project is completed? Are there other projects which would benefit from RAP, and other teams you could help?
- [ ] Is the RAP community of practice something you could contribute to? Within NHSD, this is an important and growing community of data practitioners who are developing the skills and tools to deploy RAP further.
- [ ] Are any of your outputs going to change?
  > Building a new pipeline can serve as an opportunity to improve our team's outputs. For example, you could make sure that any new publications conform to the [Government Statistical Service Accessibility Guidelines](https://gss.civilservice.gov.uk/policy-store/making-analytical-publications-accessible/).

[1]: ../training_resources/git/intro-to-git.md
[2]: ./tools.md
[3]: ../training_resources/python/basic-python-data-analysis-operations.md
[4]: ../training_resources/git/intro-to-git.md
[5]: ../training_resources/R/README.md
[6]: ../introduction_to_RAP/levels_of_RAP.md
[7]: ../our_RAP_service/thin-slice-strategy.md
