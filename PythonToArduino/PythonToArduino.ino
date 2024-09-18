void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  while(Serial.available()==0)
  {

  }
  String data="";
  data=Serial.readStringUntil('\r');
  data.trim();
  if(data=="ON")
  {
    digitalWrite(LED_BUILTIN,HIGH);
  }
  else if (data=="OFF")
  {
    digitalWrite(LED_BUILTIN,LOW);
  }

}
