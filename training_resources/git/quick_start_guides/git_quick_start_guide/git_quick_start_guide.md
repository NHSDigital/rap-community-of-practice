---
title: Git Quick Start Guide

tags: 
  - Git
  - Version control
---

#

!!! tip "TLDR"

    * Make sure to install Git on your computer.  
        * Windows: Download and install [Git][Download Git] and [Git for Windows]
        * MacOS: Run `git --version`. This will prompt you to install Git if not already installed.
        * Linux: Run `sudo apt install git-all` or `sudo dnf install git-all` depending on your distribution.
    * Check Git has been installed with `git --version` in a Bash Terminal.
    * Configure your identity for commits with the `git config` command:
        ```bash
        git config --global user.name "Peter Parker"
        git config --global user.email "peterparker@example.com
        ```

??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[Introduction to Git]|Necessary|It is important to get an understanding of Git before starting to use it|

## Install Git

Installing Git is a simple and straightforward process. You might have it already installed on your system, however, it is good to verify and make sure you are using the latest version of Git.

=== "Windows"

    [Download Git] from the Git-SCM website. In addition, install [Git for Windows], which is a project that provides additional tools to use Git in the Windows OS, including Git Bash and Git Credential Manager (GCM).

    !!! info

        During the installation of Git for Windows, you will be asked to select a credential helper, with GCM listed as the default. It is recommended that you keep this set to GCM as it will enable caching of remote repository credentials in the [GitHub] and [GitLab] quick start guides.

    Once installed, open Git Bash to verify it is installed:

    ``` bash
    git --version
    ```

=== "MacOS"

    In the [Terminal] run:

    ``` bash
    git --version
    ```

    This will detect if Git is installed and provide the version number if it is. If it is not installed, it will prompt you to install it.

    Once installed, run the above command again to check it is installed.

=== "Linux"

    Git is normally already installed on Linux, but it is good to update to the latest version anyway.

    You can install Git through the package management tool that comes with your distribution of Linux:

    === "Debian/Ubuntu based distributions"

        In the [Terminal]:

        ```
        sudo apt install git-all
        ```
    === "Fedora/CentOS based distributions"

        In the [Terminal]:
        ```
        sudo dnf install git-all
        ```

    Once installed, run the following command verify it is installed:

    ``` bash
    git --version
    ```

## First-Time Configuration

Now that you have Git on your system, there are a few things you can do to customise your Git environment. To do this we are going to use the `git config` tool.

We are going to use the `--global` flag to set these values for all your repositories.

!!! question inline end "Why does Git need these details?"

    Git uses these details in every commit you make; it is immutably baked into them. 
    
    When you later examine the Git history, you will be able to see who did what.

The first properties we are going to set are your name and email address:

``` bash
git config --global user.name "Peter Parker"
git config --global user.email "peterparker@example.com
```

You can confirm they have been set with the following commands:

``` bash
git config user.name
git config user.email
```

??? info "Optional Settings"

    ### Default Editor

    Next, we can configure the default text editor that will be used when Git needs you to type in a message. This is optional, as if this property is not set, Git will just use your systems default editor. 

    We can use the following commands to configure this setting:

    === "Windows Notepad"

        ``` bash
        git config --global core.editor notepad
        ```

    === "Visual Studio Code"

        ``` bash
        git config --global core.editor "code --wait" # (1)!
        ```

        1. The `--wait` flag instructs Git to wait for the message file to close before continuing.

    === "Emacs"

        ``` bash
        git config --global core.editor emacs
        ```

    === "Other Editors"

        There are a wide variety of editors for you to use. **Use the one that suits you.** 
        
        The Pro Git Book has an appendix section with [how to set different editors]. 

    ### Setting your default branch name

    When you create a new repository with `git init`, Git will by default call the branch `master`. More recently, it has become convention to set your default branch to `main`, as it is a more neutral term.

    To change this setting, run:

    ```bash
    git config --global init.defaultBranch main
    ```

    ### Other settings

    We can set a lot of other settings with `git config`, although usually is best to leave these settings be, especially as a beginner. However, as you get to grips with Git, you might want to further tweak your experience:

    * [Git Aliases] are a great way to create shorthand commands.
    * [Credential Storage] allows you to change the default method for storing HTTP passwords.
    * [Git Configuration] explains all parts of the `git config` command and what you can do.

??? info "Checking your configuration settings"

    You can view all of your settings in two ways:

    === "Command Line"

        In a Bash Terminal run:

        ```bash
        git config --list --show-origin
        ```
    
    === "Inspecting the .gitconfig file"

        The `.gitconfig` file for global configuration variables is normally stored in the `$HOME` directory. For Windows users this is usually `C:\Users\$USER`. For MacOS and Linux this is usually `/home/$USER`.

        If you have set your configuration setting with other locality flags (`--system` or `--local`), take a look at the Pro Git book section on [First-Time Git Setup].

## Try Git Out

We have a full detailed walkthrough of using Git for the first time to [commit work]. However, let's quickly go through some commands to ensure your set up is working correctly.

??? example "Try Git Out"

    In a suitable place on your computer, this can be your `$HOME` folder (usually `C:\Users\$USER` for Windows or `/home/$USER` for MacOS and Linux), or any other folder where you want to store repositories:

    1. Create a new folder, call it `my_first_repository`. You can do this manually or via the command line using the make directory, `mkdir`, command:

        ``` bash
        mkdir my_first_repository
        ```

    2. Move into the folder via the command line:

        ``` bash
        cd my_first_repository
        ```

    3. Initialise a repository:

        ``` bash
        git init
        ```

    4. Create a empty file called `new_file.txt` with the touch command:

        ``` bash
        touch new_file.txt
        ```

    5. Add the new file to the staging area and start tracking it:

        ``` base
        git add new_file.txt
        ```

    6. Commit the file. Add a simple message using the `-m` flag:

        ``` base
        git commit -m "Added new_file.txt`
        ```

        If you have set your editor in the optional settings above, you can test it out by leaving off the `-m "<message>"` from the `git commit`. This will prompt the default editor to open. Write your commit message there and then close to submit it.

    7. View your recent commit with `git log`. Press `q` to exit the pager view of the log:

        ``` base
        git log
        ```

## Next Steps

Now that you have set up your Git environment, you will want to set up your access to a remote repository service such as [GitHub] or [GitLab]. This will enable you clone repositories from internet, as well as push and back-up your local repositories and start collaborating on them.

[Download Git]: https://git-scm.com/download/win
[Git for Windows]: https://gitforwindows.org/
[Introduction to Git]: ../introduction-to-git.md
[Terminal]: ../introduction-to-git.md#how-do-i-use-git
[how to set different editors]: https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config#ch_core_editor
[Git Aliases]: https://git-scm.com/book/en/v2/ch00/_git_aliases
[Credential Storage]: https://git-scm.com/book/en/v2/ch00/_credential_caching
[Git Configuration]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_git_config
[First-Time Git Setup]: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
[commit work]: ../git_walkthroughs/committing_work_walkthrough.md
[GitHub]: ./github_quick_start_guide.md
[GitLab]: ./gitlab_quick_start_guide.md
