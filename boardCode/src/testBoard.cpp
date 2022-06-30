// Code for testing the Reed switches installed on the chessboard
// Current functional squares: 63, 55, 47, 39, 31, 23, 15

#include <Wire.h>
#include <Centipede.h>
#include <Arduino.h>

// init vars
Centipede cent;
int squares[] = {63, 55, 47, 39, 31, 23, 15};

void setup()
{
    Wire.begin();
    cent.initialize();
    Serial.begin(9600);

    // pinning setup
    cent.portMode(0, 0b0111111001111110); // Set all Centipede pins to Input
    cent.portMode(1, 0b0111111001111110);
    cent.portMode(2, 0b0111111001111110);
    cent.portMode(3, 0b0111111001111110);
    pinMode(4, 0); // Power supply pin
    digitalWrite(4, 1);
}

void loop()
{
    for (int i = 0; i < sizeof(squares); i++)
    {
        if (cent.digitalRead(squares[i]) == 1)
        {
            Serial.println(squares[i]);
        }
        else
        {
            Serial.println("0");
        }
        delay(50);
    }
}
