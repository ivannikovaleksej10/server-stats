# Server Stats
### Application for tracking resources consumed by a remote server

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