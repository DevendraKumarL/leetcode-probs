'''
    Problem:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

    Solution:
    -Travers the array
        -Store a dictionary <arrayElement, elementIndex>
        -Subtract currentArrElement from target sum. tmp = target-arr[i]
        -Find key tmp in dict, if found result is [i, dict[tmp]]
        -If not found Keep updating dict[arr[i]] = i
'''

class Solution:
    def twoSum(self, nums: List[int], target: int):
        dict = {}
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if (temp in dict):
                return [i, dict[temp]]
            dict[nums[i]] = i