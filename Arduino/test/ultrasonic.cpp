#include "ultrasonic.h"
#include "Arduino.h"

/*
 * Ultrasonic Class Initialization/Setup 
 */

Ultrasonic::Ultrasonic(const uint8_t trigPin, const uint8_t echoPin)
{
      this->trigPin = trigPin;
      this->echoPin = echoPin;
}

void Ultrasonic::set_up()
{
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

/*
 * Ultrasonic Class Functions 
 */

float Ultrasonic::findDistance()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2000);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);

  float pingTime = pulseIn(echoPin, HIGH);
  pingTime = pingTime / 1000000;
  pingTime = pingTime / 3600;

  float targetDistance = 776.5 * pingTime;
  targetDistance = targetDistance / 2;
  targetDistance = targetDistance * 63360;

  return targetDistance;
}

