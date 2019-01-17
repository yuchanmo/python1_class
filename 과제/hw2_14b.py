def count_matches(some_list,value):
    if len(some_list) == 0:
        return 0
    cnt = 1 if some_list[0] == value else 0
    return cnt + count_matches(some_list[1:],value)

# count_matches([0, 1, 0, 4, 2, 0], 0) 
# count_matches(["a", "b", "c"], 1) 
# count_matches([], "a") 

def double_each(some_list):
    if len(some_list)==0:
        return []
    return [some_list[0]]*2 + double_each(some_list[1:])


# nums=[1,2,3]
# double_each(nums)
# double_each([])

def sums_to(nums,k):
    if len(nums) == 0:
        return 0==k
    return sums_to(nums[1:],k-nums[0])
    

# nums = [1, 2, 3] 
# sums_to(nums,6)
# sums_to(nums, 5) 
# sums_to([], 1) 


def is_reverse(x,y):
  if x == '' and y == '':
    return True
  elif x == '' or y == '':
    return False
  elif x[0].lower() != y[-1].lower():
    return False
  else:
    return is_reverse(x[1:], y[:-1])

  
# is_reverse("abc","cba")
# is_reverse("abc","abc")
# is_reverse("abc","dcba")

def sort_repated(L):
  for i in set(L):
    L.remove(i)
  return list(set(L))

# sort_repeated([1,2,3,2,1])
# sort_repeated([1,2,3,2,2,4])
# sort_repeated(list(range(100)))
    

def makeDictnumber(lst):
    dic = {}
    for v in lst:
        if v in dic:
            dic[v]+=1
        else:
            dic[v]=1
    return dic

#without get 
def mostFrequent(lst):
    dic = makeDictnumber(lst)
    return sorted(dic.items(),key = lambda d : d[1],reverse=True)[0][0]

#get version
def mostFrequent2(lst):
  dic= makeDictnumber(lst)
  return max(dic, key=dic.get)

# mostFrequent([2,5,3,4,6,4,2,4,5])
# mostFrequent2([2,5,3,4,6,4,2,4,5])



def histogram(letters):
    vs = list(letters.values())
    ks = set(vs)
    d = dict()
    for k in ks:
        d[k]=vs.count(k)
    return d

# letters = {1: "a", 2: "b", 3:"a"}
# histogram(letters) 
# letters = {1: "a", 2: "b", 3:"c"}
# histogram(letters)
# letters[4] = "a"
# letters[5] = "b"
# letters[6] = "a"
# histogram(letters)



