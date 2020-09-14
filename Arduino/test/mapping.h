#ifndef mapping_H
#define  mapping_H

#include "Arduino.h" 

#define left_to_right 1 
#define top_to_bottom 2 
#define right_to_left 3 
#define bottom_to_top 4 

/*
 * Data Class Definition 
 */
class Data 
{
  public: 
    Data();

    float car_x;
    float car_y;
    float obj_x;
    float obj_y;

    int dir;
};

/*
 * Mapping Calculation Function 
 */
Data calculateData(int dir, float c_dist,float s_dist, float MAX_X, float MAX_Y);

#endif
