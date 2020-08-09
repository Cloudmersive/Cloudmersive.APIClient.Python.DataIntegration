# cloudmersive_video_api_client
The video APIs help you convert, encode, and transcode videos.

This Python package provides a native API client for [Cloudmersive Video and Media Services](https://cloudmersive.com/video-and-media-services-api)

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
import cloudmersive_video_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_video_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudmersive_video_api_client
from cloudmersive_video_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_video_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_video_api_client.AudioApi(cloudmersive_video_api_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AudioApi* | [**audio_convert_to_aac**](docs/AudioApi.md#audio_convert_to_aac) | **POST** /audio/convert/to/aac | Convert Audio File to AAC format.
*AudioApi* | [**audio_convert_to_m4a**](docs/AudioApi.md#audio_convert_to_m4a) | **POST** /audio/convert/to/m4a | Convert Audio File to M4A format.
*AudioApi* | [**audio_convert_to_mp3**](docs/AudioApi.md#audio_convert_to_mp3) | **POST** /audio/convert/to/mp3 | Convert Audio File to MP3 format.
*AudioApi* | [**audio_convert_to_wav**](docs/AudioApi.md#audio_convert_to_wav) | **POST** /audio/convert/to/wav | Convert Audio File to WAV format.
*VideoApi* | [**video_convert_to_gif**](docs/VideoApi.md#video_convert_to_gif) | **POST** /video/convert/to/gif | Convert Video to Animated GIF format.
*VideoApi* | [**video_convert_to_mov**](docs/VideoApi.md#video_convert_to_mov) | **POST** /video/convert/to/mov | Convert Video to MOV format.
*VideoApi* | [**video_convert_to_mp4**](docs/VideoApi.md#video_convert_to_mp4) | **POST** /video/convert/to/mp4 | Convert Video to MP4 format.
*VideoApi* | [**video_convert_to_still_frames**](docs/VideoApi.md#video_convert_to_still_frames) | **POST** /video/convert/to/still-frames | Convert Video to PNG Still Frames.
*VideoApi* | [**video_convert_to_webm**](docs/VideoApi.md#video_convert_to_webm) | **POST** /video/convert/to/webm | Convert Video to WEBM format.
*VideoApi* | [**video_cut_video**](docs/VideoApi.md#video_cut_video) | **POST** /video/cut | Cut a Video to a Shorter Length
*VideoApi* | [**video_get_info**](docs/VideoApi.md#video_get_info) | **POST** /video/convert/get-info | Get detailed information about a video or audio file
*VideoApi* | [**video_resize_video**](docs/VideoApi.md#video_resize_video) | **POST** /video/resize/preserveAspectRatio | Resizes a Video Preserving the Original Aspect Ratio.
*VideoApi* | [**video_resize_video_simple**](docs/VideoApi.md#video_resize_video_simple) | **POST** /video/resize/target | Resizes a Video without Preserving Aspect Ratio.
*VideoApi* | [**video_scan_for_nsfw**](docs/VideoApi.md#video_scan_for_nsfw) | **POST** /video/scan/nsfw | Scan a Video for NSFW content.
*VideoApi* | [**video_split_video**](docs/VideoApi.md#video_split_video) | **POST** /video/split | Split a Video into Two Shorter Videos


## Documentation For Models

 - [MediaInformation](docs/MediaInformation.md)
 - [NsfwResult](docs/NsfwResult.md)
 - [NsfwScannedFrame](docs/NsfwScannedFrame.md)
 - [SplitVideoResult](docs/SplitVideoResult.md)
 - [StillFrame](docs/StillFrame.md)
 - [StillFramesResult](docs/StillFramesResult.md)
 - [VideoFile](docs/VideoFile.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



