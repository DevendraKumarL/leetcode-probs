/*
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
*/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0 || nums.size() == 1) return nums.size();
        int j = 1;
        while (j < nums.size()) {
            if (nums[j] == nums[j-1]) {
                nums.erase(nums.begin() + (j-1));
            } else {
                j++;
            }
        }
        return nums.size();
    }
};