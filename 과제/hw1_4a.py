#1. Write a function f1(list) that will return the number of odd elements 1. Write a function f1(list) that will return the number of odd elements 1. Write a function f1(list) that will return the number of odd elements 1. Write a function f1(list) that will return the number of odd elements
def f1(list):
    cnt = 0
    for i in range(len(list)):
        if list[i] % 2 == 1 :
            cnt +=1 
    return cnt
# f1([1,2,3,4])
# f1([1,2,3,4,5])


#Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list. 2. Write a function f2(list) that will print each odd element in given list.
def f2(list):    
    for i in range(len(list)):
        if list[i] % 2 == 1 :
            print(list[i])
# f2([1,2,3,4])
# f2([1,2,3,4,5])



#3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements 3. Write a function f3(list) that will return the sum of all odd elements in a given list. in a given list. in a given list. in a given list. in        
def f3(list):
    summary = 0
    for i in range(0,len(list)):
        if list[i] % 2 == 1 :
            summary+=list[i]
    return summary
# f3([1,2,3,4,5])
# f3([1,2,3,4])

def f4(list):
    summary = 0
    for i in range(0,len(list)):
        if list[i] % 2 == 1 :
            summary+=i
    return summary

# f4([1,2,3,4])
# f4([1,2,3,4,5])

        
def f5(list):
    for i in range(0,len(list)):
        originalval = list[i]
        list[i] = originalval ** 2
    return list

# f5([1,2,3,4])
# f5([1,2,3,4,5])


def f6(list):
    largest = list[0]
    for i in range(0,len(list)):
        if largest < list[i]:
            largest = list[i]
    return largest

# f6([1,2,3,4])
# f6([1,2,3,4,5])


def f7(list):
    sumofvals = 0
    for i in range(0,len(list)):
        sumofvals += list[i]
    avgofvals = sumofvals / len(list)
    return avgofvals

# f7([1,2,3,4])
# f7([1,2,3,4,5])


def f8(a,b,n):
    for i in range(a,b+1):
        if i % n == 0 :
            print(i)    

# f8(1,10,2)


def f9(width,height):
    for h in range(height):
        for w in range(width):
            print('*',end=''),
        print()

# f9(0,1)
# f9(10,0)
# f9(1,1)
# f9(5,5)

def f10(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=''),
        print()

# f10(1)
# f10(2)
# f10(3)


def f11(list):
    is_sorted_by_desc = True
    for i in range(0,len(list)-1):
        if list[i] < list[i+1]:
            is_sorted_by_desc = False
            break
    return is_sorted_by_desc

# f11([])
# f11([5,4,3,2,1])
# f11([5,4,3,2,0])
# f11([5,4,5,2])


#12. Write a function 12. Write a function 12. Write a function 12. Write a function 12. Write a function f12(list) f12(list) that will return that will return that will return that will return True Trueif the list consists of all negative if the list consists of all negative
def f12(list):
    is_all_negative_values = True
    for i in range(0,len(list)):
        if list[i] >=0 :
            is_all_negative_values = False
            break
    return is_all_negative_values

# f12([])
# f12([-1,-2,-3,-4,5])
# f12([1,2,3,4,5])
# f12([-1,-2,-3])

#13. 13. Write a function 13. Write a function 13. Write a function f13(list,target) f13(list,target) f13(list,target) that will return the index of last that will return the index of last that will return the index of last that will return the index of last that will return the index of last that will return the index of last occurrence of target in the list. Assume list is nonempty and always occurrence of target in the list. Assume list is nonempty and always occurrence of target in the list. Assume list is nonempty and always occurrence of target in the list. Assume list is nonempty and always occurrence of target in the list. Assume list is nonempty and always
def f13(list,target):    
    for i in range(len(list)-1,-1,-1):
        if list[i] == target:
            return i

# f13([1,2,3,1,2,3],3)
# f13([1,2,3],3)
# f13([1,1,1,1],1)


#14. Write a function 14. Write a function 14. Write a function 14. Write a function 14. Write a function f14(list) f14(list) that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative that will return the index of last negative number in the list. Assume list is nonempty and always contains a negative number
def f14(list):
    for i in range(len(list)-1,-1,-1):
        if list[i] < 0:
            return i

# f14([1,2,-3])
# f14([1,-2,-3,1,-2,-3])
# f14([-1,1,1,1])

#15. Write a function 15. Write a function 15. Write a function 15. Write a function 15. Write a function f15(list) f15(list) that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even that will return the sum of all elements at even index positions. index positions. index
def f15(list):
    sum = 0
    for i in range(0,len(list),2):
        sum+=list[i]
    return sum

