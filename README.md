# cli

* how to set up a python app with cli
* how to install a package that can be run from the shell

## install the package

```bash
python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip

pip install -r requirements_test.txt

pip install -e src
```

Check it has installed the package by trying:

```bash
pip install ipython
ipython
import midnyte.sample.instances
midnyte.sample.instances.get_instances()
```

Should also be able to invoke module from commandline:

```bash
midnyte_sample
```
