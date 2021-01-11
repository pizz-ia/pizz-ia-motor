import boto3

class S3Client:

    def __init__(self, endpoint_url):
        self.client = boto3.client(
            's3',
            endpoint_url=endpoint_url
        )
    
    def create_bucket(self, bucket_name):
        self.client.Bucket(bucket_name).create()
        self.client

        return self.client.Bucket(bucket_name)
    
    def get_bucket(self, bucket_name):
        return self.client.Bucket(bucket_name)

    def put_object(bucket, file_path, object_key, callback=None):
        bucket.upload_file(object_path, object_key, callback)
