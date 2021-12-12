int callibration = 30;
long unsigned int lowIN, pause = 5000;
boolean lockLOW = true, takeLOWTime;
const int pirPIN = 9, ledPIN = 13;

void setup() {
  Serial.begin(9600);
  pinMode(pirPIN, INPUT);
  pinMode(ledPIN, OUTPUT);
  digitalWrite(pirPIN, LOW);

  Serial.print("Callibrating sensor");

  for (int i=0; i<callibration; i++) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("Done");
  Serial.println("Sensor active");
  delay(50);
}

void loop() {
  if (digitalRead(pirPIN) == HIGH) {
    digitalWrite(ledPIN, HIGH);

    if (lockLOW) {
      lockLOW = false;
      Serial.println("-----");
      Serial.print("Motion detectd at ");
      Serial.println(millis()/1000);
      Serial.println(" secs");
      delay(50);
    }
    
    takeLOWTime = true;
  }

  if (digitalRead(pirPIN) == LOW) {
    digitalWrite(ledPIN, LOW);

    if (takeLOWTime) {
      lowIN = millis();
      takeLOWTime = false;
    }
    
    if (!lockLOW && millis()-lowIN > pause) {
      lockLOW = true;
      Serial.print("Motion detected at ");
      Serial.print((millis()-pause)/1000);
      Serial.println(" sec");
      delay(50);
    }
  }
}
