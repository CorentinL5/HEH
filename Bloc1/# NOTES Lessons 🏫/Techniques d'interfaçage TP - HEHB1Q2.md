---
created: 2024-02-07
tags:
  - Lessons/School/HEH/Bloc1/Quad2
---

# # 📚  Techniques d'interfaçage TP HEHB1Q2
> **Création de la note à *`13:45`* le *`2024-02-07`.***
---
[[../Lessons 🏫/0 - Lessons Menu|🏫 - Lessons Menu]]

# 📝 Prise de Notes - Cours

---

## 👋 Infos du Cours
- **Professeur :** Arnaud

---

## 📅 Dates de cours

|     Date      |      heures      | Local | Note |                                                                                              |
| :-----------: | :--------------: | :---: | ---- | :------------------------------------------------------------------------------------------: |
| mer. 07 févr. | de 13h30 à 17h30 | 2/10C |      | [[Techniques d'interfaçage TP - HEHB1Q2#Note du ../Daily 📆/2024-02-07 2024-02-07\|Clique]]  |
| mer. 14 févr. | de 13h30 à 17h30 | 2/10C |      | [[Techniques d'interfaçage TP - HEHB1Q2#Note du ../Daily 📆/2024-02-14 2024-02-14 \|Clique]] |
| mer. 21 févr. | de 13h30 à 17h30 | 2/10C |      | [[Techniques d'interfaçage TP - HEHB1Q2#Note du ../Daily 📆/2024-02-21 2024-02-21\| Clique]] |
| mer. 28 févr. | de 13h30 à 17h30 | 2/10C |      |                    [[#Note du ../Daily 📆/2024-02-28 2024-02-28\|Clique]]                    |
| mer. 13 mars  | de 13h30 à 17h30 | 2/10C |      |                               [[#Note du 2024-03-13\|Clique]]                                |

---

## ❓ Questions à Poser

- [Question 1]
- [Question 2]
- [Question 3]

---

## 📚 Références

- [Référence 1]
- [Référence 2]
- [Référence 3]

---

## 🤔 Réflexions Rapides

- [Réflexion 1]
- [Réflexion 2]

---
## 📑 Notes

### Note du [[../Daily 📆/2024-02-07|2024-02-07]]
##### => Les Sorties
#### Dépôt
- ![[../_Assets 💼/LED - Arduino, TinkerCad, classe.pdf|LED - Arduino, TinkerCad, classe]]
#### Intro du cours
- Cours avec **Arduino** *(Arduino => crée pour les enfants)*
- Section faite du cours
	- [Accueil et explication](https://ecampus.heh.be/course/view.php?id=3014&section=1) 
	- [Les sorties](https://ecampus.heh.be/course/view.php?id=3014&section=2) 
- Parties de points
	- 40% EXAM [[Techniques d'interfaçage TH - HEHB1Q2]]
	- 30% du premier projet
	- 30% deuxième projet
- Le **`C`** fait moins d'erreurs au niveau du compilateur.
- [[../Random Notes 🧨/Quizineur| Quizz sur Arduino avec Quizzineur]] 10 questions sur l'exam
- Info sur l'Arduino
	- Arduino en série, terre, etc.
	- Le PC est protégé par l'Arduino.
#### Arduino sur TinkerCad 
![[../_Assets 💼/Pasted image 20240207141145.png]]
- RX - récepteur
- TX - transmetteur
![[../_Assets 💼/Pasted image 20240207141223.png]]
- Communication entre pc et PIC
![[../_Assets 💼/Pasted image 20240207141246.png]]
- [Lien Travail Tinkercad TP1 Sorties](https://www.tinkercad.com/things/eTH37bkJuIl-arduino-tp1-sorties?sharecode=lXwGY-W5HuWEvr_8Gcjc927WzkbAUUv_9NM3a0o-DeE)

---

### Note du [[../Daily 📆/2024-02-14|2024-02-14]]
##### => Les entrées
#### Dépôt
- ![[../_Assets 💼/Dépôt TP2 Arduino.pdf|Dépôt TP2 Arduino]]
#### À faire 
1. Faire un montage PULL UP
2. Faire un montage PULL DOWN
3. Utiliser une entrée analogique via un potentiomètre 
4. Utiliser le joystick
#### Prise de note
##### Début
  ![[../_Assets 💼/Pasted image 20240214104928.png]]
##### PULL UP, PULL DOWN
###### Pull up + code 
  ![[../_Assets 💼/Pasted image 20240214140735.png]] 
```C
int pinBouton;
int pinLed;
void setup()
{
	pinLed = 13;
	pinBouton = 3;
	pinMode(pinLed, OUTPUT);
	pinMode(pinBouton, INPUT);
}
void loop()
{
	boolean etatBouton = digitalRead(pinBouton);
	if(etatBouton == 1) {
	digitalWrite(pinLed, LOW);
	} else {
	digitalWrite(pinLed,HIGH);
	}
}
``` 
###### PULL DOWN + CODE
  ![[../_Assets 💼/Pasted image 20240214142027.png]]
```C
int pinBouton;
int pinLed;

void setup()
{
	pinLed = 13;
	pinBouton = 3;
	pinMode(pinLed, OUTPUT);
	pinMode(pinBouton, INPUT);
}

void loop()
{
		boolean etatBouton = digitalRead(pinBouton); 

	if(etatBouton == 1)
	{
	digitalWrite(pinLed, HIGH); //différence
	}
	else
	{
	digitalWrite(pinLed,LOW); //différence
	}
}
```
###### FINAL PULL U/D CODE
```C
int BTN = 3;
int BTN2 = 4;
int value;
int value2;
int LED = 13;
int LED2 = 12;
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
	digitalWrite(LED2, LOW);
  } else {
	digitalWrite(LED2, HIGH);
  }
}
```
##### Potentiomètre
```c
int valPot=0; //variable pour récupérer la tension aux bornes du potentiomètre traduitepar le CAN . On l’initialise à 0.
void setup() {
 Serial.begin(9600); //Initialisation de la communication avec la console
}
void loop() {
 valPot=analogRead(A0); //lit la tension, la convertit en valeur numérique et la stockedans valeurPot
 Serial.print("Valeur lue : ");
 Serial.println(valPot);
}
```
##### Joystick
```c
int valJoystickY=0;
int valJoystickX=0;

void setup() {
 Serial.begin(9600); //Initialisation de la communication avec la console
}

void loop()
{ //Joystick
 valJoystickX=analogRead(A1);
 valJoystickY=analogRead(A2);
 Serial.print("Joystick X:");
 Serial.println(valJoystickX);
 Serial.print("Joystick Y:");
 Serial.println(valJoystickY);
}
```
##### CODE FINALE (ALL)
```c
/*
CorentinLallement: 240214
*/
int valPot=0; //variable pour récupérer la tension aux bornes du potentiomètre traduitepar le CAN . On l’initialise à 0.

int valJoystickY=0;
int valJoystickX=0;

int BTN = 3;
int BTN2 = 4;

int value;
int value2;

int LED = 13;
int LED2 = 12;
void setup() {
 Serial.begin(9600); //Initialisation de la communication avec la console
}
void loop() {
  pinMode(BTN, INPUT);
  pinMode(BTN2, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(LED2, OUTPUT);
  //potentiomètre
 valPot=analogRead(A0); //lit la tension, la convertit en valeur numérique et la stockedans valeurPot
 Serial.print("Valeurs... pot.: ");
 Serial.println(valPot);
 
  //Joystick
 valJoystickX=analogRead(A1);
 valJoystickY=analogRead(A2);
 Serial.print("Joystick X:");
 Serial.println(valJoystickX);
 Serial.print("Joystick Y:");
 Serial.println(valJoystickY);
 
 //led
  value = digitalRead(BTN);
  if (value == HIGH) {
	digitalWrite(LED, HIGH);
  } else {
	digitalWrite(LED, LOW);
  }

  value2 = digitalRead(BTN2);
  if (value2 == HIGH) {
	digitalWrite(LED2, HIGH);
  } else {
	digitalWrite(LED2, LOW);
  }
}
```

- [Lien TinkerCad](https://www.tinkercad.com/things/hjQVV0tQ3M0-arduino-tp2-entrees) 
---

### Note du [[../Daily 📆/2024-02-21|2024-02-21]]
#### Dépôt
- ![[../_Assets 💼/Dépôt TP3 Arduino.pdf|Dépôt TP3 Arduino]] 
#### => Les Moteurs
###### Moteur Servo
- Code entre 150 et 90 degrés

	```C
	#include <Servo.h>
	Servo myservo;
	
	void setup() {
	  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
	}
	
	void loop() {
	  myservo.write(150);
	  delay(1000);
	  myservo.write(90);
	  delay(1000);
	}
	```

##### Moteur "stepper"
- code +/- clockwise
	```c
	#include <Stepper.h>
	
	const int stepsPerRevolution = 200;  
	
	Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
	
	void setup() {
	  // set the speed at 60 rpm:
	  myStepper.setSpeed(60);
	  // initialize the serial port:
	  Serial.begin(9600);
	}
	
	void loop() {
	  // step one revolution  in one direction:
	  Serial.println("clockwise");
	  myStepper.step(stepsPerRevolution);
	  delay(500);
	  // step one revolution in the other direction:
	  Serial.println("counterclockwise");
	  myStepper.step(-stepsPerRevolution);
	  delay(500);
	}
	```

##### Moteur DC
- code +/- clockwise + *circuit* en H
	```c
	const int IN1_PIN = 6; // le pin Arduino connecté au pin IN1 de L298N
	const int IN2_PIN = 5; // le pin Arduino connecté au pin IN2 de L298N
	
	void setup() {
	  pinMode(IN1_PIN, OUTPUT);
	  pinMode(IN2_PIN, OUTPUT);
	}
	
	void loop() {
	  clockwiseRotation();
	  delay(1000); // Attendre 1 seconde entre les rotations
	  counterclockwiseRotation();
	  delay(1000);
	}
	
	void clockwiseRotation() {
	  analogWrite(IN1_PIN, 100);
	  analogWrite(IN2_PIN, 0);
	  delay(1000); // Rotation à vitesse maximale pendant 1 seconde
	}
	
	void counterclockwiseRotation() {
	  analogWrite(IN1_PIN, 0);
	  analogWrite(IN2_PIN, 255);
	  delay(1000); // Rotation à vitesse maximale dans le sens antihoraire pendant 1 seconde
	}
	```

---

### Note du [[../Daily 📆/2024-02-28|2024-02-28]] 
#### Dépôt
- ![[../_Assets 💼/Dépôt TP4 Arduino.pdf]]

#### => Les Capteurs
##### Capteurs à bille
```c
#define SHOCK_PIN 2
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);       // on-board LED, usually pin 13
  pinMode(SHOCK_PIN, INPUT);          // shock sensor pin set to input
}

void loop() {
  if (digitalRead(SHOCK_PIN)) {       // shock detected?
    // shock detected with pull-down resistor
    digitalWrite(LED_BUILTIN, HIGH);  // switch LED on
    delay(2000);                      // leave LED on for period
  }
  else {
    // shock not detected with pull-down resistor
    digitalWrite(LED_BUILTIN, LOW);   // switch LED off
  }
}
```

##### Capteurs relai
```c
int relayPin = 2; // broche utilisée pour contrôler le relais

void setup() {
  pinMode(relayPin, OUTPUT); // définit la broche du relais en sortie
}

void loop() {
  digitalWrite(relayPin, HIGH); // allume le relais
  delay(1000); // attend 1 seconde
  digitalWrite(relayPin, LOW); // éteint le relais
  delay(1000); // attend 1 seconde
}
```

##### Capteurs à lumière
```c
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // reads the input on analog pin A0 (value between 0 and 1023)
  int analogValue = analogRead(A0);

  Serial.print("Analog reading: ");
  Serial.print(analogValue);   // the raw analog reading

  // We'll have a few threshholds, qualitatively determined
  if (analogValue < 10) {
    Serial.println(" - Dark");
  } else if (analogValue < 200) {
    Serial.println(" - Dim");
  } else if (analogValue < 500) {
    Serial.println(" - Light");
  } else if (analogValue < 800) {
    Serial.println(" - Bright");
  } else {
    Serial.println(" - Very bright");
  }

  int x = analogValue*(0,5);
  Serial.println(x);
  analogWrite(LED_BUILTIN, x);
  delay(500);
}
```

##### Capteurs à ultrason
```c
// Définition des numéros de port
const int trigPin = 3; // Trigger (émission)
const int echoPin = 2; // Echo (réception)

// Variables utiles
long duree; // Durée de l'echo
int distance;

void setup() {
    pinMode(trigPin, OUTPUT); // Configuration du port du Trigger comme une SORTIE
    pinMode(echoPin, INPUT); // Configuration du port de l'Echo comme une ENTREE
    Serial.begin(9600) ; // Démarrage de la communication série à 9600 bits/s
}

void loop() {
    // Émission d'un signal de durée 10 microsecondes
    digitalWrite(trigPin, LOW);
    delayMicroseconds(5);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Écoute de l'écho
    duree = pulseIn(echoPin, HIGH);
    // Calcul de la distance
    distance = duree*0.034/2;
    // Affichage de la distance dans le Moniteur Série
    Serial.print("Distance en cm :") ;
    Serial.println(distance) ;
    delay(500); // Délai d'attente pour éviter d'afficher trop de résultats à la seconde
}
```

##### Capteurs infrarouge
```c
#include <IRremote.h>
const char recepteurIR = 2;

IRrecv monIR(recepteurIR);
decode_results message;

void setup()
{
 Serial.begin(9600);
 monIR.enableIRIn();
}

void loop()
{
  if(monIR.decode(&message) == "FFFFFFFF")
  {
    Serial.println("Noise");
  }
  if (monIR.decode(&message))
  {
    Serial.println(message.value,HEX);
    delay(500);
    monIR.resume();
  }
  delay(1);
}
```

---

### Note du [[2024-03-13]]
- ![[Arduino Rapport Examen]]
---
