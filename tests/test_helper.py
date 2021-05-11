import os
import json
import shutil
import logging


def setup_test_local_settings(testing_settings_path='test-local.settings.json'):
    if not os.path.exists(testing_settings_path):
        ask_user_to_generate_test_file(testing_settings_path)
        return None
    with open(testing_settings_path, 'r') as f:
        local_settings = json.load(f)
    for key in local_settings.keys():
        os.environ[key] = local_settings[key]


def ask_user_to_generate_test_file(testing_settings_path):
    generate_test_settings_command = '$ echo {} > ' + testing_settings_path
    logging.warning(f'The testing settings file don\'t exist at {testing_settings_path}. '
                    f'Run the following command to generate the file:\n {generate_test_settings_command}')


def lists_are_equal(list_1, list_2):
    return len(list_1) == len(list_2) and sorted(list_1) == sorted(list_2)


def remove_test_directory(directory):
    directory_starts_with_test = directory.startswith('test') \
                                 or directory.startswith('./test') \
                                 or directory.startswith('~/test')
    if not directory_starts_with_test:
        logging.error('Not deleting directory. Only deleting directories that start with "test"')
        return False
    try:
        shutil.rmtree(directory)
        return True
    except OSError as e:
        logging.info(f'Error: {e.filename} - {e.strerror}.')
