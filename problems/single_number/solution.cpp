class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int arr =nums[0];
        int i=1;
        while(i<nums.size()){
            arr=arr^nums[i];
            i++;
        }
    
    return arr;
    }
};