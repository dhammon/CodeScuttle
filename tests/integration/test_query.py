
import unittest
import sys
from io import StringIO
from contextlib import redirect_stdout
import requests as Requests
import time as Time
import json as Json
sys.path.insert(0, '')
from src.query import Query
from data.test_config import Config


class TestQuery(unittest.TestCase):

    def setUp(self):
        requests = Requests
        time = Time
        json = Json
        config = Config()
        self.test_obj = Query(config, requests, time, json)
        self.io = StringIO()
    

    def tearDown(self):
        self.io.close()
    
    
    def test_query(self):
        queried_items = self.test_obj.query()
        self.assertEqual(2, len(queried_items))
        self.assertIn('"total_count":1', queried_items[0])
        self.assertIn('"total_count":2', queried_items[1])  


if __name__ == "__main__":
    unittest.main()
