/*
 * Miscellaneous Mapping Functions 
 */
void changeState()
{
  if(state < 4) 
    state++;
  else 
    state = 1;
}


void formatGraphData(Data data)
{
  Serial.print("(");
  Serial.print(data.car_x);
  Serial.print(",");
  Serial.print(data.car_y);
  Serial.println(")");
  Serial.print("(");
  Serial.print(data.obj_x);
  Serial.print(",");
  Serial.print(data.obj_y);
  Serial.println(")");
}


