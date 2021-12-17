int analogIn= A0;
int analogOut = 11;

int sensorValue = 0;
int outputValue = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogIn);
  outputValue = map(sensorValue,0,1023,0,255);
  
  analogWrite(analogOut,outputValue);
  
  Serial.println(sensorValue);
  Serial.println(outputValue);
  
  delay(2);
}
