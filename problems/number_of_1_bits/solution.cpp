class Solution {
public:
    int hammingWeight(uint32_t n) {
        int i=0;
        int sum=0;
        while(i<32){
      
        if((n&1)==1){
            sum=sum+1;
        }
          n= n>>1;
        i++;
        }
    return sum;    
    }
};