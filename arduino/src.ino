

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
    Serial.begin(9600);
}

void loop()
{
    Serial.print("#");
    Serial.print(1);
    Serial.print("#");
    Serial.print(1);
    Serial.print("#");
    Serial.print(random(0,400));
    Serial.print("#");
    Serial.print(60);
    Serial.println("#");
    delay(1000);
}

void serialEvent()
{
    if (Serial.readStringUntil('\n') == "enciendete")
    {
        Serial.println("LED encendido");
        digitalWrite(LED_BUILTIN, HIGH);
    }
}