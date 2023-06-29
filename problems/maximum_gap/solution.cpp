class Solution {
public:
    int maximumGap(vector<int>& nums) {
          sort(nums.begin(),nums.end());
        int b=0;
        if(nums.size()<2){
            return 0;
        }
       for (int i = 0; i < nums.size() - 1; i++){
            int a = nums[i+1]-nums[i];
            b = max(a,b);

    }
    
        return b;
    
    }
};