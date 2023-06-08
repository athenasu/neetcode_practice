class Solution(object):
    def is_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

s = 'test'
t = 'ttse'

my_solution = Solution()
print(my_solution.is_anagram(s, t))