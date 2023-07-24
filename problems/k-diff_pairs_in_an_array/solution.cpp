class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        std::vector<int> set;
        sort(nums.begin(), nums.end());

        int left = 0;
        int right = 1;
        int count=0;
        while (right < nums.size()){
        if(nums[right]-nums[left]==k){
             if (std::find(set.begin(), set.end(), nums[left]) == set.end()) {
           count+=1;
           set.push_back(nums[left]);
           }
           left+=1;
           right=left+1;
        }
         else if(nums[right]-nums[left]>k){
             left+=1;
             right=left+1;
         }
         else{
         right+=1;

         }
        }

        return count;
    }
};