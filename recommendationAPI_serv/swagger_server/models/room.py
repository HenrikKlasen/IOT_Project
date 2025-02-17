# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.facility import Facility  # noqa: F401,E501
from swagger_server.models.room_metrics import RoomMetrics  # noqa: F401,E501
from swagger_server import util


class Room(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, room_id: str=None, date_time_slot_start: datetime=None, date_time_slot_end: datetime=None, room_metrics: RoomMetrics=None, facilities: List[Facility]=None, rank: float=None):  # noqa: E501
        """Room - a model defined in Swagger

        :param room_id: The room_id of this Room.  # noqa: E501
        :type room_id: str
        :param date_time_slot_start: The date_time_slot_start of this Room.  # noqa: E501
        :type date_time_slot_start: datetime
        :param date_time_slot_end: The date_time_slot_end of this Room.  # noqa: E501
        :type date_time_slot_end: datetime
        :param room_metrics: The room_metrics of this Room.  # noqa: E501
        :type room_metrics: RoomMetrics
        :param facilities: The facilities of this Room.  # noqa: E501
        :type facilities: List[Facility]
        :param rank: The rank of this Room.  # noqa: E501
        :type rank: float
        """
        self.swagger_types = {
            'room_id': str,
            'date_time_slot_start': datetime,
            'date_time_slot_end': datetime,
            'room_metrics': RoomMetrics,
            'facilities': List[Facility],
            'rank': float
        }

        self.attribute_map = {
            'room_id': 'roomID',
            'date_time_slot_start': 'dateTimeSlotStart',
            'date_time_slot_end': 'dateTimeSlotEnd',
            'room_metrics': 'roomMetrics',
            'facilities': 'facilities',
            'rank': 'rank'
        }
        self._room_id = room_id
        self._date_time_slot_start = date_time_slot_start
        self._date_time_slot_end = date_time_slot_end
        self._room_metrics = room_metrics
        self._facilities = facilities
        self._rank = rank

    @classmethod
    def from_dict(cls, dikt) -> 'Room':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Room of this Room.  # noqa: E501
        :rtype: Room
        """
        return util.deserialize_model(dikt, cls)

    @property
    def room_id(self) -> str:
        """Gets the room_id of this Room.

        Unique room identification string.  # noqa: E501

        :return: The room_id of this Room.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id: str):
        """Sets the room_id of this Room.

        Unique room identification string.  # noqa: E501

        :param room_id: The room_id of this Room.
        :type room_id: str
        """

        self._room_id = room_id

    @property
    def date_time_slot_start(self) -> datetime:
        """Gets the date_time_slot_start of this Room.

        The desired date and time slot for room availability start.  # noqa: E501

        :return: The date_time_slot_start of this Room.
        :rtype: datetime
        """
        return self._date_time_slot_start

    @date_time_slot_start.setter
    def date_time_slot_start(self, date_time_slot_start: datetime):
        """Sets the date_time_slot_start of this Room.

        The desired date and time slot for room availability start.  # noqa: E501

        :param date_time_slot_start: The date_time_slot_start of this Room.
        :type date_time_slot_start: datetime
        """

        self._date_time_slot_start = date_time_slot_start

    @property
    def date_time_slot_end(self) -> datetime:
        """Gets the date_time_slot_end of this Room.

        The desired date and time slot for room availability dateTimeSlotEnd.  # noqa: E501

        :return: The date_time_slot_end of this Room.
        :rtype: datetime
        """
        return self._date_time_slot_end

    @date_time_slot_end.setter
    def date_time_slot_end(self, date_time_slot_end: datetime):
        """Sets the date_time_slot_end of this Room.

        The desired date and time slot for room availability dateTimeSlotEnd.  # noqa: E501

        :param date_time_slot_end: The date_time_slot_end of this Room.
        :type date_time_slot_end: datetime
        """

        self._date_time_slot_end = date_time_slot_end

    @property
    def room_metrics(self) -> RoomMetrics:
        """Gets the room_metrics of this Room.


        :return: The room_metrics of this Room.
        :rtype: RoomMetrics
        """
        return self._room_metrics

    @room_metrics.setter
    def room_metrics(self, room_metrics: RoomMetrics):
        """Sets the room_metrics of this Room.


        :param room_metrics: The room_metrics of this Room.
        :type room_metrics: RoomMetrics
        """

        self._room_metrics = room_metrics

    @property
    def facilities(self) -> List[Facility]:
        """Gets the facilities of this Room.

        List of facilities in the room.  # noqa: E501

        :return: The facilities of this Room.
        :rtype: List[Facility]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities: List[Facility]):
        """Sets the facilities of this Room.

        List of facilities in the room.  # noqa: E501

        :param facilities: The facilities of this Room.
        :type facilities: List[Facility]
        """

        self._facilities = facilities

    @property
    def rank(self) -> float:
        """Gets the rank of this Room.

        the rank of the room representing how well it satisfies the request compared to the other available rooms.  # noqa: E501

        :return: The rank of this Room.
        :rtype: float
        """
        return self._rank

    @rank.setter
    def rank(self, rank: float):
        """Sets the rank of this Room.

        the rank of the room representing how well it satisfies the request compared to the other available rooms.  # noqa: E501

        :param rank: The rank of this Room.
        :type rank: float
        """

        self._rank = rank
