# cloudmersive_dataintegration_api_client.AudioApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audio_convert_to_aac**](AudioApi.md#audio_convert_to_aac) | **POST** /audio/convert/to/aac | Convert Audio File to AAC format.
[**audio_convert_to_m4a**](AudioApi.md#audio_convert_to_m4a) | **POST** /audio/convert/to/m4a | Convert Audio File to M4A format.
[**audio_convert_to_mp3**](AudioApi.md#audio_convert_to_mp3) | **POST** /audio/convert/to/mp3 | Convert Audio File to MP3 format.
[**audio_convert_to_wav**](AudioApi.md#audio_convert_to_wav) | **POST** /audio/convert/to/wav | Convert Audio File to WAV format.


# **audio_convert_to_aac**
> str audio_convert_to_aac(input_file=input_file, file_url=file_url, bit_rate=bit_rate)

Convert Audio File to AAC format.

Automatically detect audio file format and convert it to AAC format. Supports many input audio formats, including AAC, FLAC, M4A, MP2, MP3, OGG, WMA, and WAV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.AudioApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. (optional)
bit_rate = NULL # object | Optional; Specify the desired bitrate of the converted audio file in kilobytes per second (kB/s). Value may be between 48 and 1,411. By default, the optimal bitrate will be chosen automatically. (optional)

try:
    # Convert Audio File to AAC format.
    api_response = api_instance.audio_convert_to_aac(input_file=input_file, file_url=file_url, bit_rate=bit_rate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->audio_convert_to_aac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **bit_rate** | [**object**](.md)| Optional; Specify the desired bitrate of the converted audio file in kilobytes per second (kB/s). Value may be between 48 and 1,411. By default, the optimal bitrate will be chosen automatically. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_convert_to_m4a**
> str audio_convert_to_m4a(input_file=input_file, file_url=file_url, bit_rate=bit_rate)

Convert Audio File to M4A format.

Automatically detect audio file format and convert it to M4A format. Supports many input audio formats, including AAC, FLAC, M4A, MP2, MP3, OGG, WMA, and WAV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.AudioApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. (optional)
bit_rate = NULL # object | Optional; Specify the desired bitrate of the converted audio file in kilobytes per second (kB/s). Value may be between 48 and 1,411. By default, the optimal bitrate will be chosen automatically. (optional)

try:
    # Convert Audio File to M4A format.
    api_response = api_instance.audio_convert_to_m4a(input_file=input_file, file_url=file_url, bit_rate=bit_rate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->audio_convert_to_m4a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **bit_rate** | [**object**](.md)| Optional; Specify the desired bitrate of the converted audio file in kilobytes per second (kB/s). Value may be between 48 and 1,411. By default, the optimal bitrate will be chosen automatically. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_convert_to_mp3**
> str audio_convert_to_mp3(input_file=input_file, file_url=file_url, bit_rate=bit_rate)

Convert Audio File to MP3 format.

Automatically detect audio file format and convert it to MP3 format. Supports many input audio formats, including AAC, FLAC, M4A, MP2, MP3, OGG, WMA, and WAV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.AudioApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. (optional)
bit_rate = NULL # object | Optional; Specify the desired bitrate of the converted audio file in kilobytes per second (kB/s). Value may be between 48 and 1,411. By default, the optimal bitrate will be chosen automatically. (optional)

try:
    # Convert Audio File to MP3 format.
    api_response = api_instance.audio_convert_to_mp3(input_file=input_file, file_url=file_url, bit_rate=bit_rate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->audio_convert_to_mp3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **bit_rate** | [**object**](.md)| Optional; Specify the desired bitrate of the converted audio file in kilobytes per second (kB/s). Value may be between 48 and 1,411. By default, the optimal bitrate will be chosen automatically. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_convert_to_wav**
> str audio_convert_to_wav(input_file=input_file, file_url=file_url, sample_rate=sample_rate)

Convert Audio File to WAV format.

Automatically detect audio file format and convert it to WAV format. Supports many input audio formats, including AAC, FLAC, M4A, MP2, MP3, OGG, WMA, and WAV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.AudioApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. (optional)
sample_rate = NULL # object | Optional; Specify the desired sample rate of the converted audio file in kHz. Value may be between 8 and 96. Standard for audio CDs is 44.1, while DVD audio standard is 48. By default, the optimal sample rate will be chosen automatically. (optional)

try:
    # Convert Audio File to WAV format.
    api_response = api_instance.audio_convert_to_wav(input_file=input_file, file_url=file_url, sample_rate=sample_rate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->audio_convert_to_wav: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of an audio file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **sample_rate** | [**object**](.md)| Optional; Specify the desired sample rate of the converted audio file in kHz. Value may be between 8 and 96. Standard for audio CDs is 44.1, while DVD audio standard is 48. By default, the optimal sample rate will be chosen automatically. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

