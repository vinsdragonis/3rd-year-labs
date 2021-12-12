int pin1 = 13;
int pin2 = 12;
int pin3 = 11;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin1, HIGH);
  pinMode(pin2, LOW);
  pinMode(pin3, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin1, LOW);
  delay(1000);
  
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, HIGH);
  delay(1000);

  digitalWrite(pin2, LOW);
  digitalWrite(pin3, HIGH);
  delay(1000);

  digitalWrite(pin3, LOW);
  digitalWrite(pin1, HIGH);
}
