int RED = A1;
int GREEN = A2;
int BLUE = A3;
void setup() {
 pinMode(RED, OUTPUT);
 pinMode(GREEN, OUTPUT);
 pinMode(BLUE, OUTPUT);
}
void loop() {
 analogWrite(RED, 255);
 analogWrite(GREEN, 0);
 analogWrite(BLUE, 255);
}
