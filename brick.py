import math
def ktr_snt(n):
    if n %2==0:
        return False
    i = 3
    while i>=3 and i< n/2:
        if n% i ==0:
            return False
        i +=2
    return True
def nt_max(n):
    for h in range(3,n+1):
        if ktr_snt(h):
            li.append(h)
    return li[-1]
def gannhat(a,b):
    for m in range(a+1,b):
        if ktr_snt(m) == True:
            return False   
    return True
t= int(input('nhap t: '))
li = []
for i in range(t):
    h = int(input())
    li.append(h)
for o in li:
    stack = []
    if o <6:
        break
    if o < 15 and o >= 6:
        print(o - 6)
    else:
        b = int(math.sqrt(o))
        for x in range(3, b+1):
            t = ktr_snt(x)
            if t == True:
                stack.append(x)
    if stack:
        p = stack.pop() 
        k = o // p
        j = nt_max(k)
        p = min(p,j)
        j = max(p,j)
        if p == j :
            u = nt_max(p-2)
            print(o - u* j)
        if gannhat(p,j) == True and p != j:
            print(o - p * j)
        if gannhat(p,j) == False:
            s = nt_max(j-2)
            print(o - p*s)
