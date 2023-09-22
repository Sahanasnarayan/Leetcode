class Solution {
public:
    int n;
    vector<int> ans;

    void merge(vector<pair<int, int>>& enumNums, int low, int mid, int high) {
        int j = mid + 1;
        for (int i = low; i <= mid; i++) {
            while (j <= high && enumNums[i].second > enumNums[j].second) {
                j++;
            }
            ans[enumNums[i].first] += j - (mid + 1);
        }

        int left = low, right = mid + 1, k = 0;
        vector<pair<int, int>> temp(high - low + 1);
        while (left <= mid && right <= high) {
            if (enumNums[left].second <= enumNums[right].second) {
                temp[k] = enumNums[left];
                k++;
                left++;
            } else {
                temp[k] = enumNums[right];
                k++;
                right++;
            }
        }

        while (left <= mid) {
            temp[k] = enumNums[left];
            k++;
            left++;
        }

        while (right <= high) {
            temp[k] = enumNums[right];
            k++;
            right++;
        }

        k = 0;
        for (int i = low; i <= high; i++) {
            enumNums[i] = temp[k++];
        }
    }

    void mergeSort(vector<pair<int, int>>& enumNums, int low, int high) {
        if (low >= high) return;
        int mid = low + (high - low) / 2;
        mergeSort(enumNums, low, mid);
        mergeSort(enumNums, mid + 1, high);
        merge(enumNums, low, mid, high);
    }

    vector<int> countSmaller(vector<int>& nums) {
        n = nums.size();
        ans.resize(n);
        vector<pair<int, int>> enumNums;
        for (int i = 0; i < n; i++) {
            enumNums.push_back({i, nums[i]});
        }
        mergeSort(enumNums, 0, n - 1);
        return ans;
    }
};