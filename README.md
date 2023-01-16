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
- [psycopg2 project](https://pypi.org/project/psycopg2/)
<!-- termynal -->
```
$ pip install psycopg2
```

### Required configuration (minimal)
1. Open [settings.ini](settings.ini) file
2. Specify futures contract name `CONTRACT` (section `DATA_COLLECTION`)
3. Specify requesting date: `DAY`, `MONTH`, `YEAR` (section `DATA_COLLECTION`)
4. Specify requesting days range: `DAYS_RANGE` (section `DATA_COLLECTION`) - 
period of days from requesting date (can be negative or zero). 
Negative value is a past days, zero value is only requesting date, positive value is a future days.
5. Run main.py

or specify the same information via command line arguments:

`--contract` futures contract name

`--day` day of requesting date

`--month` month of requesting date

`--year` year of requesting date

`--range` period of days from requesting date (can be negative or zero)

### Tested environments
Recommendation is to use python 3.10 or more. 

## Configuration
Configuration can be specified via [settings.ini](settings.ini) file.
### Section DATA_COLLECTION
Do not change `TYPE` (it's a constant at this moment).  

Specify futures contract name `CONTRACT` 

Specify requesting date: `DAY`, `MONTH`, `YEAR`

Specify period of days from requesting date: `DAYS_RANGE`. Can be negative - past. Can be zero - only requesting date. 

### Section DATA_COLLECTION_SETTINGS
Settings for retry attempts in case of some errors.

Specify interval in seconds between retry attempts `RETRY_INTERVAL_SEC` 

Specify count of retry attempts `RETRY_INTERVAL_COUNT`

Specify interval in seconds between different days request `DELAY_BETWEEN_DAY_REQUESTS_SEC`

### Section DATA_STORAGE_PG
Enable or disable data storage by `ENABLED`. 0 is disabled, any no zero is enabled. 
Specify connection settings to PostgreSQL server: `HOST`, `PORT`, `USER`, `PASSWORD`, `DB`.


You can specify the same settings via command line arguments also:
`--pg_host`, `--pg_port`, `--pg_user`, `--pg_password`, `--pg_db`

## PostgreSQL server as data storage
At first please create appropriate tables via [script file](create_tables.sql).
All downloaded information will be stored into these tables.

## Use case
Main goal is download and keep information for internal purposes, such as manual analyze,  
trading ideas or strategies, ML purposes etc.

## Logging
All logs are written in logs/collector.log.
Any kind of settings can be changed in main.py code

## Docker
The Dockerfile is [here](Dockerfile).

Run example: 

sudo docker run -i image_name:tag -e "CONTRACT=CNY" -e "DAY=13" -e "MONTH=1" -e "YEAR=2023"

## K8s
[Here](helm-chart/README.md) is the chart for deployment the project on a [Kubernetes](http://kubernetes.io) cluster using 
the [Helm](https://helm.sh) package manager.

The project is configured and running as [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/). 

## Project change log
[Here](CHANGELOG.md)

## Disclaimer
The author is not responsible for any errors or omissions, or for the trade results obtained from the use of this tool. 
