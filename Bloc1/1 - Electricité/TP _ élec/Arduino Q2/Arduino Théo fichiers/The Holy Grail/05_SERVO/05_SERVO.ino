#include <Stepper.h>
int in1Pin = 11;
int in2Pin = 10;
int in3Pin = 9;
int in4Pin = 8;
int revolution = 4000;
Stepper myStepper = Stepper(revolution, in4Pin, in3Pin, in2
void setup() {
 // Set the speed to 5 rpm:
 myStepper.setSpeed(5);
}
void loop() {
 // Step one revolution in one direction:
 myStepper.step(revolution);
 delay(500);

 // Step one revolution in the other direction:
 myStepper.step(-revolution);
 delay(500);
}