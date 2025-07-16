---
title: Introduction to Git

tags: 
  - Git
  - Version control
  - GitHub
  - GitLab
---

#

!!! tip "TLDR"

    * Code version control is becoming a fundamental skill for any analyst.
    * It is needed to meet [**Baseline RAP**].
    * Allows tracking and management of changes to code, and disaster recovery.
    * [Git] is free and open-source; it is the most common code version control system and is used widely in NHS England.
    * It is recommended to use Git in the command-line, though GUIs can also be useful. Guidance [here].
    * Typically we only put code in Git repos. The [`.gitignore` file][gitignore] allows you to automatically exclude CSVs and other things we don't want adding to the Git repo.

???+ question "Why should I care?"

    The benefits of using version control include:

    * It's fundamental to RAP and essential to meeting [**Baseline RAP**]
    * Understanding what happened in the past; e.g. what did we change last time we ran this code
    * Restoring previous versions
    * Tracking changes - avoid accidentally breaking code
    * The ability to review someone's changes and to leave comments
    * The ability to plan development work more effectively through being able to assign small, discrete changes
    * Avoid code being hidden away on someone's machine
    * The ability to set up an approval process for changes
    * The ability to make changes without breaking anything - through running automated tests
    * The ability to try out experiments without the risk of breaking your main code

??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[Levels of RAP]|Helpful|Code version control (e.g. Git) is a key component of Baseline RAP; it is good to know what else is in Baseline RAP|

## What is Version Control?

Version control is the practice of tracking and managing any changes on a project's code, files or directories over time. This allows you to observe a detailed history of the changes made and enables your team members to collaborate on the same project.

The [Pro Git book], written by Scott Chacon and Ben Straub, has a more detailed [introduction to Version Control] and the different types that exist. The [Duck book] also has some excellent guidance on why you should use version control and how to use Git.

### What is Git?

