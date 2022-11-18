#define BUZZER_PIN 3
#define LDR_PIN A4

#include "SerialTransfer.h"
#include <TroykaLight.h>

SerialTransfer myTransfer;
TroykaLight sensorLight(LDR_PIN);

void setup() {
  Serial.begin(115200);
  myTransfer.begin(Serial);
}


void loop() {
  float light_lux;

  sensorLight.read();
  light_lux = sensorLight.getLightLux();

  memcpy(myTransfer.packet.txBuff, &light_lux, sizeof(float));
  myTransfer.sendData(sizeof(float));
}