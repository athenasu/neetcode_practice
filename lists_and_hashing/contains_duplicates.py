class Solution(object):
    def contains_dupe_using_dict(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # solution 2
        # timeit: min 0.0810036 seconds
        dictionary = {}
        for num in nums:
            if dictionary.get(num):
                return True
            else:
                dictionary[num] = True
        return False

    def contains_dupe_using_set(self, nums):
        # solution 1
        # timeit:0.0731915 seconds
        return len(set(nums)) != len(nums)
    

my_list = [1, 2, 3, 1]
my_solutions = Solution()
print(my_solutions.contains_dupe_using_dict(my_list))

