import Adafruit_CharLCD as adaLCD


class LCD():

    def __init__(self, lcd_rs=25, lcd_en=24, lcd_d4=23, lcd_d5=17, lcd_d6=18, lcd_d7=22, lcd_backlight=2, cols=16, rows=2):
        self.lcd = adaLCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, cols, rows, lcd_backlight)
        
    def display_on_lcd(self, message):
        self.clear_lcd()
        self.lcd.message(message)
    
    def clear_lcd(self):
        self.lcd.clear()