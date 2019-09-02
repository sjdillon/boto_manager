# Boto Client Manager
[![Build Status](https://travis-ci.org/sjdillon/boto_manager.svg?branch=master)](https://travis-ci.org/sjdillon/boto_manager)

The BotoClientManager is a class that abstracts the creation of boto clients and allows "injecting" mocking into AWS calls.  Placebo requires the creation of a boto session along with the boto client.  BotoClientManager allows both recording and playback of mock data.

* `boto_client_manager.py` -- creates and manages boto sessions and clients, allows mocking playback and recording
* `tests\test_boto_manager.py` -- unit test that executes the lambda function with mocked data (record, playback and no mocking tests)


## Quick Start
install boto_manager


```python
!pip install git+https://github.com/sjdillon/boto_manager | tail -n 1
```

      Running command git clone -q https://github.com/sjdillon/boto_manager /tmp/pip-req-build-o8i52ub4
    Successfully built boto-manager


Set up credentials (in e.g. ~/.aws/credentials):
```
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET`
```

Set up a default region (in e.g. ~/.aws/config):
```
[default]
region=us-east-1
```

# Usage

create a folder to store mock files


```python
!mkdir mock_data/
```

record: save boto call response to mock file


```python
import os
import logging
import boto_manager

logging.basicConfig(format="%(asctime)s - %(thread)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create an event to be passed to BotoClientManager
event={}
event['service'] = 'sns'
event['region'] = 'us-west-2'

# set the path to store the mock files
mock_data_path = os.path.join(os.path.dirname(os.path.abspath('.')), 'mock_data')
event['mock_data_path'] = mock_data_path

# set to record calls
event['mock_mode'] = 'record'

# create a boto_client_manager boto client
bc=boto_manager.BotoClientManager(event)
client = bc.get_client()

# run a boto call to aws (and record data for mocking)
result = client.list_subscriptions()
logger.info('result: {}'.format(result))
assert 'Subscriptions' in result

```

    2019-09-01 21:07:50,921 - 140671852791616 - INFO - recording boto to /home/sjdillon/jupyter/mock_data
    2019-09-01 21:07:50,924 - 140671852791616 - INFO - Found credentials in shared credentials file: ~/.aws/credentials
    2019-09-01 21:07:51,419 - 140671852791616 - INFO - result: {'Subscriptions': [{'SubscriptionArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-sns-pipeline-approve:590ffd51-5ff2-415c-825b-d144bcdafcc6', 'Owner': '000000000000', 'Protocol': 'email', 'Endpoint': 'sjdillon.dillon.com', 'TopicArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-sns-pipeline-approve'}, {'SubscriptionArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-deploy-events:77b3e8d6-e7dd-4243-b6fd-f51defa71e8d', 'Owner': '000000000000', 'Protocol': 'email', 'Endpoint': 'sjdillon.dillon.com', 'TopicArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-deploy-events'}], 'NextToken': 'AAGoclrsijma6fqTf/zmfTYNc++0cggCxdo/nm2QK6c7KQ==', 'ResponseMetadata': {'RequestId': 'b19aad38-be9e-504b-ada6-f8ded33939b8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b19aad38-be9e-504b-ada6-f8ded33939b8', 'content-type': 'text/xml', 'content-length': '1173', 'date': 'Mon, 02 Sep 2019 01:07:50 GMT'}, 'RetryAttempts': 0}}


confirm: check that a mock file was created


```python
assert 'sns.ListSubscriptions_1.json' in os.listdir(mock_data_path)
os.listdir(mock_data_path)

```




    ['sns.ListSubscriptions_1.json', 'sns.ListSubscriptions_2.json']



playback: run the same call using the mock file


```python
event['mock_mode'] = 'playback'

# create a new client that specifies playback mode
bc=boto_manager.BotoClientManager(event)
client = bc.get_client()

# run the boto aws call
result = client.list_subscriptions()
logger.info('result: {}'.format(result))
assert 'Subscriptions' in result

```

    2019-09-01 20:30:31,518 - 140671852791616 - INFO - playing back mock boto calls from /home/sjdillon/jupyter/mock_data
    2019-09-01 20:30:31,531 - 140671852791616 - INFO - Found credentials in shared credentials file: ~/.aws/credentials
    2019-09-01 20:30:31,589 - 140671852791616 - INFO - result: {'Subscriptions': [{'SubscriptionArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-sns-pipeline-approve:590ffd51-5ff2-415c-825b-d144bcdafcc6', 'Owner': '000000000000', 'Protocol': 'email', 'Endpoint': 'sjdillon.dillon.com', 'TopicArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-sns-pipeline-approve'}, {'SubscriptionArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-deploy-events:77b3e8d6-e7dd-4243-b6fd-f51defa71e8d', 'Owner': '000000000000', 'Protocol': 'email', 'Endpoint': 'sjdillon.dillon.com', 'TopicArn': 'arn:aws:sns:us-west-2:000000000000:sjd-demo-dev-deploy-events'}], 'NextToken': 'AAHoZj78oUtiutI0qTxPoubt0a25vsa5vgdOyqsWkuCunA==', 'ResponseMetadata': {'RequestId': 'ded87dae-c1e3-5739-88c6-2848f9d246d4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'ded87dae-c1e3-5739-88c6-2848f9d246d4', 'content-type': 'text/xml', 'content-length': '1173', 'date': 'Sun, 01 Sep 2019 21:19:45 GMT'}, 'RetryAttempts': 0}}
