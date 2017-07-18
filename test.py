import serial
import sys
import requests
import OpenSSL.SSL
from OpenSSL.SSL import ZeroReturnError

ser = serial.Serial(
	port = "/dev/ttyUSB0",
	baudrate=57600, 
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS)

#char= ser.read(size=1)
failure = 0

def sendRequest():
	char= ser.read(size=1)
	while char != "R":
		char = ser.read(size=1)
		r = requests.get("https://sqs.us-east-2.amazonaws.com/189794443393/InternQueue?Action=SendMessage&MessageBody="+str(char))

	while True:
		ch= ser.read(size=20)
		r = requests.get("https://sqs.us-east-2.amazonaws.com/189794443393/InternQueue?Action=SendMessage&MessageBody="+str(ch))
		print ch	
while failure < 10:
	try:
		sendRequest()
	except OpenSSL.SSL.ZeroReturnError:
		failure +=1 
