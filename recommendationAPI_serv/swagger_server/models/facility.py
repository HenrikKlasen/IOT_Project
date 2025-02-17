# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Facility(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, qunatity: float=None):  # noqa: E501
        """Facility - a model defined in Swagger

        :param name: The name of this Facility.  # noqa: E501
        :type name: str
        :param qunatity: The qunatity of this Facility.  # noqa: E501
        :type qunatity: float
        """
        self.swagger_types = {
            'name': str,
            'qunatity': float
        }

        self.attribute_map = {
            'name': 'name',
            'qunatity': 'qunatity'
        }
        self._name = name
        self._qunatity = qunatity

    @classmethod
    def from_dict(cls, dikt) -> 'Facility':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Facility of this Facility.  # noqa: E501
        :rtype: Facility
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Facility.

        Name of the facility.  # noqa: E501

        :return: The name of this Facility.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Facility.

        Name of the facility.  # noqa: E501

        :param name: The name of this Facility.
        :type name: str
        """

        self._name = name

    @property
    def qunatity(self) -> float:
        """Gets the qunatity of this Facility.

        Required quantity of facility  # noqa: E501

        :return: The qunatity of this Facility.
        :rtype: float
        """
        return self._qunatity

    @qunatity.setter
    def qunatity(self, qunatity: float):
        """Sets the qunatity of this Facility.

        Required quantity of facility  # noqa: E501

        :param qunatity: The qunatity of this Facility.
        :type qunatity: float
        """

        self._qunatity = qunatity
