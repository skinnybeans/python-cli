# cli

Little sample project to show how to build and install a python CLI app.

Geting up and running with `argparse` isn't difficult, however when it comes to implementing subcommands there are not obvious patterns to use.

This project also has the necessary setup to be installed as a package, this helps:

- Running tests (you don't need to have tests in the same location as your code)
- Running from the command line (you can invoke it like a normal program)
- Testing functions using python interpreter (you can import the package and test out functions)

## Setup

First, set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Update pip and install testing requirements

```bash
pip install --upgrade pip

pip install -r requirements_test.txt
```

Install this package in development mode:

```bash
pip install -e src
```

## Using the module

You should now be able to access the code in here like any other python package.
For example, from ipython:

```bash
# install ipython
pip install ipython

# run ipython
ipython

# import the package and call a function
import midnyte.sample.instances
midnyte.sample.instances.get_instances()
```

## Invoking from command line

Should also be able to invoke module from commandline:

```bash
midnyte_sample
```

## Running tests

You can now import and use the module for testing through pytest.

The `test` directory is completely seperate from the `src` directory, but can still import the module.

```bash
pytest
```

## Creating sub-commands

If you take a look into `midnyte/cli.py` you can see how the subcommands get set up.

Each subcommand get implemented as a subparser, and each subparser can have it's own seperate list of arguments.

For this sample application, there are two subcommands:

- instances
- ami

If you type in:

```bash
midnyte_sample -h
```

You will see the subcommands listed in the help.

You can get further help on each of these commands:

```bash
midnyte_sample instances -h
```

will list help for that specific subcommand.

The file `midnyte/command.py` contains an interface that can be used for adding subcommands.

The implementation of this interface can be seen in `midnyte/sample/ami.py` and `midnyte/sample/instances.py`
This is designed to give an easy way to add new commands.
