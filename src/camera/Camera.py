from picamera import PiCamera
from time import sleep

class Camera:

    def __init__(self):
        self.camera = PiCamera()

    def shoot(self, save_path, name):
        self.camera.start_preview()
        # it’s important to sleep for at least two seconds before capturing an image,
        #  because this gives the camera’s sensor time to sense the light levels.
        sleep(5)
        self.camera.capture(f"{save_path}/{name}.jpg")
        self.camera.stop_preview()

        return f"{save_path}/{name}.jpg"
    
    def shoot_multiple_time(self, save_path, name, loop_count):
        self.camera.start_preview()
        for i in range(loop_count):
            sleep(5)
            self.camera.capture(f"{save_path}/{name}-{i}.jpg")
        self.camera.stop_preview()

        return [f"{save_path}/{name}-{i}.jpg" for i in range(loop_count)]