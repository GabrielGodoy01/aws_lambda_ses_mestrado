import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("ses")
    
    subject = "E-mail automático"
    
    body = "Este é um e-mail automático enviado pelo AWS EventBridge"
    
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    
    response = client.send_email(Source = "gabriel.godoybz@gmail.com", Destination = {"ToAddresses": ["gabriel.godoybz@hotmail.com"]}, Message = message)
    
    return response
