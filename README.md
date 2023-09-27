# cron-parser
# Cron String Parser

This is a Python script that parses standard cron strings and expands each field to show the times at which it will run. The script handles the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command. It also supports non-standard extensions like "MON-FRI" for day of the week 

## Usage

To use this script, you can run it from the command line with a cron string as an argument. For example:

```bash
python src/main/cron_parser.py "*/15 0 1,15 * MON-FRI /usr/bin/find"

for test cases to run use the command
```bash
pytest

Create virtual environment
pipenv shell
pipenv sync


