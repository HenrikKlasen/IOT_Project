//www.elegoo.com
//2018.10.25


#include <dht_nonblocking.h>
#include <Streaming.h>
#define DHT_SENSOR_TYPE DHT_TYPE_11

const int pinLight = A1;
const int pinSound = A2;
static const int DHT_SENSOR_PIN = 2;
DHT_nonblocking dht_sensor( DHT_SENSOR_PIN, DHT_SENSOR_TYPE );

/*
 * Initialize the serial port.
 */
void setup( )
{
  Serial.begin( 9600);
}



/*
 * Poll for a measurement, keeping the state machine alive.  Returns
 * true if a measurement is available.
 */
static bool measure_environment( float *temperature, float *humidity)
{
  static unsigned long measurement_timestamp = millis( );

  /* Measure once every four seconds. */
  if( millis( ) - measurement_timestamp > 3000ul )
  {
    if( dht_sensor.measure( temperature, humidity ) == true )
    {
      measurement_timestamp = millis( );
      
        return( true );
      
    }
  }

  return( false );
}



/*
 * Main program loop.
 */
void loop( )
{
  float temperature;
  float humidity;
  int sensorValLight;
  int sensorValSound;
  
  /* Measure temperature and humidity.  If the functions returns
     true, then a measurement is available. */
  if( measure_environment( &temperature, &humidity) == true )
  {
    sensorValLight = analogRead(pinLight);
    sensorValSound = analogRead(pinSound);
    Serial.println(temperature);
    Serial.println(humidity);
    Serial.println(sensorValLight);
    Serial.println(sensorValSound);
    delay(3000);
  }
}
