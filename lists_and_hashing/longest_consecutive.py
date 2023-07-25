from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        """
            Find the longest consecutive element sequence
            Steps:
                1. Use a set to filter out duplicate numbers
                2. Find the start of the consecutive sequence
                3. If the length + the number is in the set, length += 1
                4. Return longest value
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        longest = 0
        num_set = set(nums)
        nums.sort()
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest


my_solution = Solution()
nums = [0,3,7,2,5,8,4,6,1,1] # Output: 9
print(my_solution.longest_consecutive(nums))


# # Solution 1, beat 63.18%
# # sort nums
# # start from nums[1] and see if the previous one == - 1, if it is, length += 1
# # else, return len(results)
# if len(nums) == 0:
#     return 0
# if len(nums) == 1:
#     return 1

# length = 1
# longest_consecutive = 1
# nums.sort()

# for i in range(1, len(nums)):
#     j = i - 1
#     if nums[j] + 1 == nums[i]:
#         length += 1
#         if length > longest_consecutive:
#             longest_consecutive = length
#     elif nums[j] == nums[i]:
#         continue
#     else:
#         length = 1
# return longest_consecutive
            
## Solution 2, beat 22.68%
# num_set = set(nums)
# longest = 0

# for num in nums:
#     # find the start of the consecutive num
#     if (num - 1) not in num_set:
#         length = 1
#         while (num + length) in num_set:
#             length += 1
#         longest = max(longest, length)
# return longest