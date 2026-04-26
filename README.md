# Surveillance Car

A Raspberry Pi based Wi-Fi-controlled surveillance car with keyboard movement control, live video streaming, and ultrasonic obstacle detection.

## Overview

This project uses a Raspberry Pi to control a robotic surveillance car over a local Wi-Fi network. The car receives keyboard inputs through an Ubuntu system and moves accordingly. A live video feed is hosted on the Raspberry Pi and can be viewed through its local IP address in a browser.

The car also includes an ultrasonic distance sensor for obstacle detection. If an obstacle is detected within 30 cm, the motor outputs are stopped automatically for safety. Since the distance is checked frequently, the car may move slightly with each input, allowing it to be moved away from an obstacle using repeated control inputs.

## Features

- Keyboard-based movement control
- Live video feed through local IP address
- Ultrasonic obstacle detection
- Automatic motor stop below 30 cm
- Raspberry Pi GPIO based motor control
- Local Wi-Fi communication
- Safety logic for collision prevention

## Hardware Used

- Raspberry Pi
- Ultrasonic distance sensor
- Motor driver module
- DC motors
- Car chassis
- Camera module
- wires
- Battery or external power supply

## Software Used

- Python
- RPi.GPIO
- curses
- Ubuntu
- Local web server

## Controls

| Key | Action |
|---|---|
| W | Move Forward |
| A | Turn Left |
| S | Move Backward |
| D | Turn Right |
| X | Stop |
| K | Quit |

## Obstacle Detection Logic

The ultrasonic sensor measures the distance between the car and nearby obstacles using TRIG and ECHO pins. If the measured distance is less than 30 cm, all motor output pins are set to LOW, stopping the car.

This prevents the car from continuously moving into an obstacle while still allowing small controlled movements so that it can be moved away safely.

## Video Feed

The live video feed remains active wether the car is running or not as long as the Raspberry-Pi is powered. It can be viewed by opening the Raspberry Pi’s local IP address in a browser on the same network.

## Project Files

```text
surveillance-car/
├── movement_control.py
├── obstacle_detection.py
└── README.md
