class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
    int i=0;
       int reverse=0;
        while(i<32){
            reverse=reverse<<1;
            if((n&1)==1){
                reverse = reverse|1;
            }
            n=n>>1;
            i++;
     
        }
    return reverse;
    }
};