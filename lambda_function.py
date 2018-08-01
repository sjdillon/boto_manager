#!python
# ==========================================================#
# project        :SJD Automation
# title          :lambda_function.py
# description    :simple sample lambda function to test boto mocking
# author         :sjdillon
# date           :06/18/2018
# python_version :2.7.8
# notes          :
# ==========================================================#
import os
import logging
import json
import boto_manager as bm

logging.basicConfig(format="%(asctime)s - %(thread)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

prefix1 = os.environ['prefix1']
prefix2 = os.environ['prefix2']
env = os.environ['env']
region = os.environ['region']
iac_version = os.environ['iac_version']


def get_topics(event):
    # add the aws service and region to params event
    event['service'] = 'sns'
    event['region'] = region

    # create instance of BotoClientManager
    bc = bm.BotoClientManager(event)

    # create boto client
    client = bc.get_client()

    # get AWS sns topics using boto
    topics = client.list_topics()
    return topics


def lambda_handler(event, context):
    logger.info('event: {}'.format(event))
    response = get_topics(event)
    return response
