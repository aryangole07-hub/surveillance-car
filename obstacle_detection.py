import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

fin1 = 4
fin2 = 27
fin3 = 22
fin4 = 23
bin1 = 24
bin2 = 25
bin3 = 5
bin4 = 6
TRIG = 26
ECHO = 13

GPIO.setwarnings(False)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(fin1,GPIO.OUT)
GPIO.setup(fin2,GPIO.OUT)
GPIO.setup(fin3,GPIO.OUT)
GPIO.setup(fin4,GPIO.OUT)
GPIO.setup(bin1,GPIO.OUT)
GPIO.setup(bin2,GPIO.OUT)
GPIO.setup(bin3,GPIO.OUT)
GPIO.setup(bin4,GPIO.OUT)

try:
    
    while True:
        
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        
        GPIO.output(TRIG, True)#emiting ultrasonic sound
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()#time sound was emitted
        
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()#time sound was recieved
        
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17150
        
        distance = round(distance, 2)
        
        d= f'{distance:.2f}'
        
        print ("Distance is:" + d + "cm")
        if distance < 30:
            GPIO.output(bin1, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(bin2, GPIO.LOW)#Left back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin3, GPIO.LOW)#Right back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin4, GPIO.LOW)#Right back wheels clockwise (Backwards) is not true
            GPIO.output(fin1, GPIO.LOW)#Left front wheels clockwise (Backwards) is not true
            GPIO.output(fin2, GPIO.LOW)#Left front wheels counter-clockwise (Forwards) is not true
            GPIO.output(fin3, GPIO.LOW)#Right front wheels clockwise (Forwards) is not true
            GPIO.output(fin4, GPIO.LOW)#Right front wheels counter-clockwise (Backwards) is not true
        
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
    GPIO.cleanup()
