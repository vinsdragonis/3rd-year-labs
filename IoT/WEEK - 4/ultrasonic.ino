const int trigPin = 3; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 2; // Echo Pin of Ultrasonic Sensor

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600); // Starting Serial Terminal
}

void loop() {
   long duration, inches, cm;
   
   digitalWrite(trigPin, LOW);
   delayMicroseconds(2);
  
   digitalWrite(trigPin, HIGH);
   delayMicroseconds(10);
  
   digitalWrite(trigPin, LOW);
   duration = pulseIn(echoPin, HIGH);
  
   inches = microsecondsToInches(duration);
   cm = microsecondsToCentimeters(duration);
  
   Serial.print(inches);
   Serial.print("in, ");
   Serial.print(cm);
   Serial.print("cm");
   Serial.println();
  
   if(inches < 4)
    digitalWrite(13,HIGH);
   else
    digitalWrite(13, LOW);
  
   delay(1000);
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
