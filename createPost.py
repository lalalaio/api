import boto3
import datetime
import uuid

def main(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    post = dynamodb.Table('post')
    created = datetime.datetime.utcnow().isoformat()
    day = created.split('T')[0]
    
    result = post.put_item(
        Item={
            'uuid': str(uuid.uuid4()),
            'created': created,
            'day': day,
            'person_uuiid': event.get('person_uuid', ''),
            'notes': event.get('notes', [])
        }
    )
    
    return True
