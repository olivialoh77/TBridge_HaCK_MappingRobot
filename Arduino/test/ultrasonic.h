#ifndef ultrasonic_H
#define  ultrasonic_H

#include "Arduino.h" 


/*
 * Ultrasonic Class Definition 
 */
class Ultrasonic
{
  public: 
    Ultrasonic(const uint8_t trigPin, const uint8_t echoPin);
    
    void set_up();
    float findDistance();
    
  private: 
    uint8_t trigPin;
    uint8_t echoPin;
    
    long duration;
};

#endif

