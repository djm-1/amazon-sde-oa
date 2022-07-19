"""
Maximize Score After N Operations/Number Game Solution
Amazon OA 2021

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.
In the i operation (1-indexed), you will:

- Choose two elements, x and y.
- Receive a score of i * gcd(x, y).
- Remove x and y from nums.

Return the maximum score you can receive after performing n operations.
The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:
Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

Example 2:
Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

Example 3:
Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

Constraints:
1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 10^6
"""
from typing import List
import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def calc_score(nums, scores):
            if not nums:
                return 0
            
            if tuple(nums) in scores:
                return scores[tuple(nums)]
            
            n = len(nums)/2
            maxScore = 0
            
            for i in range(int(2*n)):
                for j in range(i + 1, int(2*n)):
                    a = nums[i]
                    b = nums[j]
                    nums_copy = nums.copy()
                    nums_copy.remove(a)
                    nums_copy.remove(b)
                    score = int(n*math.gcd(a, b) + calc_score(nums_copy, scores))
                    
                    if score > maxScore:
                        maxScore = score
            
            scores[tuple(nums)] = maxScore
            return maxScore
        return calc_score(nums, {})