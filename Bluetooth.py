import serial
import time
import sys
import signal

COM=input("Enter the COM Port\n")
BAUD=input("Enter the Baudrate\n")
SerialPort = serial.Serial(COM,BAUD,timeout=1)
time.sleep(0.2)
SerialPort.write("I")

def signal_handler(signal, frame):
	print("closing program")
	SerialPort.close()
	sys.exit(0)

def getData():
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
			#print((IncomingData).decode('utf-8'))
			val = IncomingData.decode('utf-8')
			if ',' in val:
				return_list = val.split(',')
			elif isinstance(val, list):
				return_list = val
			else:
				print("NOTE: return val is either not a string or not a list. May cause error")
				return_list = val
			return return_list
		time.sleep(0.01)