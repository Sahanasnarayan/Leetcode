class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0;
        int r=height.size()-1;
        int maxarea=0;
        while(l<r){
            int width=r-l;
            maxarea=max(maxarea, min(height[r],height[l])*width);
            if(height[l]<=height[r]){
                l++;
            }
                else {
                    r--;
                }

            
        }
     return maxarea;   
    }
};