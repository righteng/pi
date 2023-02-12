import wiringpi as pi
import time
import datetime

SENS_PIN = 18
LED_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(SENS_PIN, pi.INPUT)
print("Operating the Sencer.")

while True:
    if(pi.digitalRead(SENS_PIN) == pi.HIGH):
        dt_now = datetime.datetime.now()
        print(dt_now)
        pi.digitalWrite(LED_PIN,pi.HIGH)
        time.sleep(5)
    else:
        pi.digitalWrite(LED_PIN,pi.LOW)
        time.sleep(1)