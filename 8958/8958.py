testNum=int(input())
testArr=[]
score=0
Ocount=1

for i in range(testNum):
    test=(input())
    testArr.append(test)

for i in range(testNum):
    testGrading=list(testArr[i])
    for i in testGrading:
        if i=="O":
            score+=Ocount
            Ocount+=1
        else:
            Ocount=1
    print(score)
    score=0
    Ocount=1