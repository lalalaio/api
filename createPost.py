import boto3
import datetime
import json
import uuid

def main(event, context):
    
    body = json.loads(event.get('body', '{}'))
    
    dynamodb = boto3.resource('dynamodb')
    post = dynamodb.Table('post')
    created = datetime.datetime.utcnow().isoformat()
    day = created.split('T')[0]
    
    result = post.put_item(
        Item={
            'uuid': str(uuid.uuid4()),
            'created': created,
            'day': day,
            'person_uuiid': body.get('person_uuid', ''),
            'notes': body.get('notes', [])
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'success': True
        })
    }
    
