# cloudmersive_dataintegration_api_client.BackupConvertApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataintegration_backup_convert_mssql_bak_get_tables_post**](BackupConvertApi.md#dataintegration_backup_convert_mssql_bak_get_tables_post) | **POST** /dataintegration/backup/convert/mssql/bak/get/tables | Lists all tables stored in a SQL Server Backup (.BAK) file
[**dataintegration_backup_convert_mssql_bak_to_csv_post**](BackupConvertApi.md#dataintegration_backup_convert_mssql_bak_to_csv_post) | **POST** /dataintegration/backup/convert/mssql/bak/to/csv | Converts a SQL Server Backup (.BAK) file into CSV for a specified table


# **dataintegration_backup_convert_mssql_bak_get_tables_post**
> MssqlBakEnumerateTablesResult dataintegration_backup_convert_mssql_bak_get_tables_post(input_file=input_file)

Lists all tables stored in a SQL Server Backup (.BAK) file

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on | [optional] 

### Return type

[**MssqlBakEnumerateTablesResult**](MssqlBakEnumerateTablesResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataintegration_backup_convert_mssql_bak_to_csv_post**
> str dataintegration_backup_convert_mssql_bak_to_csv_post(table_name=table_name, input_file=input_file)

Converts a SQL Server Backup (.BAK) file into CSV for a specified table

Input the target table to extract the data as a CSV format file.  Supports a wide array of SQL Server .BAK files and SQL Server backup file versions.  Consumes 1 API call per MB of input data.

### Example
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
table_name = 'table_name_example' # str | Name of the table to return (optional)
input_file = '/path/to/file.txt' # file | Input file to perform the operation on (optional)

try:
    # Converts a SQL Server Backup (.BAK) file into CSV for a specified table
    api_response = api_instance.dataintegration_backup_convert_mssql_bak_to_csv_post(table_name=table_name, input_file=input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupConvertApi->dataintegration_backup_convert_mssql_bak_to_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of the table to return | [optional] 
 **input_file** | **file**| Input file to perform the operation on | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

