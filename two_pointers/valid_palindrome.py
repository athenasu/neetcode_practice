import re

class Solution:
    def is_palindrome(self, s: str) -> bool:
        # clear out all spaces and non alphabet characters and .lower()
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s).lower()

        # 1 for loop and one variable to check from end
        return s == s[::-1]

my_solution = Solution()
# text = "A man, a plan, a canal: Panama"
text = '0P'
print(my_solution.is_palindrome(text))