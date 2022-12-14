## Description
Downloading tool for information about open positions of futures on MOEX Exchange. 

## Features
Downloading the following information from MOEX Exchange:
- Total count of open long and short positions by type of traders (Juridical or Physical).  
- Total count of traders by type Juridical or Physical.  

## Start
### Dependencies
- [Requests project](https://pypi.org/project/requests/)
<!-- termynal -->
```
$ pip install requests
```

### Required configuration (minimal)
1. Open [settings.ini](settings.ini) file
2. Specify futures contract name `CONTRACT` (section `DATA_COLLECTION`)
3. Specify requesting date: `DAY`, `MONTH`, `YEAR` (section `DATA_COLLECTION`)
4. Run main.py

or specify the same information via command line arguments:

`--contract` futures contract name

`--day` day of requesting date

`--month` month of requesting date

`--year` year of requesting date


### Tested environments
Recommendation is to use python 3.10 or more. 

## Configuration
Configuration can be specified via [settings.ini](settings.ini) file.
### Section DATA_COLLECTION
Do not change `TYPE` (it's a constant at this moment).  

Specify futures contract name `CONTRACT` 

Specify requesting date: `DAY`, `MONTH`, `YEAR`

### Section DATA_COLLECTION_SETTINGS
Settings for retry attempts in case of some errors.

Specify interval in seconds between retry attempts `RETRY_INTERVAL_SEC` 

Specify count of retry attempts `RETRY_INTERVAL_COUNT`

## Use case
Main goal is download and keep information for internal purposes, such as manual analyze,  
trading ideas or strategies, ML purposes etc.

## Logging
All logs are written in logs/collector.log.
Any kind of settings can be changed in main.py code

## Docker
The Dockerfile is [here](Dockerfile).

Run example: 

sudo docker run -i image_name:tag --contract=RTS --day=1 --month=12 --year=2022 


## Project change log
[Here](CHANGELOG.md)

## Disclaimer
The author is not responsible for any errors or omissions, or for the trade results obtained from the use of this tool. 
