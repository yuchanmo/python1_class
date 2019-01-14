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
        return 0
    summation = nums[0] + sums_to(nums[1:],k)
    return k == summation

nums = [1, 2, 3] 
sums_to(nums,6)
sums_to(nums, 5) 
sums_to([], 1) 
