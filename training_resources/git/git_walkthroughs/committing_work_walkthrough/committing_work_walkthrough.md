---
title: Committing Work

tags: 
  - Git
  - Version control
---

#

!!! tip "TLDR"

    - This is a beginner friendly guide on how to commit your work using Git for the first time!
    - Commits can be thought of snapshots or checkpoints along the timeline of your project that you can go back to if anything goes wrong.
    - [Initialise or clone a Git repository] with the `git init` or `git clone` command.
    - [Make changes].
    - [Stage changed files] with the `git add` command.
    - [Commit staged files] with the `git commit` command.

??? success "Pre-requisites"

    | Pre-requisite | Importance | Note |
    |---------------|------------|------|
    |[Intro to Git][introduction-to-git]|Necessary|This guide assumes you are using Git to version control|
    |[Using Git collaboratively][using-git-collaboratively]|Helpful|Get started using Git as a team|

## What is a Git commit?

Git commits are the core building blocks of a Git repository's history. Commits can be thought of as snapshots or checkpoints along the timeline of a project.

Adding commits keeps track of your changes and progress as you work and each commit is a point in the project you can always go back to if anything goes wrong.

Snapshots are always committed to the local repository. Git doesn’t force you to interact with the remote repository until you’re ready.

## How to make a Git commit

=== "Initialise a Git repository"

    To change your working directory to the project directory, open a terminal (e.g. [Bash Terminal]) and enter:

    ``` bash
    cd <project-filepath>
    ```

    To initialise a Git repository for the project, in a terminal enter:

    ``` bash
    git init
    ```

=== "Clone a Git repository"

    To clone an existing Git repository, open a terminal (e.g. [Bash Terminal]) and enter:

    ``` bash
    git clone <url>
    ```

### Make changes

Here is an example of creating a new README markdown file using the terminal:

```bash
echo "# Name of Repository" >> README.md
```

### Stage files

To add untracked or modified files to the staging area, in a terminal enter:

```bash
git add <file-name>
```

!!! warning

    You can also use `git add .` to add all the files that have changed - but use this with care - it's best practice to manually confirm each change to ensure it was intentional

!!! info

    It is possible to skip the staging process and commit a file directly.

    **However, this is generally NOT recommended.** 
    
    To find out more about why using "git add" is important, [see this great guide by Github](https://github.com/git-guides/git-add)

### Commit files

To commit all staged files, in a terminal enter:

```bash
git commit -m "Added README"
```

## Useful commands

- Check which files have changed in a repository: `git status`
- Check the history of commits: `git log`

!!! info
    
    You can escape from `git log` by pressing `q`

## Useful links

- [Git Basics - Recording Changes to the Repository]
- [Atlassian - Git commit]

[initialise or clone a git repository]: #how-to-make-a-git-commit
[make changes]: #make-changes
[stage changed files]: #stage-files
[commit staged files]: #commit-files
[introduction-to-git]: ../introduction-to-git.md
[using-git-collaboratively]: ../using-git-collaboratively.md
[bash terminal]: ../introduction-to-git.md#how-do-i-use-git
[git basics - recording changes to the repository]: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
[atlassian - git commit]: https://www.atlassian.com/git/tutorials/saving-changes/git-commit
[rap community of practice github]: https://github.com/NHSDigital/rap-community-of-practice/issues
