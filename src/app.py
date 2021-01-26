import uuid
import time
from s3.S3 import S3Client
from camera.Camera import Camera
from lcd.LCD import LCD
import os

def display_on_lcd(message):
    lcd_rs = 25
    lcd_en = 24
    lcd_d4 = 23
    lcd_d5 = 17
    lcd_d6 = 18
    lcd_d7 = 22
    lcd_backlight = 2

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 16
    lcd_rows = 2

    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    
    lcd.clear()
    lcd.message('OLIVES\nPEPERONI')
    time.sleep(5.0)
    

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

