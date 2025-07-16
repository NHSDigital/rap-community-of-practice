---
title: Working with Branches

tags: 
  - Git
  - Version control
---

#

!!! tip "TLDR"

    * This is a beginner friendly guide on how to work and collaborate with Git for the first time.
    * Working with branches is a core part of working with Git, allowing quick and safe collaboration with others (and yourself!)
    * Knowing how to [create](#creating-a-branch), [switch](#changing-branch), [delete](#deleting-a-branch), and [merge](#merging-branches) branches are a vital skills and can be done both locally via Git and remotely via GitHub and GitLab.
    * Sometimes [conflicts between branches](#resolving-merge-conflicts) occurs and Git will need your input to solve these conflicts. However, Git makes them very easy to resolve, even if they look scary initially!

??? success "Pre-requisites"

    | Pre-requisite | Importance | Note |
    |---------------|------------|------|
    |[Intro to Git](../introduction-to-git.md)|Necessary|This guide assumes you are using Git to version control|
    |[Using Git collaboratively](../using-git-collaboratively.md)|Necessary|It is important to be familiar with the concepts covered in this guide|
    |[Committing Work Walkthrough](../using-git-collaboratively.md)|Recommended|Make sure you are confident with using the basic commands of Git first|

!!! info "Check your current branch"

        When performing some operations, it is useful to know your current branch. You can quickly confirm your current branch with the following command:

        ``` bash
        git branch --show-current
        ```

        `git status` will also print the current branch at the top of the return message, as well as other useful information. Use it frequently.

## Creating a Branch

=== "Terminal"

    ??? question "Are you in the correct repository?"

        Before you start, ensure that you are in the correct directory containing the local version of your repository:

        ``` bash
        cd <project-filepath>
        ```

    To create a new branch, use the command:

    ``` bash
    git checkout -b new-branch-name
    ```

    This command will both create and switch your repository to your new branch, based on the current branch.

    !!! info "Create a branch from a different branch"

        If you want your new branch to be based off a different branch than the one you are currently on, simply specify the name of that base branch:

        ``` bash
        git checkout -b new-branch-name source-branch-name
        ```

    ### Publishing the new branch

    The branch you have created only exists on your local version of the repository and will need to be published on to the remote version of your repository:

    ```bash
    git push --set-upstream origin new-branch-name
    ```

=== "GitHub"

    To create a branch in GitHub, make sure you are on the `Code` screen of your repository, this is the default page you see when you navigate to your repository. Follows these steps:

    1. Click on the branches button, highlighted in blue below and showing the number of branches we currently have (which is currently 3).

        ![Screenshot of the header menu of a github repo with the branches button currently highlighted](../../../images/github_creating_new_branches_1.png "The button you want is next to the branches drop down menu on the left, currently showing main as our current branch")

    2. This will bring up the branches page. Click on the green `New Branch` button to the right.

        ![](../../../images/github_creating_new_branches_2.png "")

    3. This will bring up the `Create a branch` popup. Enter a suitable name for your branch and select the branch source. The branch source is the version of the code that your new branch will be based on and diverging from, and is by default main, which should be a stable working version of your code.
    4. Click the green `Create branch` button when you are ready.

        ![](../../../images/github_creating_new_branches_3.png "")

    5. Once created, you will be returned to the `Code` screen of the repository with the new branch checked out and ready to be viewed and worked on.

        ![](../../../images/github_creating_new_branches_4.png "")

    Alternatively to the process above, you can click on the branches drop down menu and enter your new branch's name. If that branch doesn't already exist then an option to create a new branch will appear.

    ![](../../../images/github_creating_new_branches_1-alternative.png "")

    The base branch will be set to the branch you are currently on and creating the new branch from. Change branches before you create the new branch if you want it to be different.

    !!!info "Accessing your new remote branch on a local repository"

        To access your new remote branch on your local repository, simply follow the instruction for [Changing Branches](#changing-branch) in the Terminal.

=== "GitLab"

    To create a new branch in GitLab:

    1. First navigate to the branches page by going to the side-menu on the left, then `Repository` then `Branches`.

        ![GitLab repository menu with branches option selected](../../../images/gitlab_create_branch_1.png "GitLab repository menu with branches option selected")

    2. Select the `New Branch` button on the left in blue

        ![Top of the Branches page with New Branch selected on the left](../../../images/gitlab_create_branch_2.png "Top of the Branches page with New Branch selected on the left")

    3. Enter your new branch's name in the `Branch name` field and from the `Create from` menu, select the source branch, which your new branch will be based upon.
    4. When ready, click the blue `Create branch` button.

        ![New branch view filled out with the branch name and source branch](../../../images/gitlab_create_branch_3.png "New branch view filled out with the branch name and source branch")

<!-- TODO: === "VS Code" -->

## Changing Branch

=== "Terminal"

    To change to a new branch:

    ``` bash
    git switch target-branch-name
    ```

    ??? info "`git checkout` vs `git switch`"

        `git switch` is a recent addition to Git and the older `git checkout` can also switch branches:

        ``` bash
        git checkout target-branch-name
        ```

        The addition of `git switch` is because `git checkout` has dual purposes, switching branches or restoring working tree files. This dual function can be a source of confusion for some users. The second function is not included in `git switch` but instead `git restore`.

        If you have already learnt to use `git checkout` to switch branches then that will continue to work, but if you are just learning git then it is better to use the more predicable `git switch` command.

=== "GitHub"

    To switch branches in GitHub:

    1. Click on the branches drop down menu in the `Code` view of your repository. This is the button in the top left of the screen and will show the name of currently checked out branch. By default this will be `main`.
    2. Type in the name of your branch to find it or select it from the list.

    ![](../../../images/github_switching_branches_1.png "")

    Alternatively, you can navigate to the "Branches" page of your repository and select the branch from there. To get to the "Branches" page, click on the button next to the branches drop down menu.

    ![](../../../images/github_switching_branches_3.png "")

    Once you have switched branches, you will be returned to the `Code` view, which will show the code from the branch you have now checked out with its name shown in the branch drop down menu.

    ![](../../../images/github_switching_branches_2.png "")

=== "GitLab"

    To switch branches in GitLab:

    1. Click on the branches drop down menu in the `Files` view of your repository. This is the button in the top left of the screen and will show the name of currently checked out branch. By default this will be `main` or `master`.
    2. Type in the name of your branch to find it or select it from the list.

        ![](../../../images/gitlab_switch_branch_1.png "")

    3. Once you have switched branches, you will be returned to the `Files` view, which will show the code from the branch you have now checked out with its name shown in the branch drop down menu.

        ![](../../../images/gitlab_switch_branch_2.png "")

<!-- TODO: === "VS Code" -->

!!!help "Help, I can't see the branch I have created locally on my remote repository (GitHub/GitLab)?"

    If you have created a new branch on a local clone of the repository but cannot see it on GitHub, then you might not have pushed it and set your local branch to track the upstream one.

    You can quickly check a local branch's branch tracking info with `git status --short --branch` or `git status -sb`:

    ```bash title="Expected return when a branch has it's upstream set correctly"
    git status -sb
    ## branch-name...origin/branch-name
    ```

    If the branch does not have a remote branch set then only the first part will show.

    ```bash title="Expected return when a branch has it's upstream has not been set"
    git status -sb
    ## branch-name
    ```

    To set the upstream, push with the `--set-upstream` (`-u`) flag:

    ```bash
    git push -u branch-name
    ```

## Deleting a Branch

=== "Terminal"

    Deleting a branch is a two step process. Just like how when creating a branch you create it both locally and on the repote repo, when deleting you have to delete the branch locally and also delete the remote branch.

    1. To delete the branch locally

        ``` bash
        git branch -d target-branch-name
        ```

    2. To delete the branch remotely:

        ``` bash
        git push origin --delete target-branch-name
        ```

        You can also use the shorter command to delete remotely:

        ``` bash
        git push origin :target-branch-name
        ```

    ??? info "Error when deleting a remote branch"

        If you get the error below, it may mean that someone else has already deleted the branch.

        ``` bash
        error: unable to push to unqualified destination: remoteBranchName The destination refspec neither matches an existing ref on the remote nor begins with refs/, and we are unable to guess a prefix based on the source ref. error: failed to push some refs to 'git@repository_name'
        ```

        Try to synchronize your branch list using:

        ``` bash
        git fetch -p
        ```

        The `-p` flag means "prune". After fetching, branches which no longer exist on the remote will be deleted.

=== "GitHub"

    To delete a branch on GitHub:

    1. Click on the branches button, highlighted in blue below and showing the number of branches we currently have (which is currently 4).

        ![Screenshot of the header menu of a github repo with the branches button currently highlighted](../../../images/github_delete_branch_1.png "The button you want is next to the branches drop down menu on the left, currently showing main as our current branch")

    2. This will bring up the branches page. Find the branch you wish to delete and click on the bin icon to the far right of it.

        ![Branches page with the delete button hovered on ready to be selected](../../../images/github_delete_branch_2.png "GitHub will clearly show you with the hover text which branch you are about to delete")

    3. This will instantly delete the branch. It will show as deleted on the branch page, however, it can be easily recovered with the `Restore` button on the far right. This is useful when you mistakenly delete a branch.

        ![Branches page showing the new-branch-name branch deleted with the Restore button to the right](../../../images/github_delete_branch_3.png "Click on the restore button to undo the delete")

=== "GitLab"

    To delete a branch on GitLab:

    1. First navigate to the branches page by going to the side-menu on the left, then `Repository` then `Branches`.

        ![](../../../images/gitlab_delete_branch_1.png)

    2. Search for the branch you wish to delete. When found, click the `Delete` bin icon to the right of the screen.

        ![](../../../images/gitlab_delete_branch_2.png)

    3. Clicking the bin icon will bring up a warning about deleting the branch. Read the warning to confirm you have got the correct branch and then click the red `Yes, delete branch` button.

        ![](../../../images/gitlab_delete_branch_3.png)

    4. This will delete the branch. The branches page of the repository will be shown with a delete confirmation banner. When searching for the deleted branch, no branch will be found.

        ![](../../../images/gitlab_delete_branch_4.png)

<!-- TODO: === "VS Code" -->

## Merging Branches

=== "Terminal"

    !!! warning "Remember to ensure local branches are up to date with their remote version"

        ```bash
        git checkout source-branch-name
        git pull
        git checkout target-branch-name
        git pull
        ```

        Or if you don't mind which branches are updated:

        ```bash title="Update all of your branches at once"
        git pull --all
        ```

    While all using the same `git merge` commands, there are a number of different merges that you might want to carry out:

    ```bash title="Updating a Feature Branch with changes in Main"
    git checkout feature/branch-name
    git merge main
    ```

    ```bash title="Merging your Feature Branch changes to Main"
    git checkout main
    git merge feature/branch-name
    ```

    ```bash title="Merging one branch into another"
    git checkout target-branch-name
    git merge source-branch-name
    ```

    When merging, if Git detects a conflict, it will stop the merge and raise and error that would look like the following:

    ```bash
    Auto-merging practice/temperatures_function.py
    CONFLICT (content): Merge Conflict in practice/temperatures_function.py
    Automatic merge failed; fix conflicts and then commit the result.
    ```

    If this occurs, then continue on to look at our walkthrough on [resolving merge conflicts](#resolving-merge-conflicts)

=== "GitHub"

    Merging on GitHub is done through pull requests, [see our walkthrough for more instructions](./pull_and_merge_requests_walkthrough.md).

=== "GitLab"

    Merging on GitLab is done through merge requests, [see our walkthrough for more instructions](./pull_and_merge_requests_walkthrough.md).

<!-- TODO: === "VS Code" -->

### Resolving Merge Conflicts

=== "Terminal"

    When merging, if Git detects a conflict, it will stop the merge and raise an error that would look like the following:

    ```bash
    Auto-merging practice/temperatures_function.py
    CONFLICT (content): Merge Conflict in practice/temperatures_function.py
    Automatic merge failed; fix conflicts and then commit the result.
    ```

    To resolve this error, we are going to find out where the merge conflicts are happening, make a choice of which version of changes to keep (which can be both), before staging the file and completing the merge with a commit (which we can then push).

    1. To find the offending file, we look at the second line of the conflict error where it is listed: `practice/temperatures_function.py`.

    2. Open the file(s) in an editor of your choosing and look for the conflicting section of the document:

        ``` title="The conflict will look something like this:"
        <<<<<< HEAD
        This line is the line in my branch.
        =======
        This line is the line in main.
        >>>>>> main
        ```

    3. Delete the content that you do not wish to keep, including the arrows and double lines.

        ``` title="If we only wished to keep changes from our branch the result will look like this:"
        This line is the line in my branch.
        ```

    4. Search for any remaining conflicts in this file and other files.
    5. Once you have found and corrected all of them, save your changes and update your branch in the usual way:

        ```bash
        git status # (1)!
        git add .
        git status
        git commit -m "Merge branch 'source-branch-name' into 'target-branch-name'" # (2)!
        git status
        git push
        ```

        1. The `git status` commands are not required, but is good practice to keep track of the current state of the repository to understand what you have done.
        2. This is an example of a good merge commit message, but you can use whatever message you want

=== "GitHub"

    When you create a Pull Request in GitHub it will check the compatibility of the two branches (base and source) and detect if there are any merge conflicts that are expected to occur.

    If it does find conflicts, it will not allow the merge to proceed until they are resolved. To resolve the conflicts:

    1. First, click on the `Resolve conflicts` button on the right of the "This branch has conflicts that must be resolved" message box.

        ![A conflicting Pull Request will have a message towards the bottom detailing the merge health. In this image it is showing a conflict in the README.md file.](../../../images/github_resolving_merge_conflicts_1.png "A conflicting Pull Request will have a message towards the bottom detailing the merge health. In this image it is showing a conflict in the README.md file.")

    2. This will bring up the conflict resolution page. Select a file with a conflict in it and find the conflicting section:

        ``` title="The conflict will look something like this:"
        <<<<<< HEAD
        New change on feature branch
        =======
        Conflicting change on target branch
        >>>>>> main
        ```

        ![](../../../images/github_resolving_merge_conflicts_2.png)

    3. Delete the content that you do not wish to keep, including the arrows and double lines. Navigate to the next conflict with the `Next v` botton. Once all conflicts in a file are resolved then the `Mark as resolved` button will become available. Click the button.

        ![All conflicts have been removed from the file and the Mark as Resolved button is available](../../../images/github_resolving_merge_conflicts_3.png)

    4. A green checkmark will appear next to the file you have resolved. Resolve all other files and a green `Commit merge` button will appear at the top of the Merge Editor space. Commit the merge.

        ![All files are resolved and the merge can now be committed](../../../images/github_resolving_merge_conflicts_4.png)

    5. Once the merge has been completed, the merge health section of the PR will show as green and healthy (assuming there are not any more review steps to go through)

        ![The merge health section showing as green and notifying the user that there are no conflicts](../../../images/github_resolving_merge_conflicts_5.png).

=== "GitLab"

    When you create a Merge Request in GitLab it will check the compatibility of the two branches (base and source) and detect if there are any merge conflicts that are expected to occur.

    If it does find conflicts, it will not allow the merge to proceed until they are resolved. To resolve the conflicts:

    1. First click on the blue `Resolve Conflicts` button to the right of the "Merge blocked: merge conflicts must be resolved" message.

        ![](../../../images/gitlab_merge_conflict_1.png)

    2. This will open up the Merge Conflicts editor which has two different mode, Interactive or Edit Inline. Select the option that best works for you.

    === "Interactive Mode"

        3. For each conflict, the changes from each branch will be shown in green for "ours" or the source branch and blue for "theirs" or the target branch over the overall merge. To the right there are buttons to select which version to use. Select the appropriate version.

            ![](../../../images/gitlab_merge_conflict_2.png)

        4. Once all conflicts are resolved, the blue `Commit to source branch` will become available. Make any changes you wish to the commit message and commit the merge.

            ![](../../../images/gitlab_merge_conflict_3.png)

    === "Inline Mode"

        3. Each conflict will be marked something like this:

            ```
            <<<<<< HEAD
            New change on feature branch
            =======
            Conflicting change on target branch
            >>>>>> main
            ```

            ![](../../../images/gitlab_merge_conflict_2b.png)

        4. Delete the content that you do not wish to keep, including the arrows and double lines.
        5. Once all conflicts are resolved, the blue `Commit to source branch` will become available. Make any changes you wish to the commit message and commit the merge.

            ![](../../../images/gitlab_merge_conflict_3b.png)

    Once the merge conflicts have been resolved and committed, you will return to the merge request. A banner at the top will confirm all conflicts have been resolved and the previous "Merge blocked: merge conflicts must be resolved" message box will now show "Ready to merge!".

    ![](../../../images/gitlab_merge_conflict_4.png)

    ![](../../../images/gitlab_merge_conflict_5.png)

<!-- TODO: === "VS Code" -->
