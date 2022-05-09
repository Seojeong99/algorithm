testcase=int(input())
for k in range(testcase):
    num=str(input())
    origin=[]
    for i in range(len(num)):
        origin.append(int(num[i]))

    count=0
    first=origin[0]
    if(origin[0]==1):
            count=count+1
    for i in range(0,len(origin)-1):
        for j in range(i+1,i+2):
            if(origin[i]!=origin[j]):
                count=count+1
    print('#{} {}'.format(k+1,count))