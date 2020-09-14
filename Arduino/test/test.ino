#include "motor.h" 
#include "ultrasonic.h" 
#include "mapping.h"
#include <SPI.h>
#include <SD.h>

/*
 * Pin Definitions 
 */
//Define the pins used to control the H bridge 
#define ENA A1
#define ENB A0
#define IN1 13
#define IN2 12
#define IN3 11
#define IN4 10

//Ultrasonic Sensors
#define trigPin_c 9
#define echoPin_c 8

#define trigPin_s 7
#define echoPin_s 6

/*
 * Definitions 
 */
//Arena Size 
#define ARENA_X 29
#define ARENA_Y 31

//Mapping Specifications 
#define turn_distance 1.0 //(in meters)
#define turn_time 5000 //(in millisecs)

//Bluetooth On or Off? 
//Bluetooth Instructions: REMEMBER WHEN UPLOADING CODE TO UNPLUG PINS 0 & 1 (TX/RX) AND PLUG THEM BACK IN AFTER THE UPLOAD  
#define BLUETOOTH_ON false

//SD Card On or Off?  (When both off, default just prints plot points to serial monitor) 
#define SD_CARD_ON false 

//Car speed 
int carspeed = 200;
int state = 0; 

/*
 * Initializations
 */
Car mycar = Car(ENA, ENB, IN1, IN2, IN3, IN4, carspeed); 

Ultrasonic car_ult = Ultrasonic(trigPin_c, echoPin_c);
Ultrasonic obj_ult = Ultrasonic(trigPin_s, echoPin_s);

File myFile;
/*
 *  Robot Code 
 */
 
void setup() 
{
  // Define the pins controlling the motors are outputs
  //mycar.set_up();

  //Ultrasonic Sensor Setup 
  car_ult.set_up();
  obj_ult.set_up();
  
  //Begin serial communication (When Bluetooth is on, CANNOT open Serial Monitor) 
  Serial.begin(9600);

}


void loop() 
{
  // Read value from serial monitor

  
  mycar.forward();

  float c_dist = car_ult.findDistance();
  float s_dist = obj_ult.findDistance();

  //Serial.println(c_dist);
  Data data = calculateData(state, c_dist, s_dist, ARENA_X, ARENA_Y);

  if(BLUETOOTH_ON)
  {
    sendBluetoothData(data);
  }
  else if(SD_CARD_ON)
  {
    sendSDData(data); 
  }
  else
  {
    formatGraphData(data);
  }

  if(c_dist < turn_distance) //car is approaching wall, ready to turn 
  {
    changeState();
    mycar.right(); //turn 
  }

  delay(100);
}


