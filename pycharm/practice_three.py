def extract_count(value):
    num=[]
    count=1
    c = list(','.join(value).split(','))
    num.append(c[0])
    for i in range(0,len(c)):

        try:
            if (ord(c[i])) != (ord(c[i+1])):
                num.append(count)
                count =1
                num.append(c[i+1])
            else:
                count +=1
        except :
            num.append(count)
            break
    for i in range(0, len(num)):
        print(num[i], end='')


a=str(input())
extract_count(a)


