int buttonPin = 2;
const int ledPins[] = {3, 4, 5, 6, 7, 8, 9, 10}; 
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);
const int Ledpinsmode[] = {13, 12, 11};
int LedAct = 0;
int mode = 0;
unsigned long TempsPressionButton = 0;
const unsigned long AppuiLong = 1000; // Déclaration de la variable AppuiLong
boolean BoutonPresser = false;
boolean ModeSelec = false;
int SelecduMode = 0;
const int buzzerPin = A1; // Définir la broche du buzzer
int LedActLast = 0; // Ajouter cette variable globale
boolean mode2Paused = false; // Ajouter cette variable globale
boolean mode2LastLedSet = false; // Ajouter cette variable globale
int mode2LastLedIndex = 0; // Ajouter cette variable globale

const int analogPin = A2;
const float minVoltage = 3.3;
int alert_times = 3;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
  for (int i = 0; i < 3; i++) {
    pinMode(Ledpinsmode[i], OUTPUT);
    digitalWrite(Ledpinsmode[i], LOW);
  }
  pinMode(buzzerPin, OUTPUT); // Définir la broche du buzzer en mode sortie

  tone(buzzerPin,200);
  delay(100); // Délai pour la durée de la tonalité
  noTone(buzzerPin);
  delay(1000); // Délai pour la durée de la tonalité

  CheckBattery();
  updateModeLEDs();
}



void loop() {
  int EtatBoutton = digitalRead(buttonPin);

  // Gestion de l'appui sur le bouton
  if (EtatBoutton == LOW) {
    if (!BoutonPresser) {
      BoutonPresser = true;
      TempsPressionButton = millis();
      LedActLast = LedAct; // Sauvegarder l'index de la dernière LED allumée
    }
    if (millis() - TempsPressionButton > AppuiLong && !ModeSelec) {
      ModeSelec = true;
      TempsPressionButton = millis(); // Réinitialiser le temps pour la sélection de mode
      SelecduMode = 0; // Réinitialiser le mode sélectionné
    }
  } else if (BoutonPresser) {
    BoutonPresser = false;
    if (!ModeSelec) {
      if (mode == 1) { // Si le mode est 2 (allumage progressif)
        if (!mode2Paused) { // Si le mode 2 est en pause
          mode2Paused = true; // Reprendre le mode 2
        } else {
          mode2Paused = false;
        }
      } 
    // Pour les autres modes
      // Appui court - changer de LED en mode 1 ou sélectionner le mode
      if (mode == 0) { // Mode 1
        digitalWrite(ledPins[LedAct], LOW);
        LedAct = (LedAct + 1) % numLeds;
        digitalWrite(ledPins[LedAct], HIGH);
      } else { // Sélectionner le mode
        mode = SelecduMode;
        executeMode();
        // Activer le buzzer lors du changement de mode
        tone(buzzerPin,200);
        delay(100); // Délai pour la durée de la tonalité
        noTone(buzzerPin);
        delay(100);
      
      }
    } else {
      // Relâchement après un appui long - sélectionner le mode
      ModeSelec = false;
      mode = SelecduMode;
      executeMode();
    }
  }

  // Si le mode est 1 et que le bouton est pressé (appui court), passer au mode 1
  if (mode == 1 && !ModeSelec && EtatBoutton == LOW && millis() - TempsPressionButton < AppuiLong) {
    //mode = 0;
    digitalWrite(ledPins[LedAct], LOW); // Éteindre la LED actuelle
    if (mode2LastLedSet) {
      LedAct = mode2LastLedIndex; // Reprendre l'index de la dernière LED allumée du mode 2
    }
    digitalWrite(ledPins[LedAct], HIGH); // Allumer la LED
    // Réinitialiser le mode 2
    mode2Paused = false;
    mode2LastLedSet = false; // Réinitialiser le mode 2 Last Led Set
  }

  // Gestion de la sélection de mode
  if (ModeSelec) {
    unsigned long currentMillis = millis();
    if (currentMillis - TempsPressionButton >= 350) {
      TempsPressionButton = currentMillis;   
      SelecduMode = (SelecduMode + 1) % 4; // Passer au mode suivant
      updateModeLEDs(); // Mettre à jour les LEDs pour afficher le mode sélectionné
      // Activer le buzzer lors du changement de mode
      tone(buzzerPin,200);
      delay(100); // Délai pour la durée de la tonalité
      noTone(buzzerPin);
      delay(100);
    }
  }

  // // Mode d'opération
  // if (!ModeSelec && mode != 1) { // Ne pas exécuter le mode 2 si mode2Paused est true
  //   executeMode();
  // }


}

