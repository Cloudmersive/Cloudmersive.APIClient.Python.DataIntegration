# cloudmersive_dataintegration_api_client.VideoApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_convert_to_gif**](VideoApi.md#video_convert_to_gif) | **POST** /video/convert/to/gif | Convert Video to Animated GIF format.
[**video_convert_to_mov**](VideoApi.md#video_convert_to_mov) | **POST** /video/convert/to/mov | Convert Video to MOV format.
[**video_convert_to_mp4**](VideoApi.md#video_convert_to_mp4) | **POST** /video/convert/to/mp4 | Convert Video to MP4 format.
[**video_convert_to_still_frames**](VideoApi.md#video_convert_to_still_frames) | **POST** /video/convert/to/still-frames | Convert Video to PNG Still Frames.
[**video_convert_to_webm**](VideoApi.md#video_convert_to_webm) | **POST** /video/convert/to/webm | Convert Video to WEBM format.
[**video_cut_video**](VideoApi.md#video_cut_video) | **POST** /video/cut | Cut a Video to a Shorter Length
[**video_get_info**](VideoApi.md#video_get_info) | **POST** /video/convert/get-info | Get detailed information about a video or audio file
[**video_resize_video**](VideoApi.md#video_resize_video) | **POST** /video/resize/preserveAspectRatio | Resizes a Video Preserving the Original Aspect Ratio.
[**video_resize_video_simple**](VideoApi.md#video_resize_video_simple) | **POST** /video/resize/target | Resizes a Video without Preserving Aspect Ratio.
[**video_scan_for_nsfw**](VideoApi.md#video_scan_for_nsfw) | **POST** /video/scan/nsfw | Scan a Video for NSFW content.
[**video_split_video**](VideoApi.md#video_split_video) | **POST** /video/split | Split a Video into Two Shorter Videos


# **video_convert_to_gif**
> str video_convert_to_gif(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, start_time=start_time, time_span=time_span)

Convert Video to Animated GIF format.

Automatically detect video file format and convert it to animated GIF format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB. Default height is 250 pixels, while preserving the video's aspect ratio.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to 250 pixels, maximum is 500 pixels. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to 250 pixels, maximum is 500 pixels. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to 24 frames per second. (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired starting time of the GIF video in TimeSpan format. (optional)
time_span = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired length of the GIF video in TimeSpan format. Limit is 30 seconds. Default is 10 seconds. (optional)

try:
    # Convert Video to Animated GIF format.
    api_response = api_instance.video_convert_to_gif(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, start_time=start_time, time_span=time_span)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to 250 pixels, maximum is 500 pixels. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to 250 pixels, maximum is 500 pixels. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to 24 frames per second. | [optional] 
 **start_time** | **datetime**| Optional; Specify the desired starting time of the GIF video in TimeSpan format. | [optional] 
 **time_span** | **datetime**| Optional; Specify the desired length of the GIF video in TimeSpan format. Limit is 30 seconds. Default is 10 seconds. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_mov**
> str video_convert_to_mov(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality)

Convert Video to MOV format.

Automatically detect video file format and convert it to MOV format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)

try:
    # Convert Video to MOV format.
    api_response = api_instance.video_convert_to_mov(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_mov: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_mp4**
> str video_convert_to_mp4(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality)

Convert Video to MP4 format.

Automatically detect video file format and convert it to MP4 format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)

try:
    # Convert Video to MP4 format.
    api_response = api_instance.video_convert_to_mp4(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_mp4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_still_frames**
> StillFramesResult video_convert_to_still_frames(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, frames_per_second=frames_per_second)

Convert Video to PNG Still Frames.

Automatically detect video file format and convert it to an array of still frame PNG images. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
frames_per_second = NULL # object | Optional; How many video frames per second to be returned as PNG images. Minimum value is 0.1, maximum is 60. Default is 1 frame per second. Maximum of 2000 total frames. (optional)

try:
    # Convert Video to PNG Still Frames.
    api_response = api_instance.video_convert_to_still_frames(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, frames_per_second=frames_per_second)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_still_frames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **frames_per_second** | [**object**](.md)| Optional; How many video frames per second to be returned as PNG images. Minimum value is 0.1, maximum is 60. Default is 1 frame per second. Maximum of 2000 total frames. | [optional] 

### Return type

[**StillFramesResult**](StillFramesResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_webm**
> str video_convert_to_webm(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality)

Convert Video to WEBM format.

Automatically detect video file format and convert it to WEBM format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)

try:
    # Convert Video to WEBM format.
    api_response = api_instance.video_convert_to_webm(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_webm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_cut_video**
> str video_cut_video(input_file=input_file, file_url=file_url, start_time=start_time, time_span=time_span)

Cut a Video to a Shorter Length

Cuts a video to the specified start and end times. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired starting time of the cut video in TimeSpan format. (optional)
time_span = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired length of the cut video in TimeSpan format. Leave blank to include the rest of the video. Maximum time is 4 hours. (optional)

try:
    # Cut a Video to a Shorter Length
    api_response = api_instance.video_cut_video(input_file=input_file, file_url=file_url, start_time=start_time, time_span=time_span)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_cut_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **start_time** | **datetime**| Optional; Specify the desired starting time of the cut video in TimeSpan format. | [optional] 
 **time_span** | **datetime**| Optional; Specify the desired length of the cut video in TimeSpan format. Leave blank to include the rest of the video. Maximum time is 4 hours. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_get_info**
> MediaInformation video_get_info(input_file=input_file, file_url=file_url)

Get detailed information about a video or audio file

Retrieve detailed information about a video or audio file, including format, dimensions, file size, bit rate, duration and start time. Compatible with many formats, including: AVI, ASF, FLV, GIF, MP4, MPEG/MPG, Matroska/WEBM, MOV, AIFF, ASF, CAF, MP3, MP2, MP1, Ogg, OMG/OMA, and WAV. Uses 1 API call per 10 MB of file size.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)

try:
    # Get detailed information about a video or audio file
    api_response = api_instance.video_get_info(input_file=input_file, file_url=file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_get_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 

### Return type

[**MediaInformation**](MediaInformation.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_resize_video**
> str video_resize_video(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, frame_rate=frame_rate, quality=quality, extension=extension)

Resizes a Video Preserving the Original Aspect Ratio.

Resizes a video, while maintaining the original aspect ratio and encoding. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)
extension = 'extension_example' # str | Optional; Specify the file extension of the input video. This is recommended when inputting a file directly, without a file name. If no file name is available and no extension is provided, the extension will be inferred from the file data, which may cause a different extension to be used in the output. (optional)

try:
    # Resizes a Video Preserving the Original Aspect Ratio.
    api_response = api_instance.video_resize_video(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, frame_rate=frame_rate, quality=quality, extension=extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_resize_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 
 **extension** | **str**| Optional; Specify the file extension of the input video. This is recommended when inputting a file directly, without a file name. If no file name is available and no extension is provided, the extension will be inferred from the file data, which may cause a different extension to be used in the output. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_resize_video_simple**
> str video_resize_video_simple(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, frame_rate=frame_rate, quality=quality, extension=extension)

Resizes a Video without Preserving Aspect Ratio.

Resizes a video without maintaining original aspect ratio, allowing fully customizable dimensions. May cause image skewing. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)
extension = 'extension_example' # str | Optional; Specify the file extension of the input video. This is recommended when inputting a file directly, without a file name. If no file name is available and no extension is provided, the extension will be inferred from the file data, which may cause a different extension to be used in the output. (optional)

try:
    # Resizes a Video without Preserving Aspect Ratio.
    api_response = api_instance.video_resize_video_simple(input_file=input_file, file_url=file_url, max_width=max_width, max_height=max_height, frame_rate=frame_rate, quality=quality, extension=extension)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_resize_video_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 
 **extension** | **str**| Optional; Specify the file extension of the input video. This is recommended when inputting a file directly, without a file name. If no file name is available and no extension is provided, the extension will be inferred from the file data, which may cause a different extension to be used in the output. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_scan_for_nsfw**
> NsfwResult video_scan_for_nsfw(input_file=input_file, file_url=file_url, frames_per_second=frames_per_second)

Scan a Video for NSFW content.

Automatically detect video file format and scan it for Not Safe For Work (NSFW)/Porn/Racy content. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per frame scanned.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being scanned. Use this option for files larger than 2GB. (optional)
frames_per_second = NULL # object | Optional; How many video frames per second to be scanned. Minimum value is 0.05 (1 frame per 20 seconds), maximum is 1. Default is 0.33 frame per second (1 frame scanned every 3 seconds). Maximum of 1000 total frames can be scanned, potentially adjusting the framerate for longer videos. (optional)

try:
    # Scan a Video for NSFW content.
    api_response = api_instance.video_scan_for_nsfw(input_file=input_file, file_url=file_url, frames_per_second=frames_per_second)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_scan_for_nsfw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being scanned. Use this option for files larger than 2GB. | [optional] 
 **frames_per_second** | [**object**](.md)| Optional; How many video frames per second to be scanned. Minimum value is 0.05 (1 frame per 20 seconds), maximum is 1. Default is 0.33 frame per second (1 frame scanned every 3 seconds). Maximum of 1000 total frames can be scanned, potentially adjusting the framerate for longer videos. | [optional] 

### Return type

[**NsfwResult**](NsfwResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_split_video**
> SplitVideoResult video_split_video(split_time, input_file=input_file, file_url=file_url, time_span=time_span)

Split a Video into Two Shorter Videos

Cuts a video into two videos based on the specified start time. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Also uses 1 API call per additional minute of processing time over 5 minutes, up to a maximum of 25 minutes total processing time. Maximum output file size is 50GB.

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
api_instance = cloudmersive_dataintegration_api_client.VideoApi(cloudmersive_dataintegration_api_client.ApiClient(configuration))
split_time = '2013-10-20T19:20:30+01:00' # datetime | Specify the desired time at which to split the video in TimeSpan format.
input_file = '/path/to/file.txt' # file | Input file to perform the operation on. (optional)
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
time_span = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired length of the second video in TimeSpan format. Leave blank to include the rest of the video. Maximum time is 4 hours. (optional)

try:
    # Split a Video into Two Shorter Videos
    api_response = api_instance.video_split_video(split_time, input_file=input_file, file_url=file_url, time_span=time_span)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_split_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **split_time** | **datetime**| Specify the desired time at which to split the video in TimeSpan format. | 
 **input_file** | **file**| Input file to perform the operation on. | [optional] 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **time_span** | **datetime**| Optional; Specify the desired length of the second video in TimeSpan format. Leave blank to include the rest of the video. Maximum time is 4 hours. | [optional] 

### Return type

[**SplitVideoResult**](SplitVideoResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

