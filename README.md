# WeatherFetcherSystem

v1.0
  - First Version

Demo:
  - URL: https://app.chiaying.wang/dashboard/ (HTTPS Required)
  - Username: demo
  - Password: chiayingwang

# Features!

  - Get Weather data from CWB per hour
  - Member System
  - RESTful API

### Tech

WeatherFetcherSystem uses those projects to work properly:

* [Python] - Backend
* [jQuery] - Frontend
* [SQLite] - Database


### System Requirement

* [Python] - v3.6+
* [OS] - Linux (CentOS 7 is recommend)
* [SQLite] - v3
* [pip] - v19
* [Django] - 1.11
* [Apache] - 2.4
* [Mod_wsgi] - 4.6.4

### Plugins

WeatherFetcherSystem is currently extended with the following plugins. 

| Plugin | Version |
| ------ | ------ |
| certifi       | 2019.6.16 |
| chardet      | 3.0.4 |
| Django    | 1.11.22 |
| django-crontab | 0.7.1 |
| idna         | 2.8 |
| pip        | 19.1.1 |
| pytz          | 2019.1 |
| requests     | 2.22.0 |
| setuptools    | 41.0.1 |
| sqlparse           | 0.3.0 |
| urllib3      | 1.25.3 |
| wheel   | 0.33.4 |


### RESTful API


##### Login API 

###### Request
`POST: https://app.chiaying.wang/api/login/?username=demo&password=chiayingwang`

| Key | Type | Required | Info |
| ------ | ------ | ------ | ------ |
| username | string | Y | Username |
| password | string | Y | Password |

###### Response

| Key | Type  | Info |
| ------ | ------ | ------ | 
| status | int | Status Code |
| data | string | Infomation |


##### Weather API 

###### Request
`GET: https://app.chiaying.wang/api/weather/?username=demo&password=chiayingwang&city=06`

| Key | Type | Required | Info |
| ------ | ------ | ------ |------ |
| username | string | Y | Username |
| password | string | Y | Password |
| city | string | Y | City Number (Taipei:01/New Taipei:06/Taoyuan:08) |

###### Response

| Key | Type  | Info |
| ------ | ------ | ------ | 
| status | int | Status Code |
| data | JSON Array | infomation |

Data JSON Array Struct

| Key | Type  | Info |
| ------ | ------ | ------ | 
| model | int | Model |
| pk | int | Primary Key |
| fields.city | string | City Number |
| fields.temp | float | Temperature |
| fields.humd | float | Humidity |
| fields.pres | float | Pressure |
| fields.wdir | float | Wind Direction |
| fields.wdsd | float | Wind Speed |
| fields.recordTime | string | Record Time |


**2019 © Ian Chiaying Wang**

