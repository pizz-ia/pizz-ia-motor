import time
import RPi.GPIO as GPIO


class MotorClient:

    def __init__(self, control_pins=[6, 13, 19, 26]):
        self.control_pins = control_pins
        for pin in control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        self.periodical_seq = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]
        ]

    def start_motor_by_period(self, period):
        """
         Distance of the motor traction equal period * circumference
        """
        for i in range(int(period*512)):
            for halfstep in range(len(self.periodical_seq)):
                for pin in range(len(self.control_pins)):
                    GPIO.output(self.control_pins[pin], self.periodical_seq[halfstep][pin])
                    time.sleep(0.001)