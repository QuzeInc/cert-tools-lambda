import boto3
import json
def handler(event,context):
  client = boto3.client('ecs')
  responseBody = client.run_task(
  cluster='cert-tools-cluster', # name of the cluster
  launchType = 'EC2',
  taskDefinition='cert-tools-task:1', # replace with your task definition name and revision
  count = 1,
  overrides = {
	'containerOverrides': [
	{
		'name':'cert-tools-container',
		'environment' : [
			{
				'name':'issuer',
				'value':event['pathParameters']['issuer']
			},
			{
				'name':'batchId',
				'value':event['pathParameters']['batchId']
			},
			{
				'name':'AWS_ACCESS_KEY_ID',
				'value':'' # Enter the values
			},
			{
				'name':'AWS_DEFAULT_REGION',
				'value':'us-east-1'
			},
			{
				'name':'AWS_SECRET_ACCESS_KEY',
				'value':'' # Enter the values
			}
		]
	}
	]
  }
  )

  response = {
	'statusCode':200,
	'body':json.dumps('',default=str),
	'isBase64Encoded':False
  }
  return response
