#include <String.h>
#include <Wire.h>
#include <hd44780.h>                       // main hd44780 header
#include <hd44780ioClass/hd44780_I2Cexp.h> // i2c expander i/o class header

hd44780_I2Cexp lcd; 

const int LCD_COLS = 20;
const int LCD_ROWS = 4;

String InBytes;
String label;
String price;
int totalPrice;

void setup()
{
  Serial.begin(9600);
  int status;
  status = lcd.begin(LCD_COLS, LCD_ROWS);
  if(status) // non zero status means it was unsuccesful
  {
    hd44780::fatalError(status); // does not return
  }
  // initalization was successful, the backlight should be on now
  lcd.print("AI CASHIER");
}

void loop() {
  if(Serial.available()>0) {
    label = Serial.readStringUntil(' ');
    if(label != ""){
      price = Serial.readStringUntil('\n');
      if(price == "reset") {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Item: -");
        lcd.setCursor(0, 1);
        lcd.print("Total: 0"); // ending message can be changed
        totalPrice = 0;
      }
      else {
        totalPrice += price.toInt();
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Item: " + label);
        lcd.setCursor(0, 1);
        lcd.print("Total: " + String(totalPrice));
      }
    }
  
  }
}
