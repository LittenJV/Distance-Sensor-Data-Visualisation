import requests

r = requests.get("https://sqs.us-east-2.amazonaws.com/189794443393/InternQueue?Action=ReceiveMessage&WaitTimeSeconds=20&VisibilityTimeOut=15&AttributeName=All&MaxNumberOfMessages=10")




