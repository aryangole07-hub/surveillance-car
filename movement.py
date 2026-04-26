import curses
import time
from time import sleep
import RPi.GPIO as GPIO

#define the outpouts of each gpio pins in which "in"

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

#setup GPIO ports
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fin1,GPIO.OUT)
GPIO.setup(fin2,GPIO.OUT)
GPIO.setup(fin3,GPIO.OUT)
GPIO.setup(fin4,GPIO.OUT)
GPIO.setup(bin1,GPIO.OUT)
GPIO.setup(bin2,GPIO.OUT)
GPIO.setup(bin3,GPIO.OUT)
GPIO.setup(bin4,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#define a curses main to call upon

def c_main(stdscr: 'curses._CursesWindow') -> int:
    while (True):

        #ask char from user and gives the output for the last input untill new input and gets a new screen to covor the old one

        char = stdscr.get_wch()
        
        if char == 'k' or char == 'K':
            print("Quit")
            GPIO.output(bin1, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(bin2, GPIO.LOW)#Left back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin3, GPIO.LOW)#Right back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin4, GPIO.LOW)#Right back wheels clockwise (Backwards) is not true
            GPIO.output(fin1, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(fin2, GPIO.LOW)#Left back wheels counter-clockwise (Forwards) is not true
            GPIO.output(fin3, GPIO.LOW)#Right back wheels clockwise (Forwards) is not true
            GPIO.output(fin4, GPIO.LOW)#Right back wheels counter-clockwise (Backwards) is not true
            break
        if char == 'a' or char == 'A':
            print("Right")
            GPIO.output(bin1, GPIO.LOW)#Right back wheels clockwise (Forwards) is true
            GPIO.output(bin2, GPIO.LOW)#Right back wheels counter-clockwise (Backwards) is not true
            GPIO.output(bin3, GPIO.HIGH)#Left back wheels counter-clockwise (Forwards) is true
            GPIO.output(bin4, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(fin1, GPIO.HIGH)#Left front wheels clockwise (Backwards) is true
            GPIO.output(fin2, GPIO.LOW)#Left front wheels counter-clockwise (Forwards) is not true
            GPIO.output(fin3, GPIO.LOW)#Right front wheels clockwise (Forwards) is true
            GPIO.output(fin4, GPIO.LOW)#Right front wheels counter-clockwise (Backwards) is not true
        if char == 'w' or char == 'W':
            print("Forward")
            GPIO.output(bin1, GPIO.HIGH)#Right back wheels clockwise (Forwards) is true
            GPIO.output(bin2, GPIO.LOW)#Right back wheels counter-clockwise (Backwards) is not true
            GPIO.output(bin3, GPIO.HIGH)#Left back wheels counter-clockwise (Forwards) is true
            GPIO.output(bin4, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(fin1, GPIO.HIGH)#Left front wheels clockwise (Backwards) is true
            GPIO.output(fin2, GPIO.LOW)#Left front wheels counter-clockwise (Forwards) is not true
            GPIO.output(fin3, GPIO.HIGH)#Right front wheels clockwise (Forwards) is true
            GPIO.output(fin4, GPIO.LOW)#Right front wheels counter-clockwise (Backwards) is not true
        if char == 'd' or char == 'D':
            print("Left")
            GPIO.output(bin1, GPIO.HIGH)#Right back wheels clockwise (Forwards) is true
            GPIO.output(bin2, GPIO.LOW)#Right back wheels counter-clockwise (Backwards) is not true
            GPIO.output(bin3, GPIO.LOW)#Left back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin4, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(fin1, GPIO.LOW)#Left front wheels clockwise (Backwards) is not true
            GPIO.output(fin2, GPIO.LOW)#Left front wheels counter-clockwise (Forwards) is not true
            GPIO.output(fin3, GPIO.HIGH)#Right front wheels clockwise (Forwards) is true
            GPIO.output(fin4, GPIO.LOW)#Right front wheels counter-clockwise (Backwards) is not true
        if char == 's' or char == 'S':
            print("Backward")
            GPIO.output(bin1, GPIO.LOW)#Right back wheels clockwise (Forwards) is not true
            GPIO.output(bin2, GPIO.HIGH)#Right back wheels counter-clockwise (Backwards) is true
            GPIO.output(bin3, GPIO.LOW)#Left back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin4, GPIO.HIGH)#Left back wheels clockwise (Backwards) is true
            GPIO.output(fin1, GPIO.LOW)#Left front wheels clockwise (Backwards) is not true
            GPIO.output(fin2, GPIO.HIGH)#Left front wheels counter-clockwise (Forwards) is true
            GPIO.output(fin3, GPIO.LOW)#Right front wheels clockwise (Forwards) is not true
            GPIO.output(fin4, GPIO.HIGH)#Right front wheels counter-clockwise (Backwards) is true
        if char == 'x' or char == 'X':
            print("Stop")
            GPIO.output(bin1, GPIO.LOW)#Left back wheels clockwise (Backwards) is not true
            GPIO.output(bin2, GPIO.LOW)#Left back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin3, GPIO.LOW)#Right back wheels counter-clockwise (Forwards) is not true
            GPIO.output(bin4, GPIO.LOW)#Right back wheels clockwise (Backwards) is not true
            GPIO.output(fin1, GPIO.LOW)#Left front wheels clockwise (Backwards) is not true
            GPIO.output(fin2, GPIO.LOW)#Left front wheels counter-clockwise (Forwards) is not true
            GPIO.output(fin3, GPIO.LOW)#Right front wheels clockwise (Forwards) is not true
            GPIO.output(fin4, GPIO.LOW)#Right front wheels counter-clockwise (Backwards) is not true


#define main to do everything
#Curses.wrapper sets up the whole screen structure  

def main() -> int:
    
    #give instructions for driving after new screen loads so they dont disappear

    print("Press W to go Forward")
    print("Press A to go Left")
    print("Press S to go Backward")
    print("Press D to go Right")
    print("Press X to Stop")
    print("Press K to Quit")
    print("PLEASE WAIT 10 SECONDS (until this disapears)")

    #give 10 secs to read as curses.wrapper clears the screen

    time.sleep(1)

    return curses.wrapper(c_main)

if __name__ == '__main__':
    exit(main())
