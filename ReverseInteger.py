"""
7. Reverse Integer: https://leetcode.com/problems/reverse-integer/

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        while x >0:
            rem = x % 10
            sum = sum * 10 + rem
            x = x // 10
        if not -2**31 < sum < 2**31-1:
            return 0
        return sign*sum
