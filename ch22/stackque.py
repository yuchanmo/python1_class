cnt = 0
def hanoi(n,x,y,z):
    global cnt
    if(n>0):
        cnt += 1
        print(cnt)
        hanoi(n-1,x,z,y)
        print("move the top disk from tower " + x + 'to top of tower' + y)
        hanoi(n-1,z,y,x)

hanoi(3,'1','2','3')