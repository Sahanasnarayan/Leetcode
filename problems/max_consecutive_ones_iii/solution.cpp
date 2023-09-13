class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        // sliding window approach
        int i = 0, j = 0;	
	    while (i < nums.size()) {
	        if (nums[i] == 0) k--; //u flip the zero and decrement k
	        if (k < 0) {
                // to flipback the one's to zero's'
	            if (nums[j] == 0){ 
                k++;
                }
	            j++;
	        }
	        i++;
	    }
	    return i - j;
    }
};