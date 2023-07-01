class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if ((mid == 0 || nums[mid - 1] < nums[mid]) &&
                (mid == nums.size() - 1 || nums[mid + 1] < nums[mid])) {
                return mid;
            }
            else if (mid > 0 && nums[mid - 1] > nums[mid]) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }

        return -1; // No peak element found
    }
};
 