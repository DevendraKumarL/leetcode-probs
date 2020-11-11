/*
    Problem:
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    Example:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2]

    Solution:
        -loop through arr starting from i = 0 until end of arr
        -remove element at i if matches the given val
        -return new arr size
*/
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        while (i < nums.size()) {
            if (nums[i] == val) {
                nums.erase(nums.begin() + i);
            } else {
                i++;
            }
        }
        return nums.size();
    }
};