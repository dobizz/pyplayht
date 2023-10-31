# pyplayht

Python wrapper for PlayHT API
https://docs.play.ht/reference/api-getting-started

### Installation
```bash
pip install pyplayht
```

### Environmental Variables
Get your keys from https://play.ht/app/api-access
| Name | Value |
| --- | --- |
| `PLAY_HT_USER_ID` | account user id |
| `PLAY_HT_API_KEY` | account secret key |

### Sample Code
```python
from pathlib import Path

from pyplayht.classes import Client

# create new client
client = Client()

# create new conversion job
job = client.new_conversion_job(
    text="Hello, World!",
    voice="en-US-JennyNeural",
)

# check job status
job = client.get_coversion_job_status(job.get("transcriptionId"))

# download audio from job
data = client.download_file(job.get('audioUrl'))

# do something with audio bytes
path = Path("demo.mp3")
path.write_bytes(data)
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
