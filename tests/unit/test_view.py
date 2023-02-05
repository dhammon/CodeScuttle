
import unittest
import sys
import json as Json
sys.path.insert(0, '')
from src.view import View
import data.filtered_result as data
from io import StringIO
from contextlib import redirect_stdout


class TestView(unittest.TestCase):

    def setUp(self):
        self.io = StringIO()
        self.test_obj = View(Json)
    

    def tearDown(self):
        self.io.close()


    def test_view_happy(self):
        filtered_result = data.filtered_result
        with redirect_stdout(self.io):
            self.test_obj.view(filtered_result)
        self.assertIn("[-]", self.io.getvalue())


    def test_view_empty(self):
        filtered_result = {}
        with redirect_stdout(self.io):
            self.test_obj.view(filtered_result)
        self.assertIn("[+] No code leaks found", self.io.getvalue())


if __name__ == "__main__":
    unittest.main()