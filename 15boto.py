import boto3 # Boto3 is maintained and published by Amazon Web Services

# create an S3 client
# s3 = boto3.client('s3')
# print(s3)
 
#  # list all buckets in S3

# response = s3.list_buckets()  #error
# buckets = [bucket['Name'] for bucket in response['Buckets']]
# print(buckets)



s3 = boto3.client('s3')

# Create a new S3 bucket
bucket_name = 'my-bucket'
s3.create_bucket(Bucket=bucket_name)

# Upload a file to the bucket
file_path = 'task.py'
object_key = 'task.py'
s3.upload_file(file_path, bucket_name, object_key)

# List objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
for object in response['Contents']:
    print(object['Key'])