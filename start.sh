i2cdetect -y 1
modprobe i2c-dev && modprobe bcm2835-v4l2 && python src/app.py