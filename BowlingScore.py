def DoOneRoll(score):
       ergebnis = 0 
       strike = False
       spare = False
       for i in range(len(score)):
              if spare:
                     spare = False
                     ergebnis += score[i]
              if strike:
                     ergebnis+=score[i]
                     spare = True
                     strike = False

              if (i % 2 == 1 and score[i] + score[i-1] == 10):
                     spare =True
              if score[i] == 10:
                     strike=True

              ergebnis += score[i]
       return ergebnis



def returnScoreBoard(score):
       ergebnis =[]
       Lastscore = 0
       for i in range(len(score)):
              if (i % 2 == 1 and score[i] + score[i-1] == 10):
                     if i+1 < len(score):
                            ergebnis.append(Lastscore + score[i] + score[i+1])
                     else:
                            ergebnis.append(Lastscore + score[i])  
              if score[i] == 10:
                     if i+2 < len(score):+
       