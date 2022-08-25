import boto3

print("started")


s3 = boto3.resource('s3',region_name='ap-south-1', aws_access_key_id='AKIAZ2R57EWW6N4FJEMK', aws_secret_access_key='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')
s3_client = boto3.client('s3')
response = s3.meta.client.upload_file(r'C:\Users\HY20367012\Documents\train.csv','ninthjenkins','train.csv')
print("the file was successfully upload")