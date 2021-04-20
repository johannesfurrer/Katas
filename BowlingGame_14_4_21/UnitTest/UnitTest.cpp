#include "pch.h"
#include "../BowlingGame/BowlingGame.h"
#include "UnitTest.h"



#define MAX_THROWS_WITHOUT_STRIKE 21
#define POINTS_WITH_ALL_1         21
#define MAX_POINTS                300


// aux functions 
void rollAllPinsSameValue(int value, BowlingGame *gameToRoll)
{
  for (int i = 0; i < MAX_THROWS_WITHOUT_STRIKE; i++)
  {
    gameToRoll->rollPin(value);
  }
}

void rollAllStrikes(BowlingGame* gameToRoll)
{
  for (int i = 0; i < 13; i++)
  {
    gameToRoll->rollPin(10);
  }
}

TEST(Init, can_create) {
  BowlingGame myGame;
  myGame.rollPin(0);
  //EXPECT_EQ(1, 0);
  //EXPECT_TRUE(true);
}



TEST(Game, roll_all_0) 
{
  BowlingGame myGame;
  rollAllPinsSameValue(0 , &myGame);
  EXPECT_EQ(myGame.getScore(), 0);
}


TEST(Game, roll_all_1) 
{
  BowlingGame myGame;
  rollAllPinsSameValue(1 , &myGame);
  EXPECT_EQ(myGame.getScore(), POINTS_WITH_ALL_1);
}

TEST(Game, roll_perfect_game)
{
  BowlingGame myGame;
  rollAllStrikes(&myGame);
  EXPECT_EQ(myGame.getScore(), MAX_POINTS);
}


