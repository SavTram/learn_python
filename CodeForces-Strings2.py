#  43B - Letter
def ktra(di1,di2):
  for x in di2:
    if not(x in di1 and di2[x] <= di1[x]):
      return False
  return True
a = input().replace(' ','')
b = input().replace(' ','')
di1 = {}
di2 = {}
for x in a:
  if x not in di1:
    di1[x] = 1
  else:
    di1[x] += 1
for x in b:
  if x not in di2:
    di2[x] = 1
  else:
    di2[x] += 1
if ktra(di1,di2) == True:
  print('YES')
else:
  print('NO')
# 3A - Shortest path of the king 
a = input()
b = input()
x = ord(a[0]) - ord(b[0])
y = int(a[1]) - int(b[1])
if x < 0:
    xstep = 'R'
    x = -x
else:
    xstep = 'L'
if y < 0:
    ystep = 'U'
    y = -y
else:
    ystep = 'D'
print(max(x,y))
while x > y:
    print(xstep)
    x -=1
while x < y:
    print(ystep)
    y -=1
while x:
    print(xstep + ystep)
    x -=1
