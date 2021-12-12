int sensorpin = A0;
int sensorvalue = 0;
int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  sensorvalue = analogRead(sensorpin);
  Serial.println(sensorvalue);
  
  if (sensorvalue < 100) {
    Serial.println("Fire detected");
    digitalWrite(led, HIGH);
    delay(1000);
  }
  
  digitalWrite(led, LOW);
}
