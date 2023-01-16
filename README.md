# dox-cli (alpha)

Cli to create project structure from a pre-defined YAML template.

There are lots of predefined template comes with the tool, you can also use your own templates as per your requirement.

## Quick start

This project is in `alpha` stage, so install with custom Python environment.

If you already know how to install python packages, then you can simply do:

```shell
$ pip install doxcli
```

If you don't know how to install python packages, please check the [detailed instructions](https://pip.pypa.io/en/latest/installation/).

## Usage

```shell
dox [template_name] [destination]
```

Examples:

```shell
# Make sure the destination directory exists
$ dox next ~/Code/nextjs-app
```

For more details

```shell
$ dox --help

Usage: dox [template name] [destination] [--options]

Options:
  # TODO
```

## Config

A config file is automatically created at `~/.config/doxcli/config` at first launch. See the file itself for a description of all available options.


## Contributions

If you're interested in contributing to this project, first of all I would like to extend my heartfelt gratitude. I've written a small doc to describe how to get this running in a development setup.

Please feel free to reach out to me if you need help.
My email: imbijaydas@gmail.com, Twitter: [`@imbijaydas`](https://twitter.com/imBijayDas)
