import os
import boto3

sqs = boto3.client('sqs', verify=False)
QUEUE_URL = os.environ.get('SQS_QUEUE_URL')


def send_message(message: str):
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=message
    )

    return response
