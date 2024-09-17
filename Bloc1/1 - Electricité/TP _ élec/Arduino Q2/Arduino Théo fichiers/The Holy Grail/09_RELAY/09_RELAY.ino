int PHOTOSENSOR = A0;
void setup() {
 Serial.begin(9600);
 pinMode(PHOTOSENSOR, INPUT);
}
void loop() {
 int analogValue = analogRead(PHOTOSENSOR);
 Serial.print("Analog reading: ");
 Serial.println(analogValue);
 delay(500);
}