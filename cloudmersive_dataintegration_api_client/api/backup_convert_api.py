# coding: utf-8

"""
    dataintegrationapi

    Easily and directly query database backup files, convert into other file formats.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_dataintegration_api_client.api_client import ApiClient


class BackupConvertApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dataintegration_backup_convert_mssql_bak_get_tables_post(self, **kwargs):  # noqa: E501
        """Lists all tables stored in a SQL Server Backup (.BAK) file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dataintegration_backup_convert_mssql_bak_get_tables_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on
        :return: MssqlBakEnumerateTablesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dataintegration_backup_convert_mssql_bak_get_tables_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dataintegration_backup_convert_mssql_bak_get_tables_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def dataintegration_backup_convert_mssql_bak_get_tables_post_with_http_info(self, **kwargs):  # noqa: E501
        """Lists all tables stored in a SQL Server Backup (.BAK) file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dataintegration_backup_convert_mssql_bak_get_tables_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file input_file: Input file to perform the operation on
        :return: MssqlBakEnumerateTablesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dataintegration_backup_convert_mssql_bak_get_tables_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/dataintegration/backup/convert/mssql/bak/get/tables', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MssqlBakEnumerateTablesResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dataintegration_backup_convert_mssql_bak_to_csv_post(self, **kwargs):  # noqa: E501
        """Converts a SQL Server Backup (.BAK) file into CSV for a specified table  # noqa: E501

        Input the target table to extract the data as a CSV format file.  Supports a wide array of SQL Server .BAK files and SQL Server backup file versions.  Consumes 1 API call per MB of input data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dataintegration_backup_convert_mssql_bak_to_csv_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str table_name: Name of the table to return
        :param file input_file: Input file to perform the operation on
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dataintegration_backup_convert_mssql_bak_to_csv_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dataintegration_backup_convert_mssql_bak_to_csv_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def dataintegration_backup_convert_mssql_bak_to_csv_post_with_http_info(self, **kwargs):  # noqa: E501
        """Converts a SQL Server Backup (.BAK) file into CSV for a specified table  # noqa: E501

        Input the target table to extract the data as a CSV format file.  Supports a wide array of SQL Server .BAK files and SQL Server backup file versions.  Consumes 1 API call per MB of input data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dataintegration_backup_convert_mssql_bak_to_csv_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str table_name: Name of the table to return
        :param file input_file: Input file to perform the operation on
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_name', 'input_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dataintegration_backup_convert_mssql_bak_to_csv_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'table_name' in params:
            header_params['tableName'] = params['table_name']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'input_file' in params:
            local_var_files['inputFile'] = params['input_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/dataintegration/backup/convert/mssql/bak/to/csv', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
