avg=[]
result=[]
testAvg=0
cnt=0
overAvgRatio=0

caseNum=int(input())

#리스트 만들어주기
for i in range(caseNum):
    testList=list(map(int,input().split(' ')))
    num=testList[0]
    del testList[0]
    testAvg=sum(testList)/num
    avg.append(testAvg)

    for j in testList:
        if j>avg[i]:
            cnt+=1

    overAvgRatio=(cnt/num)*100
    cnt=0

    result.append(overAvgRatio)

for i in range(len(result)):
    print("%.3f" %round(result[i],3)+"%")    