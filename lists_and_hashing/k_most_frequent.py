from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # creates a list of empty lists of len(nums) + 1 : freq = [[], [], [], [], [], [], []]
        

        # adds count to number of times the number is repeated: count = {1: 3, 2: 2, 3: 1}
        
        
        # uses the frequency of the value to store the key
        # freq[3] = 1 --> [[], [], [], [1], [], [], []]
        
        # start from the back because the farther back means the more times the number was repeated
            # append the most frequent value to result
        pass


    

my_solution = Solution()
nums = [1,1,1,2,2,3]
k = 2

print(my_solution.top_k_frequent(nums, k))


# Solution 1
# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     dictionary = {}
#     results = []

#     for num in nums:
#         if num in dictionary:
#             dictionary[num] += 1
#         else:
#             dictionary[num] = 1
    
#     for _ in range(k):
#         # dictionary.get will find and return the key of the maximum value
#         max_val = max(dictionary, key=dictionary.get)
#         results.append(max_val)
#         del dictionary[max_val]
#     return results