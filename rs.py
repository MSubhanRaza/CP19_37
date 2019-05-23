import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
  pir_sensor = 13 #sensor pin number
  led_pin = 7 #led pin nunmber
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pir_sensro,GPIO.IN)
  GPIO.setup(led_pin,GPIO.OUT)

  while(True):
    time.sleep(1)
    current_state = GPIO.input(pir_sensor)
    if current_state:
      GPIO.output(LEDPin, True)
    time.sleep(1)
    GPIO.output(LEDPin, False)