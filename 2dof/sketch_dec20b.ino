#include <Servo.h>

Servo servoX, servoY;
int posX = 90, posY = 90;

void setup() {
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
  servoX.write(posX);
  servoY.write(posY);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    switch (command) {
      case 'w': posY = constrain(posY + 5, 0, 180); break;
      case 's': posY = constrain(posY - 5, 0, 180); break;
      case 'a': posX = constrain(posX - 5, 0, 180); break;
      case 'd': posX = constrain(posX + 5, 0, 180); break;
    }
    servoX.write(posX);
    servoY.write(posY);
  }
}
