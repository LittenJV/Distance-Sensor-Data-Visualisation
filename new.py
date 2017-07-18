import serial
import sys
import requests
from requests_futures.sessions import FuturesSession

ser = serial.Serial(
	port = "/dev/ttyUSB0",
	baudrate = 57600,
	parity = serial.PARITY_ODD,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS)

session = FuturesSession(max_workers=10)
def readData():
	data = b""
	while True:
		char = ser.read(size=1)		
		if char == b"R":
			for c in data:
				if c == 195 or c == 13:
					data = data[:-1]
					print (data)
			r = session.get("https://sqs.us-east-2.amazonaws.com/189794443393/InternQueue?Action=SendMessage&MessageBody="+str(data))
			data = b""
		else:
			data += char

readData()
