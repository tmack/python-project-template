# Python Project Template 
A template for starting a new project in python. This project contains basic infrastructure for testing and CI/CD with github actions.

## Installing Requirements
```bash
$ pip install -r requirements.txt
```

## Setting up configs
Create the json file 'test-local.settings.json', this is a place to put project settings you'd like to use. Each key/value pair is set as environmental variable during run time.
```json
{
"env_variable_name" : "env_variable_value"
}
```

## Running Tests
To run tests use the following command. 
```bash
 python -m unittest discover -s tests -p 'test_*.py'
```
Tests can also be configured to run from an IDE. See tests/example_of_pycharm_test_configurations.png for an example from pycharm

### Example Testing Output
Here's what testing should look like when its up and running

 ```bash
$ python -m unittest discover -s tests -p 'test_*.py'
............
----------------------------------------------------------------------
Ran 1 tests in 0.001s

OK
```

