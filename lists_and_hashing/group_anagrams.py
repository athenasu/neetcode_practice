from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in dictionary:
                dictionary.get(sorted_string).append(string)
            else:
                dictionary[sorted_string] = [string]
        return dictionary.values()
    
my_solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(my_solution.group_anagrams(strs))