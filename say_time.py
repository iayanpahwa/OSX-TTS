#!/usr/bin/python
#TO run 
# 1) chmod +x say_time.py
# 2) ./say_time.py /dev/tty.usbmodem1421 9600 ,change port accordingly

import serial
from sys import argv
from os import system
from time import sleep

#Supply com port and baud rate as arguments

com = argv[1]
baud = argv[2]

ser = serial.Serial(com, baud)
while True:
	command =  ser.readline()
	if command == "say\n":
		system("say -v Agnes hello guys whatsup")
		sleep(2)
	
	elif command == "time\n":
		system("say Ok let me tell you date and time")
		sleep(2)
		system("say Today is")
		system("date | say -v ALEX") 
