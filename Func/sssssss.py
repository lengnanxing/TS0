def func(list):
    c= len(list)
    if c%2==0:
        while len(list)>2:
            c=len(list)
            #print(c)
            for i in range(1,c):
                if list[i]!=list[0]:
                    list.pop(0)
                    list.pop(i-1)
                    break
                if i==c-1:
                    return list[0]
        return (list[0])
    else:
        while len(list)>1:
            c=len(list)
            for i in range(1,c):
                if list[i]!=list[0]:
                    #print(i)
                    list.pop(0)
                    list.pop(i-1)
                    break
                if i ==c-1:
                    return list[0]
        return list[0]


#a=["5","4" ,"5" ]
#print(func(a))
#print(func(3))
if __name__ == '__main__':
    while True:
        a=input().split(" ")
        print(func(a))