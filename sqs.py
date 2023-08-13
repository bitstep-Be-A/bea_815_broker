import os
import boto3

sqs = boto3.client('sqs')
QUEUE_URL = os.environ.get('SQS_QUEUE_URL')


def send_message(message: str, id: str):
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=message,
        MessageGroupId=os.environ.get('SQS_GROUP_ID'),
        MessageDeduplicationId=id
    )

    return response
