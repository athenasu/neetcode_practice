from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        # 57.8% faster, 2 pointers
        numbers.sort()
        right, left = 0, len(numbers) - 1
        while left > right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                left -= 1
            elif current_sum < target:
                right += 1
            else:
                return [right + 1, left + 1]


        # 68.57% faster, 1 pointer
        # dictionary = {}
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in dictionary:
        #         return [dictionary[diff] + 1, i + 1]
        #     else:
        #         dictionary[numbers[i]] = i

my_solution = Solution()
numbers = [-1,0]
target = -1
# numbers = [2,7,11,15]
# target = 9
print(my_solution.twoSum(numbers, target))