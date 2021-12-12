int light_sensitivity = 400;
int digiOut = 11;

void setup() {
  Serial.begin(9600);
  pinMode(digiOut, OUTPUT);
}

void loop() {
  int LDRValue = analogRead(A0);
  
  Serial.println(LDRValue);
  delay(50);
  
  if( LDRValue < light_sensitivity )
   digitalWrite(digiOut, HIGH);
  else
   digitalWrite(digiOut, LOW);

  delay(1000);
}
