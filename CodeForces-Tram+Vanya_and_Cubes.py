# Tram
n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        t = a + b
    if i != 0:
        t = t - a + b
    l.append(t)
print(max(l))


# Vanya_and_Cubes
n = int(input())
sum = 0
count = 0
for i in range(1,n+1):
    sum += (i*(i+1)//2)
    if sum <= n:
        count +=1
print(count)
