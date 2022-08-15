# Development approach

This directory holds resources relevant to writing good code in any language. 

Adopting **version control** is the single most important improvement that most analytical teams can make. This is a hard thing to do as a team but the effort pays off in a multitude of ways. We have two guides - the first explains the basics of using git while the second offers a real life explanation for how you might use it as a team. 

* [Learn about the basics of git](01_intro-to-git.md)

* [Learn how to use git collaboratively in your team](02_using-git-collaboratively.md)


**Quality assurance** is a big and complex topic. This guide distills the activities listed in both the Aqua book and the 'Duck book' to give a template you can adapt for your own project. 

* [Learn about creating the QA plan for your RAP project](03_quality-assuring-analytical-ouputs.md)


The next two guides talk about **testing**. Writing tests can initially seem like more work but the effort pays for itself in time saved debugging. The second guide offers a particularly useful way of deriving fields (columns) that can help in situations where there are a lot of changes to the specifications.

* [Learn how to design and write unit tests](04_unit-tests.md)

* [Learn about how to write and test field definitions in a way that is easy to understand and maintain](05_unit-testing-field-definitions.md)

Adopting inconsistent data formats leads to a huge amount of wasted effort and can actually lead to very complex code. By adopting **tidy data format** for your work you can both improve your service to users and simplify your own production pipeline. 

* [Learn how tidy data can help teams to use a consistent format](06_tidy-data.md)

Another topic we encounter frequently is the question of **when to use Jupyter notebooks**. These can be really helpful for exploratory work but also have some serious problems. This guide talks through the situations when you might use notebooks versus standard development tools. 

* [Learn about the difference between using notebooks vs IDEs](07_notebooks_versus_ide_development.md)

In NHS Digital we have committed to publishing more and more of our code over time to **improve the transparency** of our analytical work. We have a process in place to publish code safely. 

* [Learn how to publish your code in the open](08_how-to-publish-your-code-in-the-open.md)

One of the most effective practices for quickly improving the capability of a team is **code review**. 

* [Learn how to do effective code review to build capability in your team](./09_code-review.md)

* [Learn how to test that your new pipeline produces the same outputs as your historical code](./10_backtesting.md)