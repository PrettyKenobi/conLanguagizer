# conLanguagizer

[![Documentation Status](https://readthedocs.org/projects/conlanguagizer/badge/?version=latest)](https://conlanguagizer.readthedocs.io/en/latest/?badge=latest)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)

A digital binder for you constructed language. Keep track of your conlang's phonology, orthography, and word definitions with a dictionary. Organize the rules of your language in the grammar. You can define them using the [regular expression](https://en.wikipedia.org/wiki/Regular_expression) method or the more human readable cLa syntax. conLanguagizer can then apply the grammar to one or more words in the dictionary so you don't have to conjugate yourself!

## Project Goals

1. An easy-to-use and powerful tool for creating and organizing a lexicon and grammar for a conlang
1. Fully accessible

## Contributing

Thank you for wanting to help! First, please read our [Code Of Conduct](https://conlanguagizer.readthedocs.io/en/latest/CODE_OF_CONDUCT.html). Then look [here](https://conlanguagizer.readthedocs.io/en/latest/contributing.html) for ideas on how you can contribute and how to do so.

## Cloning and Running the Source Code

Whether you're looking to contribute or tinker for your own enjoyment, below are the steps to get you started.

### Code Prerequisites

- [Node.js](TODO create and link to doc on installing)
- [yarn](TODO create and link to doc on installing)

---

Before you clone, navigate your terminal to the directory you want to be the parent for the project. (Aka the folder the conLanguagizer folder will live in.)
Once that's done, do the following commands:

```bash
mkdir my-folder
cd my-folder
git clone https://github.com/PrettyKenobi/conLanguagizer.git .
```

Before you can run the app first time you'll need to run `yarn build` to locally install the app's dependencies and create its dependency tree. Depending on your internet's speed and your machine's connectivity this can take more than 10 minutes.

To actually run the code type `yarn dev` and a new window should open.

## Building the Documentation

We write most of our documentation pages in [reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) and host them [Read the Docs](https://readthedocs.org). Read the Docs converts (builds) these pages to html whenever we merge a PR (TODO link to info on pull requests) into any of the branches. If you edit the documentation though, you should see if it will build before you make a PR.
To do this, we use the same utility Read the Docs does, called [Sphinx](https://www.sphinx-doc.org/en/master/index.html).

### Documentation Prerequisites

- [Python 3](TODO Link to instructions under dev documentation)
- [Sphinx](TODO Link to instructions under dev documentation)
  - Plugins: (TODO Add sphinx plugin names here and include them in requirements.txt)

Follow the steps under [Cloning and Running the Source Code](#cloning-and-running-the-source-code) to clone the project. Next navigate to the documentation folder with `cd './docs`.

The command to build the documentation is `make html`.

Your terminal will display some logging output from Sphinx. If everything went well the last line will start with `build succeeded`. Congratulations! To explore the output insert the full path of `./_build/html/index.html` into your browser's address bar.

## Built with

- [Electron React Boilerplate](https://github.com/electron-react-boilerplate)

## Authors

- **Ken Bonnstetter** [PrettyKenobi](https://github.com/PrettyKenobi) - _Initial work_

## License

MIT - _See [LICENSE] for details_

## Acknowledgements

- Inspired by Polyglot (TODO: link) by (TODO: lookup author)
