###### TEXT TO SPEECH on MAC OSX EL CAPITAN ####
Author: Ayan Pahwa


Interacting with MAC OSX Terminal using Arduino and python over Serial (Text-To-Speech)

Load Arduino sketch, Connect pushbuttons 
Run python code with sudo permissions and arduino board serial port and baud rate as CLI arguments

To run sudo python say_time.py serial port baud rate
ex: python say_time.py /dev/tty.usbmodem1421 9600

On pressing button a BASH process is created which yell out speech from text
for eg: Saying date using command "date | say"

NOTE: say is OSX CLI utility for TTS
