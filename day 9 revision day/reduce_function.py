from functools import reduce

nums = [1,2,3,4]
sum_all = reduce(lambda x,y: x+y, nums)
print(sum_all)