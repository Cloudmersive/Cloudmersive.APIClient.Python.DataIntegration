# cloudmersive_dataintegration_api_client
Easily and directly query database backup files, convert into other file formats.

This Python package provides a native API client for [Cloudmersive Data Integration](https://cloudmersive.com/data-integration-api)

- API version: v1
- Package version: 3.0.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_dataintegration_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_dataintegration_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudmersive_dataintegration_api_client
from cloudmersive_dataintegration_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_dataintegration_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_dataintegration_api_client.BackupConvertApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on (optional)

try:
    # Lists all tables stored in a SQL Server Backup (.BAK) file
    api_response = api_instance.dataintegration_backup_convert_mssql_bak_get_tables_post(input_file=input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupConvertApi->dataintegration_backup_convert_mssql_bak_get_tables_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BackupConvertApi* | [**dataintegration_backup_convert_mssql_bak_get_tables_post**](docs/BackupConvertApi.md#dataintegration_backup_convert_mssql_bak_get_tables_post) | **POST** /dataintegration/backup/convert/mssql/bak/get/tables | Lists all tables stored in a SQL Server Backup (.BAK) file
*BackupConvertApi* | [**dataintegration_backup_convert_mssql_bak_to_csv_post**](docs/BackupConvertApi.md#dataintegration_backup_convert_mssql_bak_to_csv_post) | **POST** /dataintegration/backup/convert/mssql/bak/to/csv | Converts a SQL Server Backup (.BAK) file into CSV for a specified table


## Documentation For Models

 - [MssqlBakEnumerateTablesResult](docs/MssqlBakEnumerateTablesResult.md)
 - [MssqlTable](docs/MssqlTable.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



