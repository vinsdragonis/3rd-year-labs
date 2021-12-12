int char_ = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  char_ = Serial.read();
  Serial.print("Received: ");
  Serial.print(char_);
}
