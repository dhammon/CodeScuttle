
import unittest
import sys
from io import StringIO
from contextlib import redirect_stdout
sys.path.insert(0, '')
from src.triage import Triage
from data.test_config import Config
import data.response_false as ResponseFalse
import data.response_true as ResponseTrue
import data.responses_included as ResponsesIncluded
import data.responses_excluded as ResponsesExcluded


class TestTriage(unittest.TestCase):

    def setUp(self):
        config = Config()
        self.io = StringIO()
        self.test_obj = Triage(config)
    

    def tearDown(self):
        self.io.close()
    

    def test_triage_excluded(self):
        items = ResponsesExcluded.responses
        filtered_items = self.test_obj.triage(items)
        self.assertIn('"total_count":1', filtered_items[0])    
    

    def test_triage_included(self):
        items = ResponsesIncluded.responses
        filtered_items = self.test_obj.triage(items)
        self.assertIn('"total_count":2', filtered_items[0])
    

    def test_loop_response_true1(self):
        response = ResponseTrue.response
        exclude = self.test_obj.loop_response(response)
        self.assertTrue(exclude)


    def test_loop_response_false1(self):
        response = ResponseFalse.response
        exclude = self.test_obj.loop_response(response)
        self.assertFalse(exclude)


    def test_loop_response_false2(self):
        item = {}
        exclude = self.test_obj.loop_response(item)
        self.assertFalse(exclude)



if __name__ == "__main__":
    unittest.main()