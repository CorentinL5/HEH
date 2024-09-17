int SHOCK_PIN = 12;
void setup() {
 pinMode(LED_BUILTIN, OUTPUT); // on-board LED, usua
 pinMode(SHOCK_PIN, INPUT); // shock sensor pin s
}
void loop() {
 if (digitalRead(SHOCK_PIN)) { // shock detected?
 // shock detected with pull-down resistor
 digitalWrite(LED_BUILTIN, HIGH); // switch LED on
 delay(2000); // leave LED on for
 }
 else {
 // shock not detected with pull-down resistor
 digitalWrite(LED_BUILTIN, LOW); // switch LED off
 }
}