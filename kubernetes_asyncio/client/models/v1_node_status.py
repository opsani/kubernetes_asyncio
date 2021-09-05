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


class V1NodeStatus(object):
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
        'addresses': 'list[V1NodeAddress]',
        'allocatable': 'dict(str, str)',
        'capacity': 'dict(str, str)',
        'conditions': 'list[V1NodeCondition]',
        'config': 'V1NodeConfigStatus',
        'daemon_endpoints': 'V1NodeDaemonEndpoints',
        'images': 'list[V1ContainerImage]',
        'node_info': 'V1NodeSystemInfo',
        'phase': 'str',
        'volumes_attached': 'list[V1AttachedVolume]',
        'volumes_in_use': 'list[str]'
    }

    attribute_map = {
        'addresses': 'addresses',
        'allocatable': 'allocatable',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'config': 'config',
        'daemon_endpoints': 'daemonEndpoints',
        'images': 'images',
        'node_info': 'nodeInfo',
        'phase': 'phase',
        'volumes_attached': 'volumesAttached',
        'volumes_in_use': 'volumesInUse'
    }

    def __init__(self, addresses=None, allocatable=None, capacity=None, conditions=None, config=None, daemon_endpoints=None, images=None, node_info=None, phase=None, volumes_attached=None, volumes_in_use=None, local_vars_configuration=None):  # noqa: E501
        """V1NodeStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._allocatable = None
        self._capacity = None
        self._conditions = None
        self._config = None
        self._daemon_endpoints = None
        self._images = None
        self._node_info = None
        self._phase = None
        self._volumes_attached = None
        self._volumes_in_use = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if allocatable is not None:
            self.allocatable = allocatable
        if capacity is not None:
            self.capacity = capacity
        if conditions is not None:
            self.conditions = conditions
        if config is not None:
            self.config = config
        if daemon_endpoints is not None:
            self.daemon_endpoints = daemon_endpoints
        if images is not None:
            self.images = images
        if node_info is not None:
            self.node_info = node_info
        if phase is not None:
            self.phase = phase
        if volumes_attached is not None:
            self.volumes_attached = volumes_attached
        if volumes_in_use is not None:
            self.volumes_in_use = volumes_in_use

    @property
    def addresses(self):
        """Gets the addresses of this V1NodeStatus.  # noqa: E501

        List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See http://pr.k8s.io/79391 for an example.  # noqa: E501

        :return: The addresses of this V1NodeStatus.  # noqa: E501
        :rtype: list[V1NodeAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V1NodeStatus.

        List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See http://pr.k8s.io/79391 for an example.  # noqa: E501

        :param addresses: The addresses of this V1NodeStatus.  # noqa: E501
        :type: list[V1NodeAddress]
        """

        self._addresses = addresses

    @property
    def allocatable(self):
        """Gets the allocatable of this V1NodeStatus.  # noqa: E501

        Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.  # noqa: E501

        :return: The allocatable of this V1NodeStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._allocatable

    @allocatable.setter
    def allocatable(self, allocatable):
        """Sets the allocatable of this V1NodeStatus.

        Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.  # noqa: E501

        :param allocatable: The allocatable of this V1NodeStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._allocatable = allocatable

    @property
    def capacity(self):
        """Gets the capacity of this V1NodeStatus.  # noqa: E501

        Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity  # noqa: E501

        :return: The capacity of this V1NodeStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1NodeStatus.

        Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity  # noqa: E501

        :param capacity: The capacity of this V1NodeStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._capacity = capacity

    @property
    def conditions(self):
        """Gets the conditions of this V1NodeStatus.  # noqa: E501

        Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition  # noqa: E501

        :return: The conditions of this V1NodeStatus.  # noqa: E501
        :rtype: list[V1NodeCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1NodeStatus.

        Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition  # noqa: E501

        :param conditions: The conditions of this V1NodeStatus.  # noqa: E501
        :type: list[V1NodeCondition]
        """

        self._conditions = conditions

    @property
    def config(self):
        """Gets the config of this V1NodeStatus.  # noqa: E501


        :return: The config of this V1NodeStatus.  # noqa: E501
        :rtype: V1NodeConfigStatus
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this V1NodeStatus.


        :param config: The config of this V1NodeStatus.  # noqa: E501
        :type: V1NodeConfigStatus
        """

        self._config = config

    @property
    def daemon_endpoints(self):
        """Gets the daemon_endpoints of this V1NodeStatus.  # noqa: E501


        :return: The daemon_endpoints of this V1NodeStatus.  # noqa: E501
        :rtype: V1NodeDaemonEndpoints
        """
        return self._daemon_endpoints

    @daemon_endpoints.setter
    def daemon_endpoints(self, daemon_endpoints):
        """Sets the daemon_endpoints of this V1NodeStatus.


        :param daemon_endpoints: The daemon_endpoints of this V1NodeStatus.  # noqa: E501
        :type: V1NodeDaemonEndpoints
        """

        self._daemon_endpoints = daemon_endpoints

    @property
    def images(self):
        """Gets the images of this V1NodeStatus.  # noqa: E501

        List of container images on this node  # noqa: E501

        :return: The images of this V1NodeStatus.  # noqa: E501
        :rtype: list[V1ContainerImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this V1NodeStatus.

        List of container images on this node  # noqa: E501

        :param images: The images of this V1NodeStatus.  # noqa: E501
        :type: list[V1ContainerImage]
        """

        self._images = images

    @property
    def node_info(self):
        """Gets the node_info of this V1NodeStatus.  # noqa: E501


        :return: The node_info of this V1NodeStatus.  # noqa: E501
        :rtype: V1NodeSystemInfo
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this V1NodeStatus.


        :param node_info: The node_info of this V1NodeStatus.  # noqa: E501
        :type: V1NodeSystemInfo
        """

        self._node_info = node_info

    @property
    def phase(self):
        """Gets the phase of this V1NodeStatus.  # noqa: E501

        NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.  # noqa: E501

        :return: The phase of this V1NodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1NodeStatus.

        NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.  # noqa: E501

        :param phase: The phase of this V1NodeStatus.  # noqa: E501
        :type: str
        """

        self._phase = phase

    @property
    def volumes_attached(self):
        """Gets the volumes_attached of this V1NodeStatus.  # noqa: E501

        List of volumes that are attached to the node.  # noqa: E501

        :return: The volumes_attached of this V1NodeStatus.  # noqa: E501
        :rtype: list[V1AttachedVolume]
        """
        return self._volumes_attached

    @volumes_attached.setter
    def volumes_attached(self, volumes_attached):
        """Sets the volumes_attached of this V1NodeStatus.

        List of volumes that are attached to the node.  # noqa: E501

        :param volumes_attached: The volumes_attached of this V1NodeStatus.  # noqa: E501
        :type: list[V1AttachedVolume]
        """

        self._volumes_attached = volumes_attached

    @property
    def volumes_in_use(self):
        """Gets the volumes_in_use of this V1NodeStatus.  # noqa: E501

        List of attachable volumes in use (mounted) by the node.  # noqa: E501

        :return: The volumes_in_use of this V1NodeStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._volumes_in_use

    @volumes_in_use.setter
    def volumes_in_use(self, volumes_in_use):
        """Sets the volumes_in_use of this V1NodeStatus.

        List of attachable volumes in use (mounted) by the node.  # noqa: E501

        :param volumes_in_use: The volumes_in_use of this V1NodeStatus.  # noqa: E501
        :type: list[str]
        """

        self._volumes_in_use = volumes_in_use

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
        if not isinstance(other, V1NodeStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1NodeStatus):
            return True

        return self.to_dict() != other.to_dict()
