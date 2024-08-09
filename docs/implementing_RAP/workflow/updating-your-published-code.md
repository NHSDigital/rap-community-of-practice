---
title: How to update your published code

tags: 
  - Publishing code
  - Transparency
---

#

## Introduction

!!! tip "TLDR"

    - Update your published code as often as you feel the need to (managers
      discretion)
    - Keep the [publishing code checklist][1] in mind, though its up
      to your manager if a full check is required
    - A **`publish` branch** and **merge requests** helps you check
      only what has changed, **saving time**
    - when approved you can move your code over to the public repo
    ([see the existing guidance][2])
    - consider using [releases][5], [semantic versioning][4] and
    [CHANGELOG.md][6]

??? question "Why should we care?"

    - Hopefully, all of our published code will be updated someday
    - on that day you might need this guidance

??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[Publishing Code in the Open][1]|Necessary|You need to have done this before, or at least understand the process|
    |[Intro to Git](../training_resources/git/introduction-to-git.md)|Necessary|There will be some use of GitHub and GitLab so knowing about Git is needed|

After you've [published your code][1] for the first time, you may go on to do subsequent additions, changes and updates to the codebase held in our internal "development" repositories. It will then be time to update the code that has been published.

!!! info "NHS England colleagues"

    See our internal confluence pages on [**"Git, GitLab and GitHub"**][3] which explains our internal setup.

This is pretty straightforward and follows the same process as described in
"[Publishing Code in the Open][1]", however hopefully the guidance here will
help you save time.

![xkcd comic update](https://imgs.xkcd.com/comics/update.png "comic showing
someone ignoring a critical update which prevents random laptop fires due
it requiring a laptop restart")

## How to do the update

If you're developing your code on a private repo (either **GitLab** or 
**Github**), it's a good idea to keep a branch on your "`development`" repo
which is **identical** to your public "`publish`" repo. This means that you can
easily see what changes there are between your published code and the "main"
branch of your development repo.

This means that when you are ready to update your published code:

**First**, in your private repo:

=== "GitHub"

    1. do a `pull-request` (a.k.a. `merge`) from your `main` branch into your 
    `publish` branch ![pull request button](../images/pull-request-button.jpg 
    "picture showing the pull request button")

    2. if required by your manager, go through the 
    "[Publishing Code in the Open][1]" process and checklist

           - focus on just the things in the `pull-request' that have
           **changed** ![files changed button](../images/pull-request-files-changed-button.jpg "picture showing the pull request files changed button")

    3. when you're happy with the changes and they have been **"approved"** in
    the `pull-request` you can move the code from `publish` branch to the
    public repo ([see the existing guidance][2])

=== "GitLab"

    1. do a `merge-request` (a.k.a. `merge`) from your `main` branch into your
    `publish` branch ![pull request button](../images/gitlab merge request button.jpg "picture showing the pull request button")

    2. if required by your manager, go through the 
    "[Publishing Code in the Open][1]" process and checklist

           - focus on just the things in the `merge-request' that have **changed**
           ![files changed button](../images/gitlab merge request changes button.jpg "picture showing the pull request files changed button")

    3. when you're happy with the changes and they have been **"approved"** in the
    `merge-request` you can move the code from `publish` branch to the public repo
    ([see the existing guidance][2])

It's good practice to make a new branch and do a `pull-request` in your public 
repo too, but you could also just make the changes durectly to the `main` branch
of the public repo.

## Versioning and Changelogs

When you update your code, you've done the pull request, and it's all ready to
be moved over to the public repo, it's a good time to tag the repo with a 
[semantic version][4] (in GitHub this can be done using the ["release"][5]
functionality). You could also maintain a [`CHANGELOG.md`][6] so users can easily
see what has changed since your last version release.

If you do a release with a version in the private repo, **make sure you also 
release with the same version tag on the public repo**.

## How often to update the published code?

!!! tip "Main Points"

    - ultimately it's up to the person who "owns" the codebase and the needs 
    of the stakeholders
    - small changes can probably be batched up and then the published code 
    updated less frequently

Each codebase (for a publication, package or whatever) will be different and
will need changing at different rates, decided by the needs of the stakeholders,
available resources and the person in charge of that codebase. 

For example, for an annual publication, if some changes are made, might not be 
necessary to update the existing published codebase immediately, especially if 
they're small, minor fixed. However, If it's an important, change such as a new 
feature (i.e. some new metric) then it would probably help any stakeholders to 
see that published as soon as possible.

## Useful Links

- [GitHub pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests "guidance on github pull requests")
- [GitLab merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/)
- [GitHub Releases][5]
- [Semantic Versioning][4]
- [Keep a changelog][6]

above.*

[1]: how-to-publish-your-code-in-the-open.md
[2]: how-to-publish-your-code-in-the-open/#moving-your-code-to-the-nhs-digital-github
[3]: https://nhsd-confluence.digital.nhs.uk/pages/viewpage.action?spaceKey=KH&title=Github+-+publishing+your+code
[4]: https://semver.org/
[5]: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
[6]: https://keepachangelog.com/en/1.0.0/
