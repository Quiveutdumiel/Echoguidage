int ledPin = 13;                // choose the pin for the LED
int inputPin = 3;               // Connect sensor to input pin 3 

#include <Wire.h>
#include <VL6180X.h>
VL6180X sensor;
#define RAD_TO_DEG  57.295779513082320876798154814105
//Analog read pins
const unsigned char xPin = A0;
const unsigned char yPin = A1;
const unsigned char zPin = A2;
float xRead = 0;
float yRead = 0;
float zRead = 0;
const unsigned char xPin1 = A3;
const unsigned char yPin1 = A4;
const unsigned char zPin1 = A5;
float xRead1 = 0;
float yRead1 = 0;
float zRead1 = 0;

//The minimum and maximum values that came from
//the accelerometer while standing still
float xminVal = 200;
float xmaxVal = 300;
float yminVal = 205;
float ymaxVal = 307;
float zminVal = 205;
float zmaxVal = 306;
float xAng = 0;
float yAng = 0;
float zAng = 0;
float FTX=0;
float FTY=0;
float FTZ=0;
float a=0.3;
float xminVal1 = 200;
float xmaxVal1 = 300;
float yminVal1 = 205;
float ymaxVal1 = 307;
float zminVal1 = 205;
float zmaxVal1 = 306;
float xAng1 = 0;
float yAng1 = 0;
float zAng1 = 0;
float FTX1=0;
float FTY1=0;
float FTZ1=0;
float a1=0.3;

//calibration
float calibX=0;
float calibY=14.00;
float calibZ=-14.00;
float calibX1=0;
float calibY1=14.00;
float calibZ1=-20.00;

//to hold the caculated values
double x;
double y;
double z;
double x1;
double y1;
double z1;
//resultats
String resultat="";

//Acceleration
//void valueprint()
//{
// Serial.print(xRead);
// Serial.print('\t');
// Serial.print(yRead);
// Serial.print('\t');
// Serial.println(zRead);
// Serial.print(xRead1);
// Serial.print('\t');
// Serial.print(yRead1);
// Serial.print('\t');
// Serial.println(zRead1);
//}

float map_new(float x, float in_min, float in_max, float out_min, float out_max)
{
 return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void setup()
{
 FTX=analogRead(xPin);
 FTY=analogRead(yPin);
 FTZ=analogRead(zPin);
 FTX1=analogRead(xPin1);
 FTY1=analogRead(yPin1);
 FTZ1=analogRead(zPin1);

 Serial.begin(9600);
 Wire.begin();
 sensor.init();
 sensor.configureDefault();
 sensor.setTimeout(500);
}

void loop(){
 // ACCELEROMETRE  
 //read the analog values from the accelerometer
 xRead = analogRead(xPin);
 yRead = analogRead(yPin);
 zRead = analogRead(zPin);
 xRead=a*xRead+(1-a)*FTX;
 yRead=a*yRead+(1-a)*FTY;
 zRead=a*zRead+(1-a)*FTZ;
 FTX=xRead;
 FTY=yRead;
 FTZ=zRead;
 xRead1 = analogRead(xPin1);
 yRead1 = analogRead(yPin1);
 zRead1 = analogRead(zPin1);
 xRead1=a*xRead1+(1-a)*FTX1;
 yRead1=a*yRead1+(1-a)*FTY1;
 zRead1=a*zRead1+(1-a)*FTZ1;
 FTX1=xRead1;
 FTY1=yRead1;
 FTZ1=zRead1;
 
 //convert read values to degrees -90 to 90 - Needed for atan2
 xAng = map_new(xRead, xminVal, xmaxVal, -90, 90);
 yAng = map_new(yRead, yminVal, ymaxVal, -90, 90);
 zAng = map_new(zRead, zminVal, zmaxVal, -90, 90);
 xAng1 = map_new(xRead1, xminVal1, xmaxVal1, -90, 90);
 yAng1 = map_new(yRead1, yminVal1, ymaxVal1, -90, 90);
 zAng1 = map_new(zRead1, zminVal1, zmaxVal1, -90, 90);
 
 //Caculate 360deg values like so: atan2(-yAng, -zAng)
 //atan2 outputs the value of -π to π (radians)
 //We are then converting the radians to degrees
 x = RAD_TO_DEG * (atan2(-yAng, -zAng) + PI);
 y = RAD_TO_DEG * (atan2(-xAng, -zAng) + PI);
 z = RAD_TO_DEG * (atan2(-yAng, -xAng) + PI);
 x = RAD_TO_DEG * (atan2(-yAng1, -zAng1) + PI);
 y = RAD_TO_DEG * (atan2(-xAng1, -zAng1) + PI);
 z = RAD_TO_DEG * (atan2(-yAng1, -xAng1) + PI);

 //calibration
 int x[20],y[20],z[20],m[20],n[20],o[20],a,b,c,d,e,f;
  for (int i=0; i <= 14; i++) {
    x[i]=xAng;
    y[i]=yAng;
    z[i]=zAng;
    m[i]=xAng1;
    n[i]=yAng1;
    o[i]=zAng1;
    a=a+x[i];
    b=b+y[i];
    c=c+z[i];
    d=d+m[i];
    e=e+n[i];
    f=f+o[i];}
 xAng = a/20 + calibX;
 yAng = b/20 + calibY;
 zAng = c/20 + calibZ;
 xAng1 = d/20 + calibX1;
 yAng1 = e/20 + calibY1;
 zAng1 = f/20 + calibZ1;  

 // ACCELEROMETRE 1
 resultat=xAng;
 resultat=resultat+";";
 resultat=resultat+yAng;
 resultat=resultat+";";
 resultat=resultat+zAng;
 resultat=resultat+";";
 
 // ACCELEROMETRE 1
 resultat=resultat+xAng1;
 resultat=resultat+";";
 resultat=resultat+yAng1;
 resultat=resultat+";";
 resultat=resultat+zAng1;
 resultat=resultat+";";
 
 //DISTANCE
  int K[10],p;
  for (int i=0; i <= 9; i++) {
    K[i]=sensor.readRangeSingleMillimeters();
    p=p+K[i]; }//Serial.println(y/5);
  resultat=resultat+p/10+";";
  if (sensor.timeoutOccurred()) {
    Serial.print(" TIMEOUT"); }
    
  //BUTTON
  pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare pushbutton as input
  int val = digitalRead(inputPin);  // read input value
  if (val == HIGH) {            // check if the input is HIGH
    digitalWrite(ledPin, LOW);  // turn LED OFF
    resultat=resultat+"1;";
  } else {
    digitalWrite(ledPin, HIGH); // turn LED ON
    resultat=resultat+"0;";
  } 
  //int x, y, z;               //three axis acceleration data
  double roll = 0.00, pitch = 0.00;   //Roll & Pitch are the angles which rotate by the axis X and y 
  double x_Buff = float(xAng);
  double y_Buff = float(yAng);
  double z_Buff = float(zAng);
  roll = atan2(y_Buff , z_Buff) * 57.3;
  //pitch = atan2((- x_Buff) , sqrt(y_Buff * y_Buff + z_Buff * z_Buff)) * 57.3;
  
  //resultat=resultat=resultat+roll+";";
  Serial.println(resultat);
  resultat="";
  
  //delay(100);//just here to slow down the serial output - Easier to read
  Serial.flush(); 
}

