from typing import List, Any
from teoria_combinatoria import permutacion, variacion, combinacion
import numpy, threading, datetime

lim=100
fin = False
num = 1
maxBall = 24
ONE = 1
winnerSing = 6
ball = range(ONE, maxBall)
ball_imt = tuple(ball)
allWinnerProb: List[tuple] = []
valor = True
print("numero: ",combinacion(maxBall, winnerSing))
maxNum = int(combinacion(maxBall, winnerSing))

def timeStop():
    global valor, fin, num, maxNum
    fijo = 60
    timeValue = fijo
    valor2 = datetime.timedelta(seconds=timeValue)
    timeInit = datetime.datetime.now()
    while True:
      timeEnd = datetime.datetime.now()
      if timeEnd - timeInit > valor2:
          timeValue +=fijo
          print(timeValue)
          valor2 = datetime.timedelta(seconds=timeValue)
          print("proceso: ", num, "de: ", maxNum)
    return


def winnerRandom():
    winner_array: List[int] = []
    global ball_imt, ONE
    num_ = ONE
    while True:
        numberRandom_ = numpy.random.randint(len(ball_imt))
        val = ball_imt[numberRandom_]
        if val in winner_array:
            continue
        else:
            winner_array.append(val)
        if len(winner_array) == winnerSing:
            break
        else:
            num_ += ONE
    return winner_array



def winnerJoin():
    winner = winnerRandom()
    winner_join = ""
    for win in winner:
        if win > 9:
            winner_join += str(win)
        else:
            winner_join += f"0{str(win)}"
    return winner_join


def allCombiner():
    global maxBall, allWinnerProb
    for i in range(maxBall):
        x = tuple(winnerRandom())
        if x not in allWinnerProb:
            allWinnerProb.append(x)
        else:
            continue
    return
def allCombiner2():
    global maxBall, allWinnerProb, winnerSing, num,fin
    test = combinacion(maxBall, winnerSing)
    timeInit= datetime.datetime.now()
    while True:
        if fin:
            break
        x = tuple(winnerRandom())
        if len(allWinnerProb) == test:
            break
        if x not in allWinnerProb:
            allWinnerProb.append(x)
            num +=1
        else:
            continue

    timeEnd = datetime.datetime.now()
    print("proseso duro ", timeEnd-timeInit, "iteraxciones:", num)
    return "listo"


def main():
    global lim
    print("inicio")
    x1 = threading.Thread(target=timeStop, args=())
    x1.start()

    for i in range(lim):
        name_ = "thread" + str(i)
        x0 = threading.Thread(target=allCombiner2, args=(), name=name_)
        x0.start()
        if(i==lim-1):
            print("listo")

    x1.join()
    return
