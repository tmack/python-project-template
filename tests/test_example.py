import unittest
from tests.test_helper import setup_test_local_settings
from main import test_settings_exists


class TestExample(unittest.TestCase):

    def setUp(self):
        setup_test_local_settings()

    def test_that_test_settings_exist(self):
        # setup
        should_test_settings_exist = True

        # exercise
        test_settings_exist = test_settings_exists()

        # validate
        self.assertEqual(should_test_settings_exist, test_settings_exist)
