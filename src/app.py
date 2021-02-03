import requests
from api.API import APIClient
from motor.Motor import MotorClient
from lcd.LCD import LCD

PERIOD = 0.64

PI_URL = "http://192.168.66.120:5000"

if __name__ == "__main__":
    print("App is running")
    lcd = LCD()
    lcd.clear_lcd()
    api = APIClient("https://api.pizzia.k8s.jeremychauvin.fr")
    motor = MotorClient()

    treatment_id = None
    while True:
        result = api.last_predict()
        if result.get('id', None) != treatment_id:
            print(result.get('id', None))
            motor.start_motor_by_period(PERIOD)
            msg = result.get('message', "")
            if len(msg) > 16:
                msg = [*msg[:16], '\n', *msg[16:]]
            lcd.display_on_lcd(msg)
            treatment_id = result.get('id', None)
            r = requests.get(f'{PI_URL}/picture')