int myLEDpin = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(myLEDpin, HIGH);
  delay(1000);
  digitalWrite(myLEDpin, LOW);
  delay(1000);
}
