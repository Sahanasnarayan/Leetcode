class Solution {
public:

    int getDivSum(int x){
        if (x<5){
            return 0;
        }
        int summ = 0;
        int cnt = 0;
        for (int i = 1; i*i<=x; i++){
            if (x%i == 0){
                if (x/i == i){
                  summ += i;
                  ++cnt;
                }
                else{
                  summ += i + (x/i);
                  cnt += 2;
                }
            }
        }
        if (cnt == 4){
            return summ;
        }
        return 0;
    }


    int sumFourDivisors(vector<int>& nums) {
        int sum = 0;
        for (int i = 0; i<nums.size(); i++){
            sum = sum + getDivSum(nums[i]);
        }
        return sum;
    }
};