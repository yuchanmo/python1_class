# f = open('새파일.txt',mode='w',encoding='utf-8')
# for i in range(1,11):
#     data = '%d번째 줄입니다\n' %i
#     f.write(data)
# f.close()


f = open('새파일.txt',mode='r',encoding='utf-8')
ss = f.readlines()
i = 0
while True:
    line = f.readline()
    if not line:
        f.seek(0,0)
        i+=1
        continue
    if i ==3:  
        break
    print(line)
f.close()