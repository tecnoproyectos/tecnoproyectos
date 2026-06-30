function setup() {
  // Crear canvas ancho x alto
  createCanvas(400, 600);
}

function draw() {
  background(220);

  fill(255, 100, 50); // naranja en RGB
  noStroke();         // sin borde
  // Elipse con dos radios iguales = círculo
  ellipse(300, 200, 100, 100);
}