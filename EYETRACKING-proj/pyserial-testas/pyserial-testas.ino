String userInput;

void setup() {
  Serial.begin(9600);
  Serial.print("OK ");

}

void loop() {
  if (Serial.available() > 0) {

    userInput = Serial.read();
    Serial.println(userInput);

  }
}
