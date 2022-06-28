#include <Wire.h>
#include "Centipede.h"
#include <SPI.h>
#include <SD.h>

// init vars
Centipede cent;
File file;
int arr1[64];
int arr2[64];
int coord1 = 65;
int coord2 = 65;

void setup()
{
  Wire.begin();
  cent.initialize();

  // Gen File
  randomSeed(analogRead(0));
  int rand = random(10000);
  char buffer[5];
  sprintf(buffer, "%u", rand);
  file = SD.open(buffer);

  // pinning setup
  cent.portMode(0, 0b0111111001111110); // Set all Centipede pins to Input
  cent.portMode(1, 0b0111111001111110);
  cent.portMode(2, 0b0111111001111110);
  cent.portMode(3, 0b0111111001111110);
  pinMode(2, 1); // Connected to button to begin program
  pinMode(7, 0); // Power supply for all switches

  for (int i = 0; i < 64; i++)
  {
    arr1[i] = cent.digitalRead(i);
  }
}

void loop()
{
  while (coord2 == 65)
  { // loops until a move has been completed
    for (int i = 0; i < 64; i++)
    { // single scan
      arr2[i] = cent.digitalRead(i);
      if (coord1 != 65)
      {
        coord2 = arr2[i];
      }
      else
      {
        coord1 = arr2[i];
      }
    }
    if (arr2[coord1] == 1) // if the state of the first coordinate is HIGH, reset
    {
      coord1 = 65;
      coord2 = 65;
    }
  }

  while (digitalRead(2) != 1)
  {
    ;
  } // Wait for button on pin 2 to be pushed, ending move
  if (cent.digitalRead(coord1) == 1)
  { // if players undo the move, button resets coords
    coord1 = 65;
    coord2 = 65;
  }
  else
  {
    for (int i = 0; i < 64; i++)
    {
      arr2[i] = cent.digitalRead(i);
    }

    // Castling
    if (coord1 == 4 && coord2 == 7)
    { // White Short Castling
      if (cent.digitalRead(5) == 1 && cent.digitalRead(6) == 1)
      {
        file.print("O-O,");
      }
    }
    else if (coord1 == 60 && coord2 == 63) // Black Short Castling
    {
      if (cent.digitalRead(61) == 1 && cent.digitalRead(62) == 1)
      {
        file.print("O-O,");
      }
    }
    else if (coord1 == 4 && coord2 == 0) // White Long Castling
    {
      if (cent.digitalRead(2) == 1 && cent.digitalRead(3) == 1)
      {
        file.print("O-O-O,");
      }
    }
    else if (coord1 == 60 && coord2 == 56) // Black Long Castling
    {
      if (cent.digitalRead(58) == 1 && cent.digitalRead(59) == 1)
      {
        file.print("O-O-O,");
      }
    }
    else
    {
      file.print(String(coord1) + "," + String(coord2) + ",");
    }
    memcpy(arr1, arr2, sizeof(arr2));
  }
}