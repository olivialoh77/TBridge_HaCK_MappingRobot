import serial
import time
import sys
import signal
import graphing # for drawing after receiving each


def signal_handler(signal, frame):
	print("closing program")
	SerialPort.close()
	sys.exit(0)
'''
COM=input("Enter the COM Port\n")
BAUD=input("Enter the Baudrate\n")
SerialPort = serial.Serial(COM,BAUD,timeout=1)'''
#time.sleep(0.2)
#SerialPort.write("I")
#
def getData():
#while (1):
	'''try:
		OutgoingData=input('> ')
		SerialPort.write(bytes(OutgoingData,'utf-8'))
	except KeyboardInterrupt:
		print("Closing and exiting the program")
		SerialPort.close()
		sys.exit(0)
	IncomingData=SerialPort.readline()
	if(IncomingData):
		#print((IncomingData).decode('utf-8'))
		return(0,0,0,0)
	time.sleep(0.01)'''
	return(5,5,3,3) # some random number