int x=0;
int y=0;
int z=0;
void setup() {
  
Serial.begin(115200);
}

void loop() {
  // Serial.print(count);
  // Serial.println(": PhucVy");
  // count++;
  x+=2;
  y+=3;
  z+=4;
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z);
  delay(1000);

}
