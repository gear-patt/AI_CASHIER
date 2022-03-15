#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);   //Module IIC/I2C Interface บางรุ่นอาจจะใช้ 0x3f
void setup(){
  lcd.begin();
  //lcd.noBacklight();   // ปิด backlight
  lcd.backlight();      // เปิด backlight 
  lcd.home();
  lcd.print("hello world");
  lcd.setCursor(0, 1);
  lcd.print("Steven is gay!");
}

void loop() {
  
}
