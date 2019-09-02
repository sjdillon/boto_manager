#!python
# ==========================================================#
# project        :sjdillon
# title          :test_boto_manager.py
# description    :unit test for boto_manager which abstracts and
#                 centralizes common configuration conventions used in this framework
# author         :sjdillon
# date           :06/18/2018
# python_version :3.7
# notes          :
# ==========================================================#
import logging
import os

import boto_manager.boto_client_manager as bm

logging.basicConfig(format="%(asctime)s - %(thread)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# to simulate lambda, load vars into environ vars
os.environ['region'] = 'us-west-2'
os.environ['profile'] = 'default'
os.environ['prefix1'] = 'sjd'
os.environ['prefix2'] = 'demo'
os.environ['env'] = 'dev'
os.environ['account_id'] = '000000000000'
os.environ['iac_version'] = '1'


def test_boto_manager(mode='playback'):
    """
    Test making a mocked playback call using boto
    :param mode: mock mode - record, playback or None
    :return:
    """
    event = {}
    # GIVEN an event requesting mocked playback data be used
    if mode:
        event['mock_mode'] = mode
        event['mock_data_path'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mock_data')
    # add the aws service and region to params event
    event['service'] = 'sns'
    event['region'] = 'us-west-2'

    # WHEN we make a boto call to s3
    # create instance of BotoClientManager
    bc = bm.BotoClientManager(event)
    # create boto client
    client = bc.get_client()
    # get AWS sns topics using boto

    # THEN we get results from mocked calls
    event = client.list_topics()
    logger.info('result: {}'.format(event))
    assert 'Topics' in event
