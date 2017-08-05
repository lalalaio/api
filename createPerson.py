import boto3
import datetime
import uuid

def main(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    person = dynamodb.Table('person')

    person.put_item(
        Item={
            'uuid': str(uuid.uuid4()),
            'created': datetime.datetime.utcnow().isoformat(),
            'identity': 'test',
            'key': 'test',
        }
    )
    
    return True
