int APin = 0;
float celsius;

void setup() {
  Serial.begin(9600);
}

void loop() {
  float rawVoltage = analogRead(APin);
  float millivolts = (rawVoltage/1024)*5000;
  celsius = millivolts/10;
  
  Serial.println(celsius);
  Serial.print("Degree Celsius \n");
  Serial.print((celsius*9)/5 +32);
  Serial.print("degree Farenheit\n");
  delay(3000);
}
