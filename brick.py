import math
def snt(n):
    if n%2==0 and n>2:
        return False
    s= 3
    while s>=3 and s<= n //2:
        if n%s ==0:
            return False
        s +=2
    return True
def snt_next(n):
    i = n+1
    while i >n:
        if snt(i) == True:
            li.append(i)
            break
        i +=1   
t = int(input())
l = []
for i in range(t):
    n = int(input())
    l.append(n)
m = int(math.sqrt(max(l)))
li = []
for i in range(2, m +1):
    if snt(i) == True:
        li.append(i)
snt_next(li[-1])
k = []
for o in l:
    for index in range(len(li) -1):
        j = li[index] * li[index + 1]
        k.append(j)
        if j > o: 
            print(o - k[-2])
            break
        if j ==o:
            print('0')
            break


