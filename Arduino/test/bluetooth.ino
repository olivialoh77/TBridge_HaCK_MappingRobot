/*
 * Bluetooth Functions
 */
//Sending data via TX/RX on Arduino Serial Communication 

void sendBluetoothData(Data data)
{
  if(Serial.available())
  {
    Serial.println(data.car_x);
    delay(10);

    Serial.println(data.car_y);
    delay(10);

    Serial.println(data.obj_x);
    delay(10);

    Serial.println(data.obj_y);
    delay(10);

    Serial.println(data.dir);
    delay(10);
  }
}

