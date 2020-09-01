#include "DHT.h"     
#include <ArduinoJson.h>
#define DHTPIN 2     
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHTTYPE); 

void setup() {
  Serial.begin(9600);
}

void loop() {
  float tempvalue = dht.readTemperature();  // 변수 t에 온도 값을 저장
  float moisture = analogRead(A0);  //토양수분센서값 읽기
  String jsondata = "";
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& object = jsonBuffer.createObject();
  object["tempvalue"] = tempvalue;
  object["moisture"] = moisture;
  object.printTo(jsondata); //String으로 변환
  Serial.println(jsondata);
  delay(10000);
}
