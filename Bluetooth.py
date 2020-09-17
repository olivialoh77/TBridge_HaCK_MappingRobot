import serial
import time
import sys
import signal

def signal_handler(signal, frame):
	print("closing program")
	SerialPort.close()
	sys.exit(0)

def getData():
	COM=input("Enter the COM Port\n")
	BAUD=input("Enter the Baudrate\n")
	SerialPort = serial.Serial(COM,BAUD,timeout=1)
	time.sleep(0.2)
	SerialPort.write("I")
	while (1):
		try:
			OutgoingData=input('> ')
			SerialPort.write(bytes(OutgoingData,'utf-8'))
		except KeyboardInterrupt:
			print("Closing and exiting the program")
			SerialPort.close()
			sys.exit(0)
		IncomingData=SerialPort.readline()
		if(IncomingData): # ASSUME INCOMING DATA IS A LIST OF 6 INDICES
			print((IncomingData).decode('utf-8'))
			return(IncomingData) # <---- DATA GOES HERE
		time.sleep(0.01)