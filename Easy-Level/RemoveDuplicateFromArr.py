'''
    Problem:
    Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2]

    Solution:
        -start from index i = 1 and loop until end of list
        -if nums[i] == nums[i-1] delete item at i
        -else increment i
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        j = 1
        while j < len(nums):
            if (nums[j] == nums[j-1]):
                nums.pop(j-1)
            else:
                j = j + 1
        return len(nums)