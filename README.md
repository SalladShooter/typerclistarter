# Typer CLI Starter

### Installation 

```bash
git clone https://github.com/SalladShooter/typerclistarter.git my-cli
cd my-cli
```

> If you do not have Typer install it as such
> ```bash
> pip install typer
> ```

### Includes

- `pyproject.toml` for easy uploads to PyPI or elswhere
- `my-package/` for containing all of the logic of your CLI
- `main.py` for containing the Typer app
- `commands/` for all of the commands to run in your package
- `LICENSE.txt` for a blank license

### Test your CLI

You can install/reinstall your CLI on your machine via:

```bash
pip install -e .
```

And then you can run the CLI as a normal terminal command!

### Publishing

Want to upload to PyPI? Use Twine!

```bash
pip install build twine
python -m build
twine upload dist/*
```
