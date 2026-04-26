# surveillance-car
This project is a Raspberry Pi based Wi-Fi-controlled surveillance car. 
The car can be controlled using keyboard inputs and includes an ultrasonic distance sensor for obstacle detection. 
When an obstacle is detected within 30 cm, the motor outputs are stopped automatically for safety. The distance is checked frequently enough for it to still move a little for every input. Hence, the car can still be moved away from the obstacle by giving repeted inputs.
Live video feed (always active) is also shown.
inputs are passed on to the car by ubuntu, feed is shown at the IP (local website)
