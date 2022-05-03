num=int(input())
for t in range(num):
    s=str(input())
    all=[]
    turnNum=[0]*4
    binary=''
    turnten=''
    resultf=[]
    for k in s:
        all.append(k)


    #4개 단위로 하는 부분 넣기
    #for j in range(int(len(all)/4)):
    #4*j,4*(j+1)
    for j in range(int(len(all)/4)):
        for z in range(4*j,4*(j+1)):
            if (ord(all[z])>=65)&(ord(all[z])<=90):#여기들어가서 그런거였네 알파벳이랑 숫자 어떻게 구별할지
                turnNum[z-(4*j)]=ord(all[z])-65
            elif(ord(all[z])>=97)&(ord(all[z])<=122):
                turnNum[z-(4*j)]=ord(all[z]) - 71
            elif(ord(all[z])>=48)&(ord(all[z])<=57):#여기 안들어가는게 문제임
                turnNum[z-(4*j)]=ord(all[z]) + 4
            elif(ord(all[z])==43):
                turnNum[z-(4*j)]=ord(all[z]) + 19
            elif (ord(all[z]) == 47):
                turnNum[z-(4*j)] = ord(all[z]) + 16
        for i in range(0,4):
            firstbin = format(turnNum[i],'b')
            firstbin=firstbin.zfill(6)
            binary = binary + firstbin
            firstbin=0
        for k in range(0,3):
            for i in range(8*k,8*(k+1)):
                turnten=turnten+binary[i]
            resultf.append(chr(int(turnten,2)))
            turnten=''
        binary=''

        turnNum = [0] * 4
    print('#{} '.format(t+1),end='')
    for f in resultf:
        print(f,end='')
    print('')