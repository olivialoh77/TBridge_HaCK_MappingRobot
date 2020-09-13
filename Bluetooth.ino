#include <SoftwareSerial.h>
float var = 30.00;
float inc = 5;
char Incoming_value = 0;    

//SoftwareSerial mySerial(3, 4);//Variable for storing Incoming_value


void setup() 
{
  
  Serial.begin(9600);         //Sets the data rate in bits per second (baud) for serial data transmission
  //pinMode(2, OUTPUT);        //Sets digital pin 13 as output pin
  //while(!Serial){;}
  //mySerial.begin(38400);
  //myStepper.setSpeed(60);
  Serial.println("Hello, world?");
}
void loop()
{
  /*while(mySerial.available())  
  {
    mySerial.write();
  }*/


  if(Serial.available() > 0) 
  {
    
    var+= inc;
    
    char cmd = Serial.read(); 
    if (cmd == 's')
    {
      Serial.println(var);
      delay(100);
    }

    if(var >=50 || var <=30)
    {
      inc = -inc;
    }
  }
}
