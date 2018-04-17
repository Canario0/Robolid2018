

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
    Serial.begin(9600);
}

void loop()
{
}

void serialEvent()
{
    if (Serial.readStringUntil('\n') == "enciendete"){
        Serial.println("LED encendido");
        digitalWrite(LED_BUILTIN, HIGH);
    }
}