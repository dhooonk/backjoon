testNum=int(input())
totalScore=0

testScore=list(map(int,input().split()))
    
maxScore=max(testScore)

for i in range(testNum):
    testScore[i]=testScore[i]/maxScore*100
    totalScore+=testScore[i]

avgScore=totalScore/testNum
print((avgScore))