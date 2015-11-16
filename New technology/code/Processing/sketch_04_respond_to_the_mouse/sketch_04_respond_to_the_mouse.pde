int x = 0;
int y = 0;

int x2 = 0;
int y2 = 0;

void setup() {
 size(500, 500);

 // Set the value of x to be half the width of the window
 x = width / 2;

 // Set the value of y to be half the height of the window
 y = height / 2;
}

void draw () {
 background(0, 100, 0);

 // Draw the circle in the position taken from the x and y variables:
 fill(255, 255, 255);
 ellipse(x, y, 50, 50);
 
 
 x2 = mouseX;
 y2 = mouseY;
 fill(255, 0, 0);
 ellipse(x2, y2, 20, 20);
}

void mousePressed() {
  // When the mouse is pressed, update x and y
  // to contain the current position of the mouse:
  x = mouseX;
  y = mouseY;
}