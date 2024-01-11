#!/usr/bin/env python
# coding: utf-8

# In[31]:


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_x = 0
        x1 = x
        X_MIN = -2**31
        X_MAX = 2**31 - 1
        if x < 0 or (x != 0 and x % 10 == 0) or x < X_MIN or x > X_MAX:
            return False
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return x1 == reversed_x


# In[33]:


x = 131
solution = Solution()
result = solution.isPalindrome(x)
print(result)

