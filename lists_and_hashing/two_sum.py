class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in dictionary:
                return [dictionary[result], i]
            else:
                dictionary[num] = i
        return []
    
my_solution = Solution()
nums = [1, 2, 5, 7, 8]
target = 10
print(my_solution.two_sum(nums, target))