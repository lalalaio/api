import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime, timedelta
import json

def main(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    post = dynamodb.Table('post')
    now = datetime.utcnow()
    
    items = []
    
    while len(items) < 2:
    
        day = now.isoformat().split('T')[0]
        response = post.query(
            IndexName='day-index',
            KeyConditionExpression=Key('day').eq(day)
        )
        now = now - timedelta(days=1)
        items = items + [item.get('uuid') for item in response.get('Items', [])]

    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps(items)
    }    
