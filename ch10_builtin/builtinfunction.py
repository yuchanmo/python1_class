def enumgenerate(l):
    idx = 0
    for v in l:
        yield idx, v
        idx+=1

a = list(range(100))

b = enumgenerate(a)

for aa,bb in b:
    print(aa,bb)


seqstring = 'Python'
list(reversed(seqstring))

type(reversed(seqstring))

v = reversed

lb = [24,-1,421,-36,22,8]
lsr= sorted(lb,key=int,reverse=True)