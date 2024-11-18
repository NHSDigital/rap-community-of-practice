---
title: Git Hooks

tags: 
  - Git
  - Version control
---

#

!!! tip "TLDR"

    - Git hooks are scripts that run automatically every time a particular event occurs in a Git repository.
    - Git hooks can automate virtually any aspect of your workflow.
    - Git hooks can detect secrets in your code.
    - This is a Gold Level RAP guide.

??? success "Pre-requisites"

    |Pre-requisite | Importance | Note |
    |--------------|------------|------|
    |[Intro to Git][introduction-to-git]|Necessary|This guide assumes you are using Git to version control|
    |[Using Git collaboratively][using-git-collaboratively]|Helpful|Get started using Git as a team|

## What are Git hooks?

Git hooks are scripts that run automatically every time a particular event occurs in a Git repository. They let you customize Git’s behavior and trigger actions at key points in development.

Since scripts are infinitely customizable, you can use Git hooks to automate or optimize virtually any aspect of your development workflow. Some example hook scripts include:

- pre-commit: Check commit messages for spelling errors.
- pre-receive: Enforce project coding standards.
- post-receive: Push code to production.
- post-release: Publish a packaged repository to PyPI.

## Why use Git hooks?

Git hooks can greatly increase your productivity as a developer. They can be written in any language and their biggest advantage is workflow automation. For example, you can use a Git hook to check that commit messages follow a standard and prevent the commit from executing. However, if you still want to commit, you can simply skip or override it.

When you add a hook to your local Git repository, it will not impose any policy outside of it as the hooks are stored in the `.git/hooks` directory which is ignored by Git by default.

The most important use of Git hooks is secret detection. Git hooks allow developers to easily and automatically detect any vulnerable secrets in their source code. The [govcookiecutter][govcookiecutter-repo] template repository already has secret detection integrated in it.

## How to use Git hooks

This guide will make use of the `pre-commit` and `detect-secrets` packages to quickly and easily use "out-of-the-box" pre-commit plugins.

### Installation

To install the `pre-commit` and `detect-secrets` packages, [first create and activate a virtual environment][venv] for your project, then open a terminal and enter:

``` 
pip install pre-commit detect-secrets
```

!!! note

    Don't forget to add `pre-commit` and `detect-secrets` to your `requirements.txt` file

### Configuration

To set up `pre-commit`, create a file named `.pre-commit-config.yaml` and add the following:

!!! example ".pre-commit-config.yaml"

    ``` yaml
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

    -   repo: https://github.com/kynan/nbstripout
        rev: 0.6.1
        hooks:
        -   id: nbstripout

    -   repo: https://github.com/Yelp/detect-secrets
        rev: v1.4.0
        hooks:
        -   id: detect-secrets
            args: ['--baseline', '.secrets.baseline']
    ```

This basic configuration will:

- Trim trailing whitespace.
- Make sure files end in a newline and only a newline.
- Attempt to load all yaml files to verify syntax.
- Prevent large files from being added.
- Strip output from Jupyter and IPython notebooks.
- Detect secrets.

!!! note

    See the [pre-commit documentation][pre-commit-docs] and the [pre-commit hooks][pre-commit-hooks] to configure and find compatible plugins.

### Baseline

To create a baseline of potential secrets currently found in your repository, open a terminal and enter:

```
detect-secrets scan > .secrets.baseline
```

!!! note

    See the [detect-secrets repository][detect-secrets-repo] for details on its full feature set.

### Usage

To update any Git hooks specified in the configuration file, open a terminal and enter:

```
pre-commit autoupdate
```

To install the Git hooks, open a terminal and enter:

```
pre-commit install
```

Now you're all set up to go! When you try to commit a change, the Git hooks will automatically run against any staged files and prevent the commit from completing if any fail.

!!! note

    You can also run your pre-commit Git hooks manually against all files by opening a terminal and entering:

    ```
    pre-commit run --all-files
    ```

## What if a commit is forced through a Git hook?

There are numerous ways to enforce project Git hooks. This guide will provide an example using GitHub Actions whenever a pull request has changes e.g. when a new pull request is created or when a commit is pushed to a pull request. This should trigger the workflow to run `pre-commit`.

Create a new GitHub Actions workflow file `.github/workflows/workflow-name.yaml` and add:

!!! example ".github/workflows/workflow-name.yaml"

    ``` yaml
    name: Pre-commit
    on:
    pull_request:

    jobs:
    pre-commit:
        name: Pre-commit
        runs-on: ubuntu-latest

        steps:
        - name: Checkout
            uses: actions/checkout@v3

        - name: Setup Python
            uses: actions/setup-python@v4

        - name: Install dependencies
            run: pip install pre-commit detect-secrets

        - name: Pre-commit
            run: pre-commit run --all-files        
    ```

## Useful Links

- [govcookiecutter: A template for data science projects][govcookiecutter-blog]
- [pre-commit documentation][pre-commit-docs]
- [detect-secrets repository][detect-secrets-repo]


[introduction-to-git]: ./introduction-to-git.md
[using-git-collaboratively]: ./using-git-collaboratively.md
[govcookiecutter-repo]: https://github.com/best-practice-and-impact/govcookiecutter
[python-website]: https://www.python.org/
[git-website]: https://git-scm.com/
[venv]: ../python/virtual-environments/venv.md
[pre-commit-docs]: https://pre-commit.com/
[pre-commit-hooks]: https://pre-commit.com/hooks.html
[detect-secrets-repo]: https://github.com/Yelp/detect-secrets
[govcookiecutter-blog]: https://dataingovernment.blog.gov.uk/2021/07/20/govcookiecutter-a-template-for-data-science-projects/
