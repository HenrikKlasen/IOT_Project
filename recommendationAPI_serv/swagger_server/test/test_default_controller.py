# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.room import Room  # noqa: E501
from swagger_server.models.room_request import RoomRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_recommend_rooms_post(self):
        """Test case for recommend_rooms_post

        Recommend rooms based on user-provided weights.
        """
        body = RoomRequest()
        response = self.client.open(
            '/recommend-rooms',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