void executeMode() {
  switch (mode) {
    case 0:
      // Le mode 0 est géré directement dans le loop lors de l'appui sur le bouton
      digitalWrite(11, LOW);
      digitalWrite(12,HIGH);
      digitalWrite(13, HIGH);
      break;
    case 1: // Mode 2 dans votre code d'origine - Allumage progressif
      digitalWrite(11, HIGH);
      digitalWrite(12,LOW);
      digitalWrite(13, HIGH);
      if (!mode2Paused) { // Si le mode 2 n'est pas en pause
        for (int i = 0; i < numLeds; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(500);
          if (digitalRead(buttonPin) == LOW) { // Si le bouton est pressé
            while (digitalRead(buttonPin) == LOW); // Attendre qu'il soit relâché
            mode2LastLedIndex = i; // Enregistrer l'index de la LED actuelle
            mode2LastLedSet = true; // Marquer que la dernière LED a été définie pour le mode 2
            mode2Paused = true; // Mettre le mode 2 en pause
            break; // Sortir de la boucle for
          }
          digitalWrite(ledPins[i], LOW);
          if (i == numLeds - 1) {
            // Si c'est la dernière LED, recommencer à partir de la première
            i = -1;
          }
        }
      }
      break;
    case 2: // Mode 3 dans votre code d'origine - Allumage continu
      digitalWrite(11, HIGH);
      digitalWrite(12,HIGH);
      digitalWrite(13, LOW);
      for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], HIGH);
      }
      delay(100); // Délai court pour voir l'effet
      for (int i = 0; i < numLeds; i++) {
        digitalWrite(ledPins[i], LOW);
      }
      break;
      case 3: // Nouveau cas - Description du cas
        // Code spécifique au cas 3
        // Allumage continu des LED pendant un certain temps
        digitalWrite(11, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(13, LOW);
        for (int i = 0; i < numLeds; i++) {
          digitalWrite(ledPins[i], HIGH);
        }
        delay(100); // Délai court pour voir l'effet
        for (int i = 0; i < numLeds; i++) {
          digitalWrite(ledPins[i], LOW);
      }
      break;

  }
}

void updateModeLEDs() {
  if (SelecduMode == 0){
    digitalWrite(11, LOW);
    digitalWrite(12,HIGH);
    digitalWrite(13, HIGH);
  }
  if (SelecduMode == 1){
    digitalWrite(11, HIGH);
    digitalWrite(12,LOW);
    digitalWrite(13, HIGH);
  }
  if (SelecduMode == 2){
    digitalWrite(11, HIGH);
    digitalWrite(12,HIGH);
    digitalWrite(13, LOW);
  }
  if (SelecduMode == 3){
    digitalWrite(11, LOW);
    digitalWrite(12,LOW);
    digitalWrite(13, HIGH);
  }
}


void CheckBattery() {  
  int sensorValue = analogRead(analogPin); // Lit la valeur de l'entrée analogique
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.println(voltage*2);
  if (voltage*2 < minVoltage) {
    for (int i = 0; i < alert_times; i++) {
      tone(buzzerPin,200);
      delay(500); // Délai pour la durée de la tonalité
      noTone(buzzerPin);
      delay(300); // Délai pour la durée de la tonalité
    }
  }
}