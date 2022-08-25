import boto3
print("started")

# Create an S3 client
s3 = boto3.resource('s3',region_name='ap-south-1', aws_access_key_id='AKIAZ2R57EWW6N4FJEMK', aws_secret_access_key='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')

# Call S3 to list current buckets
import boto3


response = s3.create_bucket(
      Bucket = 'ninthjenkins',

    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }


)
print("bucket was created successfully")

