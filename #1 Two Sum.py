"""
Given an array of integers `nums` and an integer `target`, 
return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

https://leetcode.com/problems/two-sum/
"""

class MySolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = []
        for i, n in enumerate(nums):
            m = target - n
            if m in nums and nums.index(m) != i:
                idx.append(i)
                idx.append(nums.index(m))
        return list(set(idx))

## Runtime: 140 ms, faster than 5.21% of Python3 online submissions for Two Sum.
## Memory Usage: 14.5 MB, less than 12.96% of Python3 online submissions for Two Sum.


class BestSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d: return [d[m], i]
            else: d[n] = i

## Runtime: 48 ms, faster than 63.00% of Python3 online submissions for Two Sum.
## Memory Usage: 14.4 MB, less than 75.09% of Python3 online submissions for Two Sum.