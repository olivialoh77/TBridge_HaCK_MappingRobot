#include "mapping.h"
#include "Arduino.h"

/*
 * Data Class Initialization 
 */

Data::Data()
{ 
  car_x = 0;
  car_y = 0;
  obj_x = 0;
  obj_y = 0;
  dir = 1; 
}

/*
 * Mapping Calculation Function  
 */
Data calculateData(int dir, float c_dist, float s_dist, float MAX_X, float MAX_Y)
{
  float car_x; 
  float car_y; 

  float obj_x;
  float obj_y;

  switch(dir)
  {
    case(left_to_right): 
      car_x = MAX_X - c_dist; 
      car_y = 0; 
      obj_x = car_x; 
      obj_y = s_dist;
      break;
    case(top_to_bottom): 
      car_x = MAX_X;
      car_y = MAX_Y - c_dist; 
      obj_x = MAX_X - s_dist; 
      obj_y = car_y;
      break;
    case(right_to_left):
      car_x = c_dist; 
      car_y = MAX_Y;
      obj_x = car_x; 
      obj_y = MAX_Y - s_dist;
      break;
    case(bottom_to_top): 
      car_x = 0;
      car_y = c_dist; 
      obj_x = s_dist; 
      obj_y = car_y; 
      break; 
  }

  Data newline;

  newline.car_x = car_x; 
  newline.car_y = car_y;
  newline.obj_x = obj_x;
  newline.obj_y = obj_y; 

  newline.dir = dir; 
  return newline;
}