Git is a free, light-weight and open-source version control system; it is considered **the standard** version control system. Other version control systems exist, however, [git's feature set] has made it the dominant version control system. While Git has a steep initial learning curve, the payoff is huge and it is strongly recommend you take the time to learn it.

In Git, each user has the entire repository (project's working directory) on their computer (offline), hence, they can work separately offline until they opt to push their updated version of the code to the remote (online) central repository.

Remote repositories are versions of your project that are hosted on an online Version Control System, such as [**GitHub**] and [**GitLab**] (also [**BitBucket**]).

???+ question "What is the difference between Git, GitLab, and GitHub?"

    === "Git"
        * Git is the software, locally installed on your computer and manages code and file history.
        
        * Git was released in 2005 and maintained by Linux.

        * Git focuses on version control and code sharing and has no user management ability.

        **Get started with Git with our [Git Quick Start Guide]**

    === "GitHub"
        * GitHub is a cloud-based remote repository storage service accessible [online][GitHub website].
        
        * GitHub was released in 2008 and is maintained by Microsoft.

        * GitHub focuses on centralising source code hosting and provides user management features.

        * GitHub is highly integrated with Visual Studio Code, which is also maintained by Microsoft.

        * NHS Digital has a [GitHub "Organisation"] which can host both public code repositories and private ones only visible to NHS Digital colleagues. 
        
        * This website is hosted out of the NHS Digital GitHub organisation - [see the repo here].

        * GitHub also provides some additional features, such as [GitHub Pages], which is used to host static websites. [This website] is hosted in this exact way.

        **Get started with GitHub by checking out our [GitHub Quick Start Guide]**

    === "GitLab"
        * GitLab, like GitHub, is a remote repository storage service. It is accessible [online][GitLab website].
        
        * It was released in 2014 and is maintained by GitLab Inc, which is considered the first partly-Ukrainian unicorn.

        * GitLab hosts Git repositories, focusing on centralising source code hosting. It provides user management features.

        * Both GitHub and GitLab function in very similar ways [with some differences in terminology], e.g. Merge Requests vs Pull Requests.

        * NHS England has a number of internally hosted instances of GitLab. These can only be accessed by members of the instance.

        **Get started with GitLab by checking out our [GitLab Quick Start Guide]**

??? info "Read more about Git"

    You can read more about Git in the previously mentioned Pro Git book, including a [short history of Git] and [what is Git] in more detail than explained here.

## How do I use Git?

You can start using Git on your machine with our [Git Quick Start Guide]. However, there are two main ways of interacting with Git, using the Command Line and using a Graphical User Interface (GUI).

=== "Using the Command Line"

    ??? question "What is the Command Line?"

        *Aka the Terminal, the Command Prompt, the Shell*

        The Command Line acts like a mediator - it takes text input (a command) and returns an output (a process, a result, an action) that depends on the command input's process. 
        
        Command line terminals can be used to input commands such as listing directories, moving folders and files, version control (Git) and creating isolated environments (conda, venv etc).

    **Using the Command Line is the recommended method of interacting with Git**. It is the only method that you can use to run *all* Git commands.


    There are a number of command line terminals that are available for you to use, depending on what Operating System (OS) you are using:

    === "Windows"

        **Git Bash** is a recommended method of interacting with Git in Windows. Git Bash comes packaged with [Git for Windows] and provides a Bash emulation used to run Git from the command line. This provides commonality of commands with other OS's.

        Alternatively, **Powershell** is a powerful terminal built into Windows by default. Once installed, using Git is exactly the same as in Git Bash. However, other commands (like creating a new folder or viewing a folder's contents) might differ. In these guides, any differences in commands between Powershell and Git Bash will be highlighted.

        It is also possible to set up other terminals, like Anaconda Prompt and the legacy CMD prompts to work with Git.

    === "MacOS"

        **Terminal** is the built-in command line terminal for MacOS. It uses an extended variant of Bash called [Zsh], which adds some new features and support for plugins and themes. It still runs on the same commands as Bash, so it has many of the same features and commands.

    === "Linux"

        **Terminal** is the built-in command line terminal for Linux. It uses Bash on most distributions of Linux. 

        It is relatively straightforward to customise the terminal in Linux, for example, setting it up to use Zsh with [Oh My ZSH]

=== "Using a GUI"

    GUIs make it easier to use Git by presenting Git outputs in a more user-friendly state and removing the need to remember the exact commands needed. They are great for getting simple tasks done.

    Git comes with built-in GUI tools for committing ([git-gui]) and browsing ([gitk]), but there are several also third-party tools, like [GitHub Desktop], and integrations with IDEs, like [Visual Studio Code].

    However, GUIs are commonly limited in capabilities, usually only implementing a partial subset of Git functionality for simplicity. Therefore, **it is recommended that you learn to use the command line** first and as your primary means of working with Git. Then, after you feel more confident and are using it day-to-day, start exploring and adopting GUIs to make your life easier.

### Common Git Commands

Below is a list of common commands for reference. We only list basic commands here. This is just to flag to you that these commands exist. You can google for more detail on any of them.

`git init`

:   **Create a new Git repo locally.**  
    The init command is short for "initialise"; it's the command that will do all of the initial setup of a repository. The directory needs to actually exist before we can create a new repository with Git.

`git clone <url>`

:   **Clone an existing Git Repository**  
    Happens only once when you need to create a local copy of a GitLab repository.

`git status`

:   **Check whether any files have changed in a repository**  
    Displays the state of the working directory and the staging area. See which changes have been staged, which haven't, and which files aren't being tracked by Git. The status output does not show you any information regarding the committed project history.  

`git add`

:   **Add files to the staging area**  
    `git add <file>` will add the specified file to the staging area, ready for commit.  
    `git add .` will add all modified files to the staging area, ready for commit.

`git commit -m "<message>"`

:   **Commit staged files with a message**  
    Committing changes in this way captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project.

`git pull`

:   **Update your current branch with the online/remote branch info**  
    Pulls the latest changes from the repository and only affects the current active branch you’re in.

`git push`

:   **Update the online/remote branch with commits from your current branch**  
    Pushes the latest changes to the repository and only affects the current active branch you're in.

`git fetch`

:   **Downloads the online/remote repository information, including commits, files, and branches**  
    Unlike the more aggressive `git pull`, your local development work is unchanged. However, your local repository is aware of any changes that can be later integrated into your local work.  
    `git fetch` is a great way to safely check what everybody else has been working on in the shared repository.

`git log`

:   **Check the history of commits**  
    Press `Q` to exit the log.
    
`git diff`

:   **Show unstaged changes between your index and working directory**  
    Press `Q` to exit the diff log.

`echo '<pattern>' >> .gitignore`

:   **Adds a pattern to the end of .gitignore file**  
    This file specifies untracked files that git should ignore, such as the sensitive information related to security or the data itself. Files already tracked by git are not affected.  
    See the section on [what should you be version controlling] for more details.

`git checkout`

:   **Check out a branch.**  
    `git checkout <your branch name>` will checkout an existing branch
    `git checkout -b <your branch name>` will checkout a new branch

`git branch -a`

:   **Display a list of all branches in the repository**  

`git branch -D <your branch name>`

:   **Delete a local branch.**  
    Does not delete the remote branch

`git push origin -d <your branch name>`

:   **Delete a remote branch**  
    Does not delete the local branch.

!!! abstract "Git Cheat-Sheets"

    Keep a list of everyday Git Commands by bookmarking this cheat sheet: [Git Commands Cheat-Sheet]

!!! info Undoing changes via Git commands

    GitLab has a guide covering various cases on undoing any changes: [undo possibilities in Git](https://docs.gitlab.com/ee/topics/git/numerous_undo_possibilities_in_git/).

## What should I be version controlling?

While most guides on Git will talk about tracking code files (i.e. `.py`, `.sql`, etc.)  with Git, nearly any type of file on your computer can be tracked. However, there are some files that it is strongly recommended you do not version control using Git for a number of reasons:

* Large data files, directories, and databases; e.g. `data-files/`, `data/`, `.dbs`:
    * Git struggles to store large files, and remote repositories normally have a hard limit on file sizes.
    * Lookup or test data files of a reasonable size would probably be fine to include.
    * These files might also contain Personal Identifiable Data (PID) which must not be added to the commit history.
* Configuration files and directories; e.g. `.config`, `.vscode/`:
    * Configuration files are typically custom to the individual, storing the configurations and preference setting for your Integrated Development Environment (IDE).
    * Including these files might cause confusion or "It works on my machine" situations.
* Environment and credentials files; e.g. `.env`, `.credentials`:
    * These files might contain credentials, PATs, API keys, or other environment variables that are sensitive and should not be shared.
    * *Note: you should NEVER put credentials directly into your code. They should always be stored in a `.env` file or equivalent which are not committed to the Git repository*
    * GitHub and GitLab also allow you to store "secrets" for repos which can be used by collaborators but cannot be seen, copied or accessed directly.
* Run time files (e.g. logs); e.g. `.logs`:
    * Log files that are generated by your code are very useful for providing infomation on what was happening when your code was running. They are very useful in debugging. However, these files are usually individual to the system and can get very big.

!!! danger

    Once a file or directory is committed, a record of it and its contents will persist in the commit history. Simply deleting the file or directory at a later date will still leave a trace in the commit history.

    It is possible to scrub the Git history of any record of this file; however, this is risky in of itself and should be completed with great care. Prevention is much preferable to the cure.

    Even after scrubbing the Git history, **consider any secret information that has been committed to a repository as potentially exposed.** Carry out mitigation activities, like revoking and reissuing access keys and reporting PID leaks.

    <!-- Todo for NV-1481: Read more about these issues and how to mitigate them in our Security and Information Security guide -->

### gitignore

`.gitignore` is a text file that contains file extensions and directories' paths that we wish Git to ignore. This will ensure that the files and directories that match those specified in the `.gitignore` file and avoiding the dangerous situations detailed above.

For example, if we have created a repository that should never contain data, either held in a data directory or in CSV and XLSX Excel files elsewhere. We can create a `.gitignore` file and include in it the following:

``` title=".gitignore"
data/
*.csv
*.xlsx
```

GitHub has a [.gitignore template for python] available for analysts and developers to use for their own projects.

Some common patterns and formats for Git-Ignore files include:

`Blank Line`

:  A blank line doesn’t refer to any file name, so we can use it to separate two file names for ease of reading.

`#`

:   A line beginning with the `#` symbol refers to a comment. However, if `#` is used as a pattern, then use backslash so that it is not misunderstood as a comment, `\#`

`/`

:   Used as a directory separator, i.e. to include directories, for example, `webdev/`. 

`*.extension_name`

:   Used to match an extension name. For example, `*.txt` and `*.log` can be used to match ALL the files that have .txt and .log as their extension, respectively.

`**/any_name`

:   Used to match any file or directory with the name any_name.

`any_name/**`

:   Used to match anything that is inside the directory of the name any_name. For example, `webdev/**` matches all the files inside the webdev directory.

`!include_file.extension_name`

:   Used to create a negating pattern to exclude a file from a different pattern. In this example, all files with `.extension_name` are excluded, except `include_file.extension_name`.  

    This does not work if trying to negate something in an already ignored directory. For example, `!example_directory/example_file.md` would not negate `example_directory/` and `example_file.md` would still be ignored.

### Tracking Binary Format Files

Git is primarily designed to work with text file formats as it can easily track changes to and within the file. If you are tracking files stored in binary format (e.g. Microsoft Files and other proprietary file formats, media, compressed files, etc.), Git will only be able to track that a change has happened to the file, but not the exact changes made.

It is usually advised not to track binary files unless there is a good reason to. The [RAP Community of Practice] repository stores picture files to include in our documentation. Your repository might include a compressed directory containing an example output file your pipeline might produce.

Finally, some proprietary file formats (e.g. Microsoft Office Files) have equivalent (possibly less feature-rich) text-based open file formats. Consider converting to these file formats to allow more detailed version control tracking (and allow more users to access those files).

## What next?

Now you have been introduced to Git, make sure you are set up to use it with our [Git][Git quick start guide], [GitHub][github quick start guide], and [GitLab][gitlab quick start guide] quick start guides.

Once you are set up, check out our guide on [using git collaboratively] with your team and start incorporating it into your work.

We also have a number of walkthroughs that will guide you through using the powerful features provided by Git for the first time:

* [Committing Work Walkthrough]
* [Working with Branches Walkthrough]
* [Pull and Merge Requests Walkthrough]

[git's feature set]: https://git-scm.com/about
[Pro Git book]: https://git-scm.com/book/en/v2
[short history of Git]: https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git
[what is Git]: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
[introduction to Version Control]: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
[Git quick start guide]: ./quick_start_guides/git_quick_start_guide.md
[GitHub website]: https://github.com/
[rap-community-of-practice]: https://github.com/NHSDigital/rap-community-of-practice
[GitHub Pages]: https://pages.github.com/
[this website]: https://nhsdigital.github.io/rap-community-of-practice/
[github quick start guide]: ./quick_start_guides/github_quick_start_guide.md
[GitLab Website]: https://about.gitlab.com/
[gitlab quick start guide]: ./quick_start_guides/gitlab_quick_start_guide.md
[Git for Windows]: https://gitforwindows.org/
[Zsh]: https://zsh.sourceforge.io/
[Oh My ZSH]: https://ohmyz.sh/
[git-gui]: https://git-scm.com/docs/git-gui
[gitk]: https://www.atlassian.com/git/tutorials/gitk
[GitHub Desktop]: https://desktop.github.com/
[Visual Studio Code]: https://code.visualstudio.com/docs/sourcecontrol/overview
[Git commands cheat-sheet]: https://training.github.com/downloads/github-git-cheat-sheet/
[what should you be version controlling]: #what-should-i-be-version-controlling
[.gitignore template for python]: https://github.com/github/gitignore/blob/master/Python.gitignore
[RAP Community of Practice]: https://nhsdigital.github.io/rap-community-of-practice/
[**Baseline RAP**]: ../../introduction_to_RAP/levels_of_RAP.md
[Git]: https://git-scm.com/
[here]: #how-do-i-use-git
[gitignore]: #gitignore
[Levels of RAP]: ../../introduction_to_RAP/levels_of_RAP.md
[**Baseline RAP**]: ../../introduction_to_RAP/levels_of_RAP.md
[RAP Community of Practice GitHub]: https://github.com/NHSDigital/rap-community-of-practice/issues
[Duck book]: https://best-practice-and-impact.github.io/qa-of-code-guidance/version_control.html
[**GitHub**]: https://github.com/
[**GitLab**]: https://about.gitlab.com/
[**BitBucket**]: https://bitbucket.org/product/
[GitHub "Organisation"]: https://github.com/NHSDigital
[see the repo here]: https://github.com/NHSDigital/rap-community-of-practice
[with some differences in terminology]: https://about.gitlab.com/blog/2016/01/27/comparing-terms-gitlab-github-bitbucket/
[using git collaboratively]: ./using-git-collaboratively.md
[Committing Work Walkthrough]: ./git_walkthroughs/committing_work_walkthrough.md
[Working with Branches Walkthrough]: ./git_walkthroughs/working_with_branches_walkthrough.md
[Pull and Merge Requests Walkthrough]: ./git_walkthroughs/pull_and_merge_requests_walkthrough.md
[undo possibilities in Git]: https://docs.gitlab.com/ee/topics/git/numerous_undo_possibilities_in_git/
