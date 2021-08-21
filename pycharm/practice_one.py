import dice

#dice.py를 import 해 다음의 질문에 답하시오.
#도박에 관심이 있었던 프랑스 귀족 슈발리에가 1654년에 제안한 문제
#카지노는 한 쌍의 주사위를 24번 던져 적어도 한 번 이상 두 주사위가 모두 6이 나오면 승리하는 게임이다.
#슈발리에는 뛰어난 수학자에게 이 도박이 본인에게 유리한지, 도박장에 유리한지를 질문하였다.
# 한 쌍을 주사위를 24번 던지는 사건을 10,000번 반복하여 승리할 횟수를 구하시오.
dice1=dice.Dice()
dice2=dice.Dice()
win =0
for a in range(1,10001):
    for b in range(1,25):
        dice1.roll()
        dice2.roll()
        if dice1.getDice()==6 and dice2.getDice() ==6:
            win+=1
            break

print(win)
