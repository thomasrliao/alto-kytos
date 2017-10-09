# coding: utf-8

from __future__ import absolute_import
from napps.snlab.unicorn_resource_discovery.models.ane import ANE
from napps.snlab.unicorn_resource_discovery.models.ane_flow_vector import ANEFlowVector
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ResourceQueryResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ane_matrix: List[ANEFlowVector]=None, anes: List[ANE]=None):
        """
        ResourceQueryResponse - a model defined in Swagger

        :param ane_matrix: The ane_matrix of this ResourceQueryResponse.
        :type ane_matrix: List[ANEFlowVector]
        :param anes: The anes of this ResourceQueryResponse.
        :type anes: List[ANE]
        """
        self.swagger_types = {
            'ane_matrix': List[ANEFlowVector],
            'anes': List[ANE]
        }

        self.attribute_map = {
            'ane_matrix': 'ane-matrix',
            'anes': 'anes'
        }

        self._ane_matrix = ane_matrix
        self._anes = anes

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceQueryResponse':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceQueryResponse of this ResourceQueryResponse.
        :rtype: ResourceQueryResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def ane_matrix(self) -> List[ANEFlowVector]:
        """
        Gets the ane_matrix of this ResourceQueryResponse.

        :return: The ane_matrix of this ResourceQueryResponse.
        :rtype: List[ANEFlowVector]
        """
        return self._ane_matrix

    @ane_matrix.setter
    def ane_matrix(self, ane_matrix: List[ANEFlowVector]):
        """
        Sets the ane_matrix of this ResourceQueryResponse.

        :param ane_matrix: The ane_matrix of this ResourceQueryResponse.
        :type ane_matrix: List[ANEFlowVector]
        """
        if ane_matrix is None:
            raise ValueError("Invalid value for `ane_matrix`, must not be `None`")

        self._ane_matrix = ane_matrix

    @property
    def anes(self) -> List[ANE]:
        """
        Gets the anes of this ResourceQueryResponse.

        :return: The anes of this ResourceQueryResponse.
        :rtype: List[ANE]
        """
        return self._anes

    @anes.setter
    def anes(self, anes: List[ANE]):
        """
        Sets the anes of this ResourceQueryResponse.

        :param anes: The anes of this ResourceQueryResponse.
        :type anes: List[ANE]
        """
        if anes is None:
            raise ValueError("Invalid value for `anes`, must not be `None`")

        self._anes = anes

