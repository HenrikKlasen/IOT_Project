//www.elegoo.com
//2018.10.25


#include <dht_nonblocking.h>
#include <Streaming.h>
#include <Wire.h>
#include "rgb_lcd.h"
#define DHT_SENSOR_TYPE DHT_TYPE_11
const int pinTempSensor = A0;
const int pinLight = A1;
const int pinSound = A2;
static const int DHT_SENSOR_PIN = 2;

rgb_lcd lcd;
const int colorR = 0;
const int colorG = 255;
const int colorB = 0;


DHT_nonblocking dht_sensor( DHT_SENSOR_PIN, DHT_SENSOR_TYPE );

/*
 * Initialize the serial port.
 */
void setup( )
{
  Serial.begin( 9600);
  lcd.begin(16, 2);
    
  lcd.setRGB(colorR, colorG, colorB);
  
  // Print a message to the LCD.
  lcd.print("Starting measurement");
  delay(1000);
}



/*
 * Poll for a measurement, keeping the state machine alive.  Returns
 * true if a measurement is available.
 */
const float R_fixed = 10000.0; 
float V_in = 5;
float calculateResistance(int analogValue) {
    float V_out = (analogValue / 1023.0) * V_in; // Convert analog reading to voltage
    float R_therm = R_fixed * ((V_in / V_out) - 1); // Calculate thermistor resistance
    return R_therm;
}
float calculateTemperature(float resistance) {
    // Steinhart-Hart coefficients
    const double B = 0.00026590253045476593;
    const double A = 0.0009136903488519239;
    
    double logR = log(resistance);
    double invT = A + B * logR; // Simplified equation without C term
    double temperatureK = 1.0 / invT;
    double temperatureC = temperatureK - 273.15; // Convert Kelvin to Celsius
    return temperatureC;
}

/*
 * Main program loop.
 */
void loop( )
{
  float t;
  //float temperature;
  float humidity;
  int sensorValLight;
  int sensorValSound;
  
  /* Measure temperature and humidity.  If the functions returns
     true, then a measurement is available. */
    int a = analogRead(pinTempSensor);
    float resistance = calculateResistance(a);
    float temperature = calculateTemperature(resistance);
    sensorValLight = analogRead(pinLight);
    sensorValSound = analogRead(pinSound);
    //Serial.println(t);
    Serial.println(temperature);
    //Serial.println(humidity);
    Serial.println(sensorValLight);
    Serial.println(sensorValSound);
    lcd.setCursor(0, 0);
    lcd.print("T:" + String(temperature) + "C, L: " + String(sensorValLight) + " ");
    lcd.setCursor(0, 1);
    lcd.print("S:" + String(sensorValSound) + "" );
    delay(3000);
}
