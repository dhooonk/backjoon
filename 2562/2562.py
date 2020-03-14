arr=[]

for i in range(9):
    user_input=int(input())
    arr.append(user_input)

print(max(arr))
print(arr.index(max(arr))+1)