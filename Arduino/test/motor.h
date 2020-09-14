#ifndef motor_H
#define  motor_H

#include "Arduino.h" 


/*
 * Car Class Definition 
 */
class Car
{
  public: 
    Car(const uint8_t ENA, const uint8_t ENB, const uint8_t IN1, const uint8_t IN2, const uint8_t IN3, const uint8_t IN4, int velocity);
    
    void set_up();
     
    //Movement
    void forward();
    void backward();
    void right();
    void left();
    void halt();
    
  private: 
    uint8_t ENA;
    uint8_t ENB;
    uint8_t IN1;
    uint8_t IN2;
    uint8_t IN3;
    uint8_t IN4;
    int velocity;
};

#endif
