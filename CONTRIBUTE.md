# Contribute

Hi there! We're thrilled that you'd like to contribute to the RAP Community of Practice! Your help is crucial in keeping it great!

## Creating an issue

If you think of something worth including, improving, or want to contribute, please [raise an issue on GitHub](https://github.com/NHSDigital/rap-community-of-practice/issues).

## Submitting a pull request

If you want to contribute to our resources:

1. [Fork][fork] or clone the repository
2. Configure and install the dependencies if you want to run the page in your machine, otherwise none.
3. Create a new branch: (e.g. `git checkout -b my-branch-name`)
4. Make your change
5. Check how your change looks on our website by hosting the website locally (follow [the steps below](#contribute-to-rap-community-of-practice-website) on how to do this)
6. Push to your fork and [submit a pull request][pr]

Your pull request will then be reviewed. You may receive some feedback and suggested changes before it can be approved and your pull request merged. 

To increase the likelihood of your pull request being accepted:

- If you are making visual changes, include a screenshot of what the affected element looks like, both before and after.
- Follow the [style guide][style].
- Keep your change as focussed as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write [good commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Contribute to RAP Community of Practice Website

### Via Github Codespaces
The **easiest way is just to open the repo in [Github Codespaces](https://github.com/features/codespaces)** - you can then make your changes, run the website to check it, and commit those back all within a VSCode environment running a fresh Python install.

### Working locally

If you don't want to use Github codespaces (or can't because it's blocked, or you've run out of credits), then you can make changes to the repo locally on your machine.

#### Requirements

It's probably most ideal to work on a linux envirnoment, but any machine which can run Python and is connected to the internet should be ok.

#### Making a Python environment and installing dependencies

You'll need to make the same environment that we use to run the website.

1. Make a `venv` and install the python libraries found in our `requirements.txt`
    * We have a [great little guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/virtual-environments/venv/) on how to do the above!
1. Activate the `venv` and in the command line run: `mkdocs serve` (depending on how your python install is setup, this might need to be `python -m mkdocs serve`) 
1. Open up http://127.0.0.1:8000/ in your browser, and you'll see the [RAP Community of Practice home page](https://nhsdigital.github.io/rap-community-of-practice/) being displayed with your updates applied.
    * Read more: [Getting Started with MkDocs](https://www.mkdocs.org/getting-started/#getting-started-with-mkdocs)

### Editing the contents

To add a new page to the website, you can add the file as you would normally and then update 'nav' in mkdocs.yml to include the file within the nested list. Don't forget to check that the links, images, headings, and contents are all working correctly on both the website and in the GitHub repo.

All of the files accessed via the website are nested within the 'docs' folder.

The website currently uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) theme. This sets the layout, colour, font, search bar, header, footer, navigation bar and contents. You can follow the documentation to make any changes (e.g. change the [colour scheme](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)) as it is simple to use and also easy to overwrite. There is a separate stylesheet, [extra.css](./docs/stylesheets/extra.css), which is used to overwrite the colours, fonts and some of the sizing for some elements.
Here is a good [cheat sheet](https://yakworks.github.io/docmark/cheat-sheet/) for what features can be used in MkDocs and also interesting features in [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/).

## Resources

- [Contributing to Projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
- [Using Pull Requests](https://help.github.com/articles/using-pull-requests/)
- [GitHub Help](https://help.github.com)

[fork]: https://github.com/pages-themes/slate/fork
[pr]: https://github.com/pages-themes/slate/compare
[style]: http://ben.balter.com/jekyll-style-guide/
