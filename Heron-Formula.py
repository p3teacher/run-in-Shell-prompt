# Heron’s Formula
# 2024-02-16
#
# test data 1 : 3,4,5
# test data 2 : 30,40,50
#
"""
Q:
un-sortted /unformated imports error!!!
---------------------------------------
A:
go to pyproject.toml and remove the 
'I' from the select variable list
"""
import math
#
print('please input 3 numbers separate by ,')
nums = [int(i) for i in input().split(',')]
nums.sort()
print(nums)
s = int((nums[0] + nums[1] + nums[2]) / 2)
Area_of_Triangle = math.sqrt(s*(s-nums[0])*(s-nums[1])*(s-nums[2]))
#
print("s =", s)
print("s*(s-nums[0])*(s-nums[1])*(s- nums[2]) = ", s*(s-nums[0])*(s-nums[1])*(s-nums[2]) )
print("Area of Triangle =", int(Area_of_Triangle))