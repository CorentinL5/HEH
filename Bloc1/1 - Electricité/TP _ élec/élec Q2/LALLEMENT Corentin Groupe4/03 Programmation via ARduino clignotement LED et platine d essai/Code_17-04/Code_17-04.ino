#include <LiquidCrystal.h>

#include <LiquidCrystal.h>

const int LCD_RS = 12;
const int LCD_EN = 11;
const int LCD_D4 = 5;
const int LCD_D5 = 4;
const int LCD_D6 = 3;
const int LCD_D7 = 2;

const int ANALOG_PIN = A0;

// Tamanho da matriz de LED
#define NUM_ROWS 8
#define NUM_COLS 8

bool leds[NUM_ROWS][NUM_COLS];

LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

void setup() {
  lcd.begin(16, 2);
  
  for (int row = 0; row < NUM_ROWS; row++) {
    for (int col = 0; col < NUM_COLS; col++) {
      leds[row][col] = false;
    }
  }
}

// Função principal
void loop() {
  int analogValue = analogRead(ANALOG_PIN);
  
  // Mapeia o valor para a escala de 0-100
  int brightness = map(analogValue, 250, 1023, 0, 100);
  
  // Atualiza a matriz de LED para exibir o valor numérico
  updateLEDs(brightness);
  
  // Exibe o valor numérico no display LCD
  displayLCD(brightness);
  
  // Aguarda um breve intervalo
  delay(100);
}

// Função para atualizar a matriz de LED para exibir o valor numérico
void updateLEDs(int brightness) {
  // Limpa a matriz de LED
  clearLEDs();
  
  // Calcula o número de LEDs acesos com base no brilho
  int numLEDs = map(brightness, 0, 100, 0, NUM_ROWS * NUM_COLS);
  
  // Atualiza a matriz de LED com base no número de LEDs acesos
  for (int i = 0; i < numLEDs; i++) {
    int row = i / NUM_COLS;
    int col = i % NUM_COLS;
    leds[row][col] = true;
  }
}

void clearLEDs() {
  for (int row = 0; row < NUM_ROWS; row++) {
    for (int col = 0; col < NUM_COLS; col++) {
      leds[row][col] = false;
    }
  }
}

// Função para exibir o valor numérico no display LCD
void displayLCD(int value) {
  lcd.setCursor(0, 0);
  lcd.print("Valor: ");
  lcd.print(value);
  lcd.print("m3/hora");
}