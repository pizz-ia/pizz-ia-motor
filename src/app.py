import uuid
from s3.S3 import S3Client
from camera.Camera import Camera

SAVE_PICTURE_PATH = "/data"
S3_ENDPOINT_URL = "https://object-store.par1.openstack.unyc.io"
S3_BUCKET_NAME = "capture"

def callback_upload_s3(bytes_uploaded):
    print(f"Bytes Uploaded: {bytes_uploaded}")

if __name__ == "__main__":
    print("App is running")
    cam = Camera()
    picture_path = cam.shoot(SAVE_PICTURE_PATH, "python-test")
    s3 = S3(S3_ENDPOINT_URL)
    bucket = None

    try:
        bucket = s3.create_bucket(S3_BUCKET_NAME)
    except expression as identifier:
        print(identifier)
        bucket = s3.get_bucket(S3_BUCKET_NAME)

    s3.put_object(bucket, picture_path, f"{uuid.uuid4()}.jpg", callback_upload_s3)