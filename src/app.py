import uuid
import time

from api.API import APIClient
from camera.Camera import Camera
from lcd.LCD import LCD
import os

SAVE_PICTURE_PATH = "/data"

if __name__ == "__main__":
    print("App is running")
    cam = Camera()
    picture_path = cam.shoot(SAVE_PICTURE_PATH, "python-test")
    print("Picture taked")

    api = APIClient("https://api.pizzia.k8s.jeremychauvin.fr")
    api.predict(picture_path)

    lcd = LCD()
    lcd.display_on_lcd('coucou')