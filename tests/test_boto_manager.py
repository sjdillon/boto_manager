#!python
# ==========================================================#
# project        :SJD Automation
# title          :test_boto_manager.py
# description    :unit test for boto_manager which abstracts and centralizes common configuration conventions used in this framework
# author         :sjdillon
# date           :06/18/2018
# python_version :2.7.8
# notes          :
# ==========================================================#
import os
import logging

logging.basicConfig(format="%(asctime)s - %(thread)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

## to simulate lambda, load vars into environ vars
os.environ['region'] = 'us-west-2'
os.environ['profile'] = 'default'
os.environ['prefix1'] = 'sjd'
os.environ['prefix2'] = 'demo'
os.environ['env'] = 'dev'
os.environ['account_id'] = '000000000000'
os.environ['iac_version'] = '1'
# the lambda_function uses environtal variables, must import after setting envion for test
import lambda_function as f


def run_lambda_function(mode=None):
    # prepare the params
    params = {}

    # inject mocking if needed
    if mode:
        params['mock_mode'] = mode
        params['mock_data_path'] = 'mock_data'

    # invoke the lambda function
    event = f.lambda_handler(params, '')
    logger.info('result: {}'.format(event))
    assert 'Topics' in event


def test_lambda_function_playback():
    logging.info('testing placebo playback')
    run_lambda_function(mode='playback')
