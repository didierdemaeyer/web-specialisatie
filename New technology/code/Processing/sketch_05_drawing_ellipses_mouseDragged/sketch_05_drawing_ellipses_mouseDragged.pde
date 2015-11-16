int[] arrX = new int[100];
int[] arrY = new int[100];

int counter = 0;

void setup() {
 size(500, 500);
}

void draw () {
 background(0, 100, 0);
 
 noStroke();
 fill(255, 0, 0);
 
 for (int i = 0; i < arrX.length; i++) {
   ellipse(arrX[i], arrY[i], 10, 10);
 }
}

void mouseDragged() {
  if (counter == 99) {
    counter = 0;
  }
  
  arrX[counter] = mouseX;
  arrY[counter] = mouseY;
  counter++;
}