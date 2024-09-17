int BTN = 3;
int BTN2 = 4;
int LED = 13;
int LED2 = 12;
int value;
int value2;
void setup() {
 pinMode(BTN, INPUT);
 pinMode(BTN2, INPUT);
 pinMode(LED, OUTPUT);
 pinMode(LED2, OUTPUT);
}
void loop() {
 value = digitalRead(BTN);
 if (value == HIGH) {
 digitalWrite(LED, LOW);
 } else {
 digitalWrite(LED, HIGH);
 }
 value2 = digitalRead(BTN2);
 if (value2 == HIGH) {
 digitalWrite(LED2, HIGH);
 } else {
 digitalWrite(LED2, LOW);
 }
}
