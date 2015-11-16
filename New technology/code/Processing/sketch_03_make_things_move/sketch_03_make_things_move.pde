// Create an integer variable called i and store the value 0 in it:
int i = -15;

void setup() {
  // Create a 500 pixel by 500 pixel window:
  size(500, 500); 
}

void draw() {
  // Set the background to blue:
  background(0, 0, 100);

  // Set the fill to red:
  fill(255, 0, 0);

  // Draw a circle. Its y coordinate will be taken from the variable i:
  ellipse(250, i, 30, 30);

  // Update the variable i:
  if (i < height+15) { // if it's less than the height of the window:
    i = i + 2; // then add 1 to its value
  }
  else { // otherwise (if it's greater than or equal to the height of the window): 
    i = -15; // set it back to zero.
  }
}