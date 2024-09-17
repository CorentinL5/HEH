int hbridgeIN1 = 2;
int hbridgeIN2 = 3;
void setup() {
 pinMode(hbridgeIN1, OUTPUT);
  pinMode(hbridgeIN2, OUTPUT);
}
void loop() {
 digitalWrite(hbridgeIN1, HIGH);
 delay(1000);
 digitalWrite(hbridgeIN1, LOW);
 digitalWrite(hbridgeIN2, HIGH);
 delay(1000);
 digitalWrite(hbridgeIN2, LOW);
}
