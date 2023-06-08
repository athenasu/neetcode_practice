class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

s = 'test'
t = 'ttse'

my_solution = Solution()
print(my_solution.isAnagram(s, t))