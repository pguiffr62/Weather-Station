import processing.serial.*;
Serial myPort = new Serial(this, Serial.list()[2], 9600);
int myInt;
int myNum;
float xo;
float yo;
float angle = 0;

void setup() {
  size(500, 500);
  ellipseMode(RADIUS);
  xo = width/2;
  yo = height/2;
  println("Available serial ports:");
  println(Serial.list());
}
void draw() {
 // println("working?");
  if (myPort.available() > 0) {
    myInt = myPort.read();
    println(myInt);
    if (myInt > 0) {
      angle = radians(myInt);
      background(255, 255, 255);
      fill(0, 0, 225);
      ellipse(250, 250, 100, 100);
      xo = cos(angle)*100  + 250; //makes x coordinate of end of line
      yo = 250-sin(angle)*100; //makes y coordinate of end of line
      line(250, 250, xo, yo);
    }
  }
}
