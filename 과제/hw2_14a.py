def first_perfect_square(lst):
    for i,v in enumerate(lst):
        if v >= 0:
            res = v ** 0.5
            if res == int(res):
                return i
    return -1

# first_perfect_square(list(range(5)))
# first_perfect_square([2,4,6,8,10,12])
# first_perfect_square([6,8,10,12,9])
# first_perfect_square([1,1])
# first_perfect_square([-6,-6,-2,2,-3,3])
# first_perfect_square([42])
# first_perfect_square([])
# first_perfect_square([123456789123456789**2])

def num_perfect_squares(numbers):
    cnt = 0
    for i,v in enumerate(numbers):
        if v >=0:
            res = v ** 0.5
            if res == int(res):
                cnt += 1
    return cnt

# num_perfect_squares([])
# num_perfect_squares([0])
# num_perfect_squares([0,1])
# num_perfect_squares(list(range(10)))
# num_perfect_squares([3]*10)
# num_perfect_squares([4]*10)
# num_perfect_squares([-4,-2,0,2,4])


def second_largest(values):
    largest = values[0]
    second_largest = values[0]
    for i in range(1,len(values)):
        if values[i] > largest :
            largest,second_largest = values[i],largest
        else:
            if values[i] > second_largest:
                second_largest = values[i]
    return second_largest
    #return sorted(values,reverse = True)[1]

# second_largest([3,-2,10,-1,5])
# second_largest([-2,1,1,-3,5])
# second_largest([1,2,3,3])
# second_largest(["alpha","gamma","beta","delta"])
# second_largest([3.1,3.1])
# second_largest([True,False,False,True])
# second_largest([False,False,True])

def print_french(lo,hi):
    for i in range(lo,hi+1):
        print(i,"\t: ",num_in_french(i))

def digit(num,pos):
    return (num // 10** (pos-1)) % 10

def num_in_french(num):
    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix","onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    
    if not(0<=num<=100):
        return ("The given number: ",num, "is out of bound,Try again!")

    # Part 1: get the ones and tens digits of num

    one_val = digit(num,1)
    ten_val = digit(num,2)
    hundred_val = digit(num,3)

    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 10
    if hundred_val == 1:
        return ("cent")
    if ten_val < 2:
        return (ones_list[num])

    # Part 4: case when the numbers are 70, 71, 72,...79, and 90, 91, 92,...99

    if (ten_val ==7 or ten_val == 9):
        if num == 71:
            return (tens_list[7] + " et onze")
        if num == 91:
            return (tens_list[9] + "-onze")
        
        irregular = ["dix", " ","douze","treize","quatorze",
                    "quinze","seize","dix-sept","dix-huit","dix-neuf"]
        return (tens_list[ten_val] + "-" + irregular[one_val])
    
    # Part 5: otherwise the case when the numbers are 20, 30, 40, ...
    if one_val ==0:
        if ten_val == 8:
            return (tens_list[ten_val] + "s")
        return (tens_list[ten_val])

    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...

    if one_val == 1:
        if ten_val == 8:
            return (tens_list[ten_val]+ "-un")
        return (tens_list[ten_val]+" et un")

    return (tens_list[ten_val]+"-"+ones_list[one_val])


print_french(0, 3)
print_french(18, 19) 
print_french(100, 100) 
print_french(12, 13) 
print_french(70, 73) 
print_french(90, 92) 
print_french(19, 20)
print_french(40, 40)  
print_french(79, 80) 
print_french(20, 22) 
print_french(51, 51) 
print_french(80, 82) 