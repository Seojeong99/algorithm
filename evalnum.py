num = int(input())
result = []
sum=0
for i in range(num):
    array = list(map(int,input().split()))
    for j in array:
        sum+=j
    average=sum/10
    result.append(average)
    sum=0

for i in range (num):
 print("#{} {}".format(i+1,round(result[i])))
