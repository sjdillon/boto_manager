# Boto Client Manager
[![Build Status](https://travis-ci.org/sjdillon/boto_manager.svg?branch=master)](https://travis-ci.org/sjdillon/boto_manager)

The BotoClientManager is a class that abstracts the creation of boto clients and allows "injecting" mocking into AWS calls.  Placebo requires the creation of a boto session along with the boto client.  BotoClientManager allows both recording and playback of mock data.

* `boto_manager.py` -- creates and manages boto sessions and clients, allows mocking playback and recording
* `lambda_function.py` -- a sample lambda function that uses an AWS resource
* `tests\test_boto_manager.py` -- unit test that executes the lambda function with mocked data (record, playback and no mocking tests)

# Installation

To get this repo running:

* Install Python 2.7.  You can find instructions [here](https://wiki.python.org/moin/BeginnersGuide/Download).
* Install [virtual environment](https://docs.python.org/3/library/venv.html) using [pip](https://pip.pypa.io/en/stable/installing/)
`python -m pip install -U virtualenv`
* Create a directory for virtual environments
`mkdir envs` 
`cd envs`
* Create a [virtual environment](https://docs.python.org/3/library/venv.html).
`python -m virtualenv vboto_manager`
* Navigate to new virtual environment
`cd vboto_manager`
* Activate new virtual environment
`Scripts\activate`
* Clone this repo `git clone https://github.com/sjdillon/boto_manager`  
* Navigate into the folder `cd boto_manager`
* Install the requirements with `pip install -r requirements.txt`

# Usage

* Set path `set PYTHONPATH=%PYTHONPATH%;.`
* Execute the unit tests `pytest -vs`

You should see output of the unit test session and mock data in the boto_manager\mock_data directory
