//./say_time.py /dev/tty.usbmodem1421 9600


const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int ledPin =  13;      // the number of the LED pin



void setup() {
  
  Serial.begin(9600);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);  
}

void loop() {

if(digitalRead(buttonPin1) == LOW)
{
digitalWrite(13,HIGH);  
Serial.write("say\n");
delay(1000);
}
else if(digitalRead(buttonPin2) == LOW) 
{
digitalWrite(13,HIGH);
Serial.write("time\n");
delay(1000);
}

else
digitalWrite(13,LOW);
}
