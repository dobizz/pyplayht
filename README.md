# pyplayht

Python wrapper for PlayHT API
https://docs.play.ht/reference/api-getting-started

### Installation
```bash
pip install pyplayht
```


### Developer Instructions
Run the dev setup scripts inside `scripts` directory
```bash
├── scripts
│   ├── setup-dev.bat # windows
│   └── setup-dev.sh # linux
```

Install the `pyplayht` package as editable
https://setuptools.pypa.io/en/latest/userguide/development_mode.html
```bash
pip install -e .
```

When making a commit, use the command `cz commit` or `cz c`

You may also use the regular `git commit` command but make sure to follow the `Conventional Commits` specification
https://www.conventionalcommits.org/en/v1.0.0/
