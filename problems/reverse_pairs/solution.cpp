class Solution {
public:
    int n, ans = 0;

    void merge(vector<int> &nums, int low, int mid, int high) {
        int j = mid + 1;
        for (int i = low; i <= mid; i++) {
            long long val = 2LL * nums[j];
            while (j <= high && (long long)nums[i] > val) {
                j++;
                if (j <= high)
                    val = 2LL * nums[j];
            }
            ans += (j - (mid + 1));
        }

        int left = low, right = mid + 1, k = 0;
        vector<int> temp(high - low + 1);
        while (left <= mid && right <= high) {
            if (nums[left] <= nums[right]) { // Changed '<' to '<='
                temp[k] = nums[left];
                k++;
                left++;
            } else {
                temp[k] = nums[right];
                k++;
                right++;
            }
        }

        while (left <= mid) {
            temp[k] = nums[left];
            k++;
            left++;
        }

        while (right <= high) {
            temp[k] = nums[right];
            k++;
            right++;
        }

        k = 0;
        for (int i = low; i <= high; i++) {
            nums[i] = temp[k++];
        }
    }

    void mergeSort(vector<int> &nums, int low, int high) {
        if (low >= high) return;
        int mid = low + (high - low) / 2;
        mergeSort(nums, low, mid);
        mergeSort(nums, mid + 1, high);
        merge(nums, low, mid, high);
    }

    int reversePairs(vector<int> &nums) {
        n = nums.size();
        mergeSort(nums, 0, n - 1);
        return ans;
    }
};
