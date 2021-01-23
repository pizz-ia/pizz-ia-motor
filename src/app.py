import uuid
import time
from s3.S3 import S3Client
from camera.Camera import Camera
from lcd.LCD import LCD
import os

SAVE_PICTURE_PATH = "/data"
S3_ENDPOINT_URL = "https://object-store.par1.openstack.unyc.io"
S3_BUCKET_NAME = "capture"

def callback_upload_s3(bytes_uploaded):
    print(f"Bytes Uploaded: {bytes_uploaded}")

if __name__ == "__main__":
    print("App is running")
    cam = Camera()
    picture_path = cam.shoot(SAVE_PICTURE_PATH, "python-test")
    print("Picture taked")
    s3 = S3Client(S3_ENDPOINT_URL)
    bucket = None

    try:
        bucket = s3.create_bucket(S3_BUCKET_NAME)
        print("in the try")
    except:
        print("fail")
        bucket = s3.get_bucket(S3_BUCKET_NAME)

    s3_file_name =  f"{uuid.uuid4()}.jpg"
    s3.put_object(bucket, picture_path, s3_file_name, callback=callback_upload_s3)
    print(f"Picture send on S3 : {s3_file_name}")

    lcd = LCD()

