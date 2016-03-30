# Django boilerplate

This projects contains a Django boilerplate to easy create a multi app Django projecto with easy CI and CD using Bamboo.


## How to use

Simply copy/paste this code in your root repo and change `my_project` and `my_app` to your own names.

**NOTE:** `my_app` is just an example app, you can remove it at create your own if you want instead of rename it.

### Requirements

To install dependencies run:

```
$ pip install -r requirements.txt
```

You can add your own extra dependencies in `requirements/common.txt` or `requirements/tests.txt` files.

### Settings

Settings are readed from a `.json` file in some place on your OS filesystem. By default is set it to `/etc/my_project/settings.json`, you can just replace this route in `settings.config` file to your own path.

An example config file:
```
{
    "SECRET_KEY": "MY_SECRET_KEY",
    "DB_NAME": "my_app",
    "DB_USER": "user",
    "DB_PASSWORD": "password",
    "STATIC_ROOT": "STATIC_ROOT",
    "ENVIRONMENT": "development"
}
```

When you deploy your app remenber to set the right permissions to this file and set `ENVIRONMENT` settings to `"procution"` value.

Database is set it as a mysql database as default but you can easely extend it or change it modifying  `settings.config` file and addint new fields to your settings file.

## Path structure

This boilerplate is to create apps which could contains several apps inside.
The folders inside are:

- `apps/`: Contains all Django apps in our project.
    - `my_app/`
        - `tests/`: Containing all tests in our app.
            - `test_filename_to_test.py`
            - ...
- `settings/`: Contains Django project settings.
    - `common.py`: This file contain common settings for any app and any environment.
    - `config.py`: Read dev and production settings from a file.
    - `testing_ci.py`: Set static values to easy use on CI.
- `requirements/`: Contains `pip` requirements files.
    - `common.txt`: dev/production/CI common requirements.
    - `tests.txt`: dev/CI requirements.
- `scripts/`: Bash script utils to seasy run tests.
    - `init.sh`: Set initial vars to run any script.
    - `pylint.sh`: Run python lint.
    - `run_all_tests.sh`: Run all tests (lint and Django tests) on a dev environment.
    - `run_tests_on_ci.sh`: Run all tests using `testing_ci.py` file config and xml reporter middleware to get parseable results for Bamboo.


**NOTE:** If your project is too big, take a look on Microservices (or any SOA) architectures, it is not recomended to create very big monolithics apps, they are not scalable and hard to mantain.
