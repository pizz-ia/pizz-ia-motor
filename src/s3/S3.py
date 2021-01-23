import boto3

class S3Client:

    def __init__(self, endpoint_url):
        self.s3 = boto3.resource(
            's3',
            endpoint_url=endpoint_url
        )
    
    def create_bucket(self, bucket_name):
        self.s3.Bucket(bucket_name).create()
        return self.s3.Bucket(bucket_name)
    
    def get_bucket(self, bucket_name):
        return self.s3.Bucket(bucket_name)

    def put_object(self, bucket, file_path, object_key, callback=None):
        bucket.upload_file(file_path, object_key, Callback=callback)
