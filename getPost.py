import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime, timedelta
import json

def main(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    post = dynamodb.Table('post')
    path = event.get('params', {}).get('path', {})

    response = post.query(
        KeyConditionExpression=Key('uuid').eq(path.get('uuid', ''),)
    )
    
    items = response.get('Items', [])
    
    if len(items) > 0:
        return items[0]

    return {'error': 'Post not found'}
