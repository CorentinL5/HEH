#include <IRremote.h>
#include <IRremoteInt.h>
int RECV_PIN = 7; // The digital pin that the sig
IRrecv receiver(RECV_PIN); // Create a new receiver objec
decode_results results; // A varuable that would be us
void setup() {
 Serial.begin(9600); // Setup serial port to send
 receiver.enableIRIn(); // Enable receiver so that it
elec code 10
}
void loop() {
 if(receiver.decode(&results)) { // Decode t
 Serial.println(results.value, HEX); // Print the
 receiver.resume(); // Continue
 }
}