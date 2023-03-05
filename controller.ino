void setup(){
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(A0, INPUT);
}

void loop(){
  Serial.print("A'");
  Serial.print(digitalRead(2));
  Serial.print("'B'");
  Serial.print(digitalRead(3));
  Serial.print("'S'");
  Serial.print(map(analogRead(A0), 0, 1023, -32700, 32700));
  Serial.println("'");
  delay(1);
}