/*
 * SD Card Write Functions 
 */
void SD_setup()
{
  if (!SD.begin(10)) {
    //led blink... 
    while (true);
  }
}

void sendSDData(Data data)
{
  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  if (dataFile) {
    dataFile.print(data.car_x);
    dataFile.print(",");
    dataFile.print(data.car_y);
    dataFile.print(",");
    dataFile.print(data.obj_x);
    dataFile.print(",");
    dataFile.print(data.obj_y);
    dataFile.print(",");
    dataFile.println(data.dir);
    dataFile.close();
  }
}
 
