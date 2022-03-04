# argparse

testing how to call functions based on subparser commands issued

## install the package

```bash
python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip

pip install -r test_requirements.txt

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
