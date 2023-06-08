from typing import List
from math import prod, floor


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 2
        # O(n) time complexity, O(1) space complexity
        results = [1] * len(nums)
        prefix = 1
        postfix = 1
        # prefix is the product of all the numbers that come before nums[i]
        # results[0] is 1 as a placeholder
        # Output: results = [1, 1, 2, 6]
        for i in range(len(nums)):
            results[i] = prefix
            prefix *= nums[i]
        # multiply the results (or postfix) items to the postfix items
        # postfix is the product of all the numbers that come after nums[i]
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]
        return results

        # # will be the product of the pre[i - 1] before self and the post[i + 1]
        # results = []
        # # stores the product of all the numbers including self, previous index is the product of all except self and after
        # pre = []
        # prefix = 1
        # # stores the product of all the numbers from self and on
        # post = [1] * len(nums)
        # postfix = 1
        # for i, num in enumerate(nums):
        #     pre.append(prefix * num)
        #     prefix = pre[i]
        # for i in range(len(nums) - 1, -1, -1):
        #     post[i] = (nums[i] * postfix)
        #     postfix = post[i]
        # prefix = 1
        # for i in range(1, len(nums) - 1):
        #      results.append(pre[i - 1] * post[i + 1])
        #      prefix = pre[i]
        # return results

        
    

my_solution = Solution()
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
print(my_solution.productExceptSelf(nums))


# Solution 1, too slow
# results = []
# for i in range(len(nums)):
#     temp = nums.pop(i)
#     results.append(prod(nums))
#     nums.insert(i, temp)
# return results

# [prod(nums) // num for num in nums]