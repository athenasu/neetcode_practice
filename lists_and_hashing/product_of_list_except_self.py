from typing import List
from math import prod, floor


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        # Solution 2
        # O(n) time complexity, beats 66.9%; O(1) space complexity, beats 59.75%
        
        # prefix is the product of all the numbers that come before nums[i]
        # results[0] is 1 as a placeholder
        # Output: results = [1, 1, 2, 6]
        
        # multiply the results (or postfix) items to the postfix items
        # postfix is the product of all the numbers that come after nums[i]
        pass
        
    

my_solution = Solution()
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
print(my_solution.product_except_self(nums))


# Solution 1, too slow
# results = []
# for i in range(len(nums)):
#     temp = nums.pop(i)
#     results.append(prod(nums))
#     nums.insert(i, temp)
# return results

# [prod(nums) // num for num in nums]