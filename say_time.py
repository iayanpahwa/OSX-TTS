#!/usr/bin/python

import serial
from sys import argv
from os import system
from time import sleep

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
