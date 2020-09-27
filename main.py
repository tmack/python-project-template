import json
import logging
import os


def test_settings_exists(test_config_path='./test-local.settings.json'):
    if os.path.exists(test_config_path):
        return True
    return False

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    get_hello_world()
