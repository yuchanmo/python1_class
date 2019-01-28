filename = 'alice.txt'

try:
    with open(filename,mode='r') as f:
        print(f.readlines())
except FileNotFoundError as ffe:
    print('filenotfound')
else:
    pass