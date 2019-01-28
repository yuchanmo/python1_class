import time
n = 10000000
l = []
start = time.time()
for i in range(n):
    l.append(i)

end = time.time()
timelapsed = end - start
print(timelapsed)

s = set()
start = time.time()
for i in range(n):
    s.add(i)

end = time.time()
timelapsed = end - start
print(timelapsed)