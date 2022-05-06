k= int(input())
for k in range(k):
    n= int(input())
    all=[]
    for z in range(n):
        alpha, num = map(str, input().split())
        num = int(num)
        for i in range(num):
            all.append(alpha)

    print('#{}'.format(k+1))
    count=0
    for i in range(len(all)):
        print(all[i],end='')
        count=count+1
        if (count==10):
            print('')
            count=0
    print('')
