#  141A - Amusing Joke
a = input()
b = input()
t = input()
c = a+b
d1 = {}
d2 = {}
if len(c) == len(t):
  for i in range(len(c)):
    if c[i] not in d1:
        d1[c[i]] = 1
    else:
        d1[c[i]] += 1
    if t[i] not in d2:
        d2[t[i]] = 1
    else:
        d2[t[i]] += 1 
  if (sorted(d1.items())==sorted(d2.items())):
    print('YES')
  else:
    print('NO')
else:
  print('NO')

# 672B - Different is Good
a = int(input())
b = input()
d = {}
for i in range(a):
    if b[i] not in d:
        d[b[i]] = 1
    else:
        d[b[i]] += 1
d = sorted(d.values())
t = sum(d) - len(d)
if t > (26 - len(d)):
  print(-1)
else:
  print(t)
