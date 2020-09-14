#include "motor.h"
#include "Arduino.h"

/*
 * Car Class Initialization/Setup 
 */
 
Car::Car(const uint8_t ENA, const uint8_t ENB, const uint8_t IN1, const uint8_t IN2, const uint8_t IN3, const uint8_t IN4, int velocity) 
{
      this->ENA = ENA;
      this->ENB = ENB;
      this->IN1 = IN1;
      this->IN2 = IN2;
      this->IN3 = IN3;
      this->IN4 = IN4;
      this->velocity = velocity;
}

void Car::set_up()
{
   pinMode(IN1,OUTPUT); 
   pinMode(IN2,OUTPUT);
   pinMode(IN3,OUTPUT); 
   pinMode(IN4,OUTPUT);
   pinMode(ENA,OUTPUT); 
   pinMode(ENB,OUTPUT);
}

/*
 * Car Class Functions 
 */
void Car::forward()
{
  analogWrite(ENA, velocity);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENB, velocity);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(1000);
}
void Car::backward()
{
  analogWrite(ENA, velocity);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(ENB, velocity);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(1000);
}
void Car::right()
{
  analogWrite(ENA, velocity);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENB, velocity);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(1000);
}
void Car::left()
{
  analogWrite(ENA, velocity);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(ENB, velocity);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(1000);
}
void Car::halt()
{
  analogWrite(ENA, LOW);
  analogWrite(ENB, LOW);
  delay(1000);
}
