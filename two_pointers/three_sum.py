from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 2
        # 3 pointers, one main, 2 from ends of the list
        pass


        
    

my_solution = Solution()
# nums = [0,0,0]
# nums = [0,1,1]
nums = [-1,0,1,2,-1,-4]
print(my_solution.threeSum(nums))


# Solution 1: takes too long
# results = []
# length = len(nums)
# target = 0

# for i in range(length):
#     for j in range(i + 1, length):
#         for k in range(j + 1, length):
#             if nums[i] + nums[j] + nums[k] == target:
#                 my_list = [nums[i], nums[j], nums[k]]
#                 my_list.sort()
#                 if my_list not in results:
#                     results.append(my_list)
# return results


# Solution 2
# results = []
# nums.sort()

# for i, num in enumerate(nums):
#     # skip positive numbers
#     if num > 0:
#         break
    
#     # skip repeated numbers if num is repeated
#     if i > 0 and num == nums[i - 1]: 
#         continue

#     left, right = i + 1, len(nums) - 1

#     while left < right:
#         num_sum = num + nums[left] + nums[right]
#         if num_sum > 0:
#             right -= 1
#         elif num_sum < 0:
#             left += 1
#         else:
#             results.append([num, nums[left], nums[right]])
#             left += 1
#             right -= 1
#             # skip same number
#             while nums[left] == nums[left - 1] and left < right:
#                 left += 1
# return results