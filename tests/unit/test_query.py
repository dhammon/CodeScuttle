
import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
import sys
from io import StringIO
from contextlib import redirect_stdout
import requests as Requests
import time as Time
import json as Json
sys.path.insert(0, '')
from src.query import Query
from data.test_config import Config
import data.response_obj_limit_secondary as ResponseLimitSecondaryClass
import data.response_obj_limit_other as ResponseLimitOtherClass
import data.response_obj_public as ResponsePublic
import data.response_obj_private as ResponsePrivate
import data.response_obj_empty as ResponseEmpty
import data.response_obj_403 as Response403


class TestQuery(unittest.TestCase):

    def setUp(self):
        requests = Requests
        requests.get = MagicMock(return_value="mockedGetReponse")
        time = Time
        time.sleep = MagicMock(return_value=10)
        json = Json
        config = Config()
        self.io = StringIO()
        self.test_obj = Query(config, requests, time, json)
    

    def tearDown(self):
        self.io.close()
    

    def test_query_403(self):
        requests = Requests
        requests.get = Mock()
        requests.get.side_effect = [
            ResponsePublic.ResponsePublic(),
            Response403.Response403(),
            ResponsePrivate.ResponsePrivate(),
            ResponseEmpty.ResponseEmpty()
        ]
        time = Time
        time.sleep = MagicMock(return_value=1)
        json = Json
        config = Config()
        test_obj = Query(config, requests, time, json)
        with redirect_stdout(self.io):
            queried_items = test_obj.query()
        self.assertIn("[!] INFO: GitHub API Secondary Rate Limit by exceeded", self.io.getvalue())
        self.assertEqual(2, len(queried_items))
        self.assertIn('"total_count":1', queried_items[0])
        self.assertIn('"total_count":2', queried_items[1])        


    def test_query_200(self):
        requests = Requests
        requests.get = Mock()
        requests.get.side_effect = [
            ResponsePublic.ResponsePublic(),
            ResponsePrivate.ResponsePrivate(),
            ResponseEmpty.ResponseEmpty()
        ]
        time = Time
        time.sleep = MagicMock(return_value=10)
        json = Json
        config = Config()
        test_obj = Query(config, requests, time, json)
        queried_items = test_obj.query()
        self.assertEqual(2, len(queried_items))
        self.assertIn('"total_count":1', queried_items[0])
        self.assertIn('"total_count":2', queried_items[1])


    def test_handle_rate_default(self):
        response = ResponseLimitOtherClass.ResponseLimit()
        url = "lol.com"
        headers = '{}'
        with redirect_stdout(self.io):
            response = self.test_obj.handle_rate_limit(response, url, headers)
        self.assertIn("mockedGetReponse", response)
        self.assertIn("[!] INFO: Limit exceeded.", self.io.getvalue())


    def test_handle_rate_limit(self):
        response = ResponseLimitSecondaryClass.ResponseLimit()
        url = "lol.com"
        headers = '{}'
        with redirect_stdout(self.io):
            response = self.test_obj.handle_rate_limit(response, url, headers)
        self.assertIn("mockedGetReponse", response)
        self.assertIn("[!] INFO: GitHub API Secondary Rate Limit by exceeded", self.io.getvalue())



if __name__ == "__main__":
    unittest.main()