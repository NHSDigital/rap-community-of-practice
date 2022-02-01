# Overview
This page is intended as a starting point for someone who is new to using git. It shows you the basic commands and the workflow to use git on your own. 

To use git as a team you should complete this section and the following section on [using git collaboratively](02_using-git-collaboratively.md).

# What is version control?
Version control is the practice of tracking and managing any changes on project's code, files or folders over time. This allows you to observe a detailed history of the changes made and enables your team members to collaborate on the same project.
 
In Git, each user has the entire repository (project's working directory) on their computer (offline), hence, they can work separately offline until they opt to push their updated version of the code to the remote (online) central repository. 

Remote repositories are versions of your project that are hosted on an online Version Control System. In NHS Digital, we store that in GitLab site for internal users (GitHub site for the public).

## Why should I care?
Using version control is one of the fundamental skills needed by analysts to produce high-quality analytical outputs. Git is **the standard** for tracking code over time and is the way that NHSD has chosen. While git has a steep initial learning curve, the payoff is huge and so we strongly recommend taking the time to learn this as a team.

The benefits of using version control include:

* Understanding what happened in the past. E.g., what did we change last time we ran this code
* Restoring previous versions
* Tracking changes - avoid accidentally breaking code
* The ability to review someone's changes and to leave comments
* The ability to plan development work more effectively through being able to assign small, discrete changes
* Avoid code being hidden away on someone's machine
* The ability to set up an approval process for changes
* The ability to make changes without breaking anything - through running automated tests
* The ability to try out experiments without the risk of breaking your main code

# Video showing git workflow and commands:
This short video tutorial walks you through how to create a repository and use basic git commands:

[Link to video tutorial]

We have also produced a short video that gives some more theoretical explanation of how version control works: 

[Link to video]
<br/><br/>

# Common basic commands:

Below is a list of common commands for reference. We only list basic commands here. This is just to flag to you that these commands exist. You can google for more detail on any of them.

* Create a new git repo locally: `git init`. The init command is short for "initialise", it's the command that will do all of the initial setup of a repository. The folder needs to actually exist before we can create a new repository with Git.
 
* Clone an existing Git Repository: `git clone <url>`. Happens only once, when you need to create a local copy of a Gitlab repository.

* Check whether any files have changed in a repository: `git status`. It lists the files you've changed and those you still need to add or commit. It displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git. Status output does not show you any information regarding the committed project history.

* Create and switch to a new branch: `git checkout -b <your branch name>`.

* Check out a branch: `git checkout <your branch name.`. Check out an existing new branch.

* Add file contents/stages changes from the working directory to the index: `git add <filename>` or `git add .`

* Commit staged files with a message: `git commit -m "<message>"`. Committing changes in this way captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project

* Update your branch with the online/remote branch info: `git pull`. Pulls the latest changes from the repository, only affects the current active branch you’re in.

* Check the history of commits: `git log`. 
 
* Show unstaged changes between your index and working directory: `git diff`. Press `Q` to exit the diff log.

* Ignore files: `.git-ignore file`. This file specifies untracked files that git should ignore such as the sensitive information related to security or the data itself. Files already tracked by git are not affected.

* Display a list of all branches in the repository: `git branch -a`.

* Delete a local branch: `git branch -D <your branch name>`.
