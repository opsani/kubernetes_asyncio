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


class V1CustomResourceDefinitionSpec(object):
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
        'conversion': 'V1CustomResourceConversion',
        'group': 'str',
        'names': 'V1CustomResourceDefinitionNames',
        'preserve_unknown_fields': 'bool',
        'scope': 'str',
        'versions': 'list[V1CustomResourceDefinitionVersion]'
    }

    attribute_map = {
        'conversion': 'conversion',
        'group': 'group',
        'names': 'names',
        'preserve_unknown_fields': 'preserveUnknownFields',
        'scope': 'scope',
        'versions': 'versions'
    }

    def __init__(self, conversion=None, group=None, names=None, preserve_unknown_fields=None, scope=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """V1CustomResourceDefinitionSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversion = None
        self._group = None
        self._names = None
        self._preserve_unknown_fields = None
        self._scope = None
        self._versions = None
        self.discriminator = None

        if conversion is not None:
            self.conversion = conversion
        self.group = group
        self.names = names
        if preserve_unknown_fields is not None:
            self.preserve_unknown_fields = preserve_unknown_fields
        self.scope = scope
        self.versions = versions

    @property
    def conversion(self):
        """Gets the conversion of this V1CustomResourceDefinitionSpec.  # noqa: E501


        :return: The conversion of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :rtype: V1CustomResourceConversion
        """
        return self._conversion

    @conversion.setter
    def conversion(self, conversion):
        """Sets the conversion of this V1CustomResourceDefinitionSpec.


        :param conversion: The conversion of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :type: V1CustomResourceConversion
        """

        self._conversion = conversion

    @property
    def group(self):
        """Gets the group of this V1CustomResourceDefinitionSpec.  # noqa: E501

        group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`).  # noqa: E501

        :return: The group of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1CustomResourceDefinitionSpec.

        group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`).  # noqa: E501

        :param group: The group of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def names(self):
        """Gets the names of this V1CustomResourceDefinitionSpec.  # noqa: E501


        :return: The names of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :rtype: V1CustomResourceDefinitionNames
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this V1CustomResourceDefinitionSpec.


        :param names: The names of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :type: V1CustomResourceDefinitionNames
        """
        if self.local_vars_configuration.client_side_validation and names is None:  # noqa: E501
            raise ValueError("Invalid value for `names`, must not be `None`")  # noqa: E501

        self._names = names

    @property
    def preserve_unknown_fields(self):
        """Gets the preserve_unknown_fields of this V1CustomResourceDefinitionSpec.  # noqa: E501

        preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#pruning-versus-preserving-unknown-fields for details.  # noqa: E501

        :return: The preserve_unknown_fields of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_unknown_fields

    @preserve_unknown_fields.setter
    def preserve_unknown_fields(self, preserve_unknown_fields):
        """Sets the preserve_unknown_fields of this V1CustomResourceDefinitionSpec.

        preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#pruning-versus-preserving-unknown-fields for details.  # noqa: E501

        :param preserve_unknown_fields: The preserve_unknown_fields of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :type: bool
        """

        self._preserve_unknown_fields = preserve_unknown_fields

    @property
    def scope(self):
        """Gets the scope of this V1CustomResourceDefinitionSpec.  # noqa: E501

        scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`.  # noqa: E501

        :return: The scope of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this V1CustomResourceDefinitionSpec.

        scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`.  # noqa: E501

        :param scope: The scope of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def versions(self):
        """Gets the versions of this V1CustomResourceDefinitionSpec.  # noqa: E501

        versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.  # noqa: E501

        :return: The versions of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :rtype: list[V1CustomResourceDefinitionVersion]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this V1CustomResourceDefinitionSpec.

        versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.  # noqa: E501

        :param versions: The versions of this V1CustomResourceDefinitionSpec.  # noqa: E501
        :type: list[V1CustomResourceDefinitionVersion]
        """
        if self.local_vars_configuration.client_side_validation and versions is None:  # noqa: E501
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501

        self._versions = versions

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
        if not isinstance(other, V1CustomResourceDefinitionSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CustomResourceDefinitionSpec):
            return True

        return self.to_dict() != other.to_dict()
