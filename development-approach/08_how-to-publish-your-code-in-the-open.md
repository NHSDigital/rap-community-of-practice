## Why publish your code?
The Government's [Digital Service Standard](https://www.gov.uk/service-manual/service-standard) 12th principle states that all publicly funded code should be open, reusable and available under appropriate licences. The main benefits of publishing your code are:
* It increases transparency on NHS work. This can include publication/dashboard methodologies, but also code ownership.
* It increases collaboration and knowledge sharing across cross-department teams, external users and developers. No time is wasted on requesting permissions or access to code repositories.
* Easier to share and align on standards across the health sector.
* Knowing that your code will be published will lead to your overall code health increasing as analysts and developers will take greater care in ensuring best coding practices and standards are applied.
* Reduce burden by sharing and reusing code. Internal and external users can learn from your code repositories and templates, and apply it to their work or personal projects.

The Goverment Digital Service released an **[informative video](https://www.youtube.com/watch?v=aqFFCvjXr1s)** on the benefits of coding in the open, from the start of a project.

## Analytical leadership commitment to RAP code publishing
Releasing code externally is part of the RAP project, the targets below are agreed by the analytical leadership. The set goal of publishing open code as a standard is October 2023.

% of publications on RAP
| Month |  Published code |
| --- | --- |
| Jan-22 | 0% |
| Apr-22 | 5% |
| Jul-22 | 10% |
| Oct-22 | 20% |
| Jan-23 | 40% |
| Apr-23 | 60% |
| Jul-23 | 80% |
| Oct-23 | 100% |

## How to prepare your code and repository
Coding in the Open is an internal process of NHSD's Analytics Service team to implement the Data Services Strategy where we want to open our data and source code to enhance knowledge sharing and code reusability. We have designed a process that will guide teams from the start of a project through its core development, its publishing assurance phase and reaching the final step "Publish code on NHSD Github repository". The process in place will ensure **no sensitive data or algorithms** will be published, removing any risks associated with any type of sensitive information being released.

Projects and publications with the aim to be published should follow the **Fit-for-publishing Main Diagram workflow**:

![](../images/Main_diagram_merged.png)

The first part of the workflow covers the initiation of the project, from its design phase throughout its **Core Development** phase. After designing and developing the source code on NHSD's internal Gitlab platform, you should ensure at this step that your repository, code and tests are all set and ready for external review, having addressed any security concerns. After receiving Senior manager approval, at this point the process design leaves the **Code Development** phase and enters the **Publishing Assurance** phase.

At the beginning of this phase a **snapshot** of the project's repository is taken (download the zip file of the branch) or a separate Gitlab branch is created for the review. The purpose of the snapshot is to remove all repository history and previous commits.

After creating the snapshot, the next step is to apply the **Fit-for-publishing checklist**:
### Fit for publishing checklist
This checklist covers the review process in place to ensure that the code is: 
1. Fit for purpose 
2. Well documented 
3. No credentials or personally identifiable information left in the repository
4. No data should be stored in the snapshot.  

To access the checklist click on the link below and select the Download option:
* [Repository validation checklist](https://github.com/NHSDigital/rap-community-of-practice/blob/main/images/Fit_for_publishing_checklist.docx)

For each subsection of the checklist an **internal reviewer** is assigned by the development team to check and add comments and suggestions to be impletemented. Once those are reviewed and implemented the checklist is passed on to an **external reviewer** (outside of the development team) to carry out checks and add any comments and suggestions in the external review columns. Once the external review is complete, each checklist section is assigned a **RAG status** by the lead analyst.

Once the repository is granted the **final confirmation** for publishing from a Senior Manager (as per the **Main Diagram** workflow shown above), you can then proceed to the final step, which is going **live** with your Github repository on the [NHS Digital public repository](https://github.com/NHSDigital).

**Please note:** Should the workflow at any point reach to a failed step, follow the ```No``` direction to be steered towards the revision and reiteration steps.

### Fit for publishing checklist example
Here's an **example** of the NDA RAP checklist that was applied to the repository's snapshot: [NDA RAP checklist] and the [NDA RAP Github repo](https://github.com/NHSDigital/national-diabetes-audit).

## Further reading
* [Sharing Code in the Open by NHSX](https://nhsx.github.io/AnalyticsUnit/codeintheopen.html)
* [Be open and use open source](https://www.gov.uk/guidance/be-open-and-use-open-source)
* [The benefits of coding in the open](https://gds.blog.gov.uk/2017/09/04/the-benefits-of-coding-in-the-open/)
* [Open source repositories by the Government Digital Service](https://github.com/alphagov)
