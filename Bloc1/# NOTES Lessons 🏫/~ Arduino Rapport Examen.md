---
created: 2024-03-13
tags:
  - Lessons/School/HEH/Bloc1/Quad2
---

# 🏫 Arduino Rapport d'Examen 
> **Création de la note à *`17:46`* le *`2024-03-13`.***
[[Techniques d'interfaçage TP - HEHB1Q2|Techniques d'interfaçage TP - HEHB1Q2]] 

## Exercice 6
### Code
```c
// Code réalisé par Corentin Lallement
// Cours d'Arduino avec Monsieur Arnaud à l'école HEH

#include <Stepper.h>  

const int stepsPerRevolution = 200;
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

int ledPin = 5;
int buttonPin;
int ledIndicatorPin;
unsigned long previousMillis = 0;
const long interval = 200;

int joystickValueY = 0;
int joystickValueX = 0;  

void setup() {
  pinMode(ledPin, OUTPUT);

  buttonPin = 3;
  ledIndicatorPin = 13;
  pinMode(ledIndicatorPin, OUTPUT);
  pinMode(buttonPin, INPUT);

  Serial.begin(9600);
  myStepper.setSpeed(60);

}

void loop() {
  boolean isButtonPressed = digitalRead(buttonPin);

  // Si le bouton est enfoncé, allume la LED et fait tourner le moteur
  if (isButtonPressed == HIGH) {
    digitalWrite(ledIndicatorPin, HIGH);
    joystickValueX = analogRead(A1);
    joystickValueY = analogRead(A2);

    // Calcul de la moyenne des valeurs de X et Y
    int moyenneJoystick = (joystickValueX + joystickValueY) / 2;

    // Utilise la moyenne du joystick pour faire tourner le moteur
    myStepper.step(moyenneJoystick);
  } else {
    // Si le bouton est relâché, éteint la LED
    digitalWrite(ledIndicatorPin, LOW);
  }

  // Reste du code pour le clignotement de la LED
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;  
    if (digitalRead(ledPin) == HIGH) {
      digitalWrite(ledPin, LOW);
    } else {
      digitalWrite(ledPin, HIGH);
    }
  }
  // Délai entre les étapes pour éviter des actions trop rapides
  delay(50);
}
```
### Image
![[_Assets 💼/Pasted image 20240313153326.png]] 