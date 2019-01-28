friend_dict ={}
with open('data.csv') as csvfile:
    for line in csvfile:
        rowarray = line.strip().split(',')
        friend_dict[rowarray[0]] = rowarray[1:]
    print(friend_dict)