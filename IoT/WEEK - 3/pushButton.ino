int pinOp = 13;
int pinIp = 2;
int val = 0;

void setup() {
  pinMode(pinIp, INPUT);
  pinMode(pinOp, OUTPUT);
}

void loop() {
  val = digitalRead(pinIp);
  digitalWrite(pinOp, LOW);
  
  if (val == 0)
    digitalWrite(pinOp, LOW);
  else
    digitalWrite(pinOp, HIGH);
}
