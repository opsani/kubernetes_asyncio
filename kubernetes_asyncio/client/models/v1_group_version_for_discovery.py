# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.18.20
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1GroupVersionForDiscovery(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'group_version': 'str',
        'version': 'str'
    }

    attribute_map = {
        'group_version': 'groupVersion',
        'version': 'version'
    }

    def __init__(self, group_version=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1GroupVersionForDiscovery - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_version = None
        self._version = None
        self.discriminator = None

        self.group_version = group_version
        self.version = version

    @property
    def group_version(self):
        """Gets the group_version of this V1GroupVersionForDiscovery.  # noqa: E501

        groupVersion specifies the API group and version in the form \"group/version\"  # noqa: E501

        :return: The group_version of this V1GroupVersionForDiscovery.  # noqa: E501
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """Sets the group_version of this V1GroupVersionForDiscovery.

        groupVersion specifies the API group and version in the form \"group/version\"  # noqa: E501

        :param group_version: The group_version of this V1GroupVersionForDiscovery.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_version is None:  # noqa: E501
            raise ValueError("Invalid value for `group_version`, must not be `None`")  # noqa: E501

        self._group_version = group_version

    @property
    def version(self):
        """Gets the version of this V1GroupVersionForDiscovery.  # noqa: E501

        version specifies the version in the form of \"version\". This is to save the clients the trouble of splitting the GroupVersion.  # noqa: E501

        :return: The version of this V1GroupVersionForDiscovery.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1GroupVersionForDiscovery.

        version specifies the version in the form of \"version\". This is to save the clients the trouble of splitting the GroupVersion.  # noqa: E501

        :param version: The version of this V1GroupVersionForDiscovery.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1GroupVersionForDiscovery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1GroupVersionForDiscovery):
            return True

        return self.to_dict() != other.to_dict()
