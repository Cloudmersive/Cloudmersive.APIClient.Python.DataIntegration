# coding: utf-8

"""
    Data Integration API

    Easily and directly query database backup files, convert into other file formats.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MssqlTable(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'schema_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'schema_name': 'schemaName',
        'table_name': 'tableName'
    }

    def __init__(self, schema_name=None, table_name=None):  # noqa: E501
        """MssqlTable - a model defined in Swagger"""  # noqa: E501

        self._schema_name = None
        self._table_name = None
        self.discriminator = None

        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name

    @property
    def schema_name(self):
        """Gets the schema_name of this MssqlTable.  # noqa: E501

        Name of the schema containing the table  # noqa: E501

        :return: The schema_name of this MssqlTable.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this MssqlTable.

        Name of the schema containing the table  # noqa: E501

        :param schema_name: The schema_name of this MssqlTable.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this MssqlTable.  # noqa: E501

        Name of the table  # noqa: E501

        :return: The table_name of this MssqlTable.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this MssqlTable.

        Name of the table  # noqa: E501

        :param table_name: The table_name of this MssqlTable.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MssqlTable, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MssqlTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
