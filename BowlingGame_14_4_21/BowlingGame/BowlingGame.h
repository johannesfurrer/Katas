#pragma once

#include<cstdint>

class BowlingGame
{
private:
  int scoreSum;

  int pinsPerThrow[24];
  int throwIndex;

  void initPinArray();

public:
  BowlingGame();
  void rollPin(int pins);
  int getScore();
};


//------------BowlingGame.cpp------------------

BowlingGame::BowlingGame(): scoreSum(0), throwIndex(0)
{
  initPinArray();
}

void BowlingGame::initPinArray()
{
  for (int i = 0; i < 23; i++)
  {
    pinsPerThrow[i] = 0;
  }
}

void BowlingGame::rollPin(int pins)
{
  pinsPerThrow[throwIndex] = pins;
  if (pins == 10)
  {
    throwIndex+=2;
  }
  else
  {
    throwIndex++;
  }
 
}

int BowlingGame::getScore()
{
  //1. Interate over array
  for (int i = 0; i < 22; i++)
  {
    //2. Check value == 10?
    if (pinsPerThrow[i] == 10)
    {
      if (i <= 21)
      {
        scoreSum += 2*pinsPerThrow[i + 2];
      }
      
    }
    else 
    {
      scoreSum += pinsPerThrow[i];
    }
  }
  
  
  //3. End of array
  //  a. yes

  return scoreSum;
}
