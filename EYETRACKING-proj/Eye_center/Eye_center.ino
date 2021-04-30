//SERIAL_SERVO_ver01
//
#include<Servo.h>
#define numOfValsRec 2
#define digitsPerValRec 3

Servo servoLR;
Servo servoUD;

int valsRec[numOfValsRec];
int stringLength = numOfValsRec * digitsPerValRec + 1;
int counter = 0;
bool counterStart = false;
String receivedString;

void setup() {
  servoLR.attach(6);
  servoUD.attach(5);
  Serial.begin(9600);
  Serial.print("start ");
}

void receivedData()
{
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '$') {
      counterStart = true;
    }
    if (counterStart) {
      if (counter < stringLength) {
        receivedString = String(receivedString + c);
        counter++;
      }

      if (counter >= stringLength) {
        for (int i = 0; i < numOfValsRec; i++)
        {
          int num = (i * digitsPerValRec) + 1;
          valsRec[i] = receivedString.substring(num, num + digitsPerValRec).toInt();
        }
        receivedString = "";
        counter = 0;
        counterStart = false;
      }
    }
  }
}

void loop() {
  receivedData();
  servoLR.write(valsRec[0]);
  servoUD.write(valsRec[1]);
}
