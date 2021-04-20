import unittest
from BowlingScore import DoOneRoll
from BowlingScore import returnScoreBoard


class TestCircleArea(unittest.TestCase):
    def test_function(self):
    
        self.assertEqual(DoOneRoll([1]), 1)
        self.assertEqual(DoOneRoll([0]),0)
        self.assertEqual(DoOneRoll([2]),2)
    def test_CalcScore(self):
        self.assertEqual(DoOneRoll([2,5]), 7)
        self.assertEqual(DoOneRoll([3,4,5]),12)
    def test_CalcScoreStrike(self):
        self.assertEqual(DoOneRoll([10,3,0]), 16)
        self.assertEqual(DoOneRoll([10,3,3]), 22)
        self.assertEqual(DoOneRoll([10,3,3,4,10,2,0]), 40)
        self.assertEqual(DoOneRoll([10,10,10,10,10,10,10,10,10,10,10]),300)
        self.assertEqual(DoOneRoll([10,10,10,10,10,10,10,10,10,10,9]),297)
    def test_CalcScoreSpare(self):
        self.assertEqual(DoOneRoll([9,1,1]),12)
        self.assertEqual(DoOneRoll([9,1,1,1,5,5,2,0,10,5]),47)
        self.assertEqual(DoOneRoll([10,2,0,5,5,1]),25)
        self.assertEqual(DoOneRoll([10,2,0,5,5,1,0,10]),35)

    def test_returnScoreBoard(self):
       self.assertEqual(returnScoreBoard([0]),[0])
       self.assertEqual(returnScoreBoard([1,0]),[1,1])
       self.assertEqual(returnScoreBoard([2,5]), [2,7])
       self.assertEqual(returnScoreBoard([2,5,10,2,0]), [2,7,19,21,21])
       self.assertEqual(returnScoreBoard([10]),[10])
       self.assertEqual(returnScoreBoard([10,10,0,0]),[20,30,30,30])
       self.assertEqual(returnScoreBoard([10,10,10,10,10,10,10,10,10,10,10]),[30,60,90,120,150,180,210,240,270,290,300])
       self.assertEqual(returnScoreBoard([10,10,10,10,10,10,10,10,10,10,9]),[30,60,90,120,150,180,210,240,269,288,297])