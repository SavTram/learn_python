# Theater Square
m,n,a = map(int, input().split())
if m >= n:
    m = (m+n)
    n = m - n
    m = m - n
if n <= a:
    print(1)
if n > a and m <= a:
    if n % a == 0:
        print(n // a)
    else:
        print(n//a +1)
if m > a:
    if m % a == 0 and n % a ==0:
        print((m//a)*(n//a))
    if m % a != 0 and n % a ==0:
        print((m//a +1)*(n//a))
    if m % a == 0 and n % a !=0:
        print((n//a +1)*(m//a))
    if m % a != 0 and n % a !=0:
        print((m//a +1)*(n//a +1))
# Domino Piling        
m, n = map(int, input().split())
if m <= 1 and n <= 1:
    print(0)
else:
    print(m * n // 2)        
# Elephant        
x = int(input())
l = [5,4,3,2,1]
t = 0
y = 0
for i in l:
    if y < x or x > 0:
        if x >= i:
            t += (x//i) 
        if x < i:
            t += (x//i +1) 
        y += t*i
        x = x - y
print(t)