# f15([1,2,-3])
# f15([1,-2,-3,1,-2,-3])
# f15([-1,1,1,1])


#16. Write a function 16. Write a function 16. Write a function 16. Write a function 16. Write a function f16(n) f16(n) that will print out an upside down triangle. that will print out an upside down triangle. that will print out an upside down triangle. that will print out an upside down triangle. that will print out an upside down triangle.
def f16(n):
    for r in range(n,-1,-1):
        for c in range(r):
            print('*',end='')
        print()

# f16(3)
# f16(2)
# f16(1)



#17. Write a function 17. Write a function 17. Write a function
def f17(list):
    if len(list) == 1:
        print(list[0])
    else:
        for i in range(len(list)-1,-1,-2):
            print(list[i])

# f17([1,2,3,4,5,6])
# f17([1,2,3,4])
# f17([1])

#1818. Write a function 18. Write a function 18. Write a function 18. Write a function 18. Write a function f18(n) f18(n)that will return n! that will return n! that will return n! that
def f18(n):
    
    if n == 0:
        return 1   
    return n*f18(n-1)

# f18(0)
# f18(2)
# f18(3)

#. Write a function . Write a function
def f19(list):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
    for i in range(len(list)):
        factorial_result = factorial(list[i])
        print(factorial_result)

# f19([])
# f19([1,2,3])
# f19([1,2,3,4]) 


#20 . Write a function . Write a function . Write a function . Write a function . Write a function . Write a function . Write a function . Write a function f2 0(list) that will print a countdown starting from each that will print a countdown starting from each that will print a countdown starting from each that will print a countdown starting from each that will print a countdown starting from each that will print a countdown starting from each that will print a countdown starting from each that will print a countdown starting from each element to zero for a given list. element to zero for a given list. element to zero for a given list. element to zero for a given list. element to zero for a given list. element to zero for a given list. element to zero for a given list. element
def f20(list):
    def printcountdown(v):
        for i in range(v,-1,-1):
            print(i,end=' ')
    for j in range(len(list)):
        printcountdown(list[j])
        print()

# f20([])
# f20([1,2,3])
# f20([1,2,3,4]) 


#21 . Write a function . Write a function . Write a function . Write a function f2 1(list1, list2) (list1, list2) (list1, list2) (list1, list2) that will return a new list where each index in that will return a new list where each index in that will return a new list where each index in that will return a new list where each index in that will return a new list where each index in that will return a new list where each index in that will return a new list where each index in the new list corresponds to the new list corresponds to
def f21(list1,list2):
    #assert(len(list1)!=len(list2))
    reslist = []
    for i in range(len(list1)):
        sumval = list1[i] + list2[i]
        reslist.append(sumval)
    return reslist


# f21([1,2,3], [1,2,3]) 
# f21([0,0,0], [1,2,3]) 
# f21([], []) 

#22 22. Write a function . Write a function . Write a function . Write a function . Write a function f2 2(n)
def f22(n):
    for i in range(1,n+1):
        if i %2 ==0 or i %3 ==0:
            print(i)
        

# f22(10)
# f22(1)
# f22(3)


#23
def f23(list):
    largestval = list[0][0]
    for i in range(len(list)):
        for j in range(len(list[i])):
            if largestval < int(list[i][j]):
                largestval = list[i][j]
    return largestval

# f23([[1,2,3],[4,5,6],[7,8,9]]) 
# f23([[3,2,1],[0,-1,-2]]) 
# f23([[1,2,3,4],[],[34],[],[],[56],[67]]) 
# #f23([],[])

#24 정렬 필요
def f24(list):
    #selection sort
    
    for i in range(len(list)):
        tmp_val = list[i]
        tmp_idx = i
        for j in range(i+1,len(list)):
            if tmp_val < list[j]:
                tmp_idx = j
        list[i],list[tmp_idx] =list[tmp_idx],list[i]
    #second largest val from array ordered by desenceding
    return list[1]
 
# f24([1,4,3,2,5]) 
# f24([3,2]) 
# f24([3,4]) 

        
#25
def f25(n) : 
    while n >= 10:  
        n = n // 10; 
    return n 


# f25(1234) 
# f25(4321)
# f25(3) 

#26
def f26(list):
    def printlargestval(innerlist):
        largest_val = innerlist[0]
        for i in range(len(innerlist)):
            if innerlist[i] > largest_val:
                largest_val = innerlist[i]
        print(largest_val)
    for j in range(len(list)):
        printlargestval(list[j])

# f26([[1,2,3],[4,5,6],[7,8,9]])
# f26([[3,2,1],[0,-1,-2]]) 
# f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]]) 


