# Server Stats
### Application for tracking resources consumed by a remote server

## Requirements
python ^3.12, but in fact it will run on any version above 3.10, and with skillful hands - starting from 3.8


## Before starting
* Install poetry
```$ pip install poetry```
* installing dependencies
```$ poetry install```

## Using
* Create a **.env** file in the `$ cd src` directory

* Fill in the fields **DISCORD_URL** & **DISCORD_DELAY**
*for example:*
```
DISCORD_URL="https://discordapp.com/api/webhooks/YOUR-API-KEY" 
DISCORD_DELAY=1 (ms)
```
* Run! `$ poetry run run.py`
