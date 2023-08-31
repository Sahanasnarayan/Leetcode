class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
      vector<int> jumps(n+1, 0);
        
        for(int i = 0; i<n+1; i++) {
            int l = max(0, i-ranges[i]);
            int r = min(n, i+ranges[i]);
            
            jumps[l] = max(jumps[l], r-l); //from l, that's farthest I can jump to right
        }
        int currEnd  = 0;
        int maxReach = 0;
        int count    = 0;
        for(int i = 0; i<n; i++) {
            maxReach = max(maxReach, jumps[i]+i);
            
            if(i == currEnd) {
                count++;
                currEnd = maxReach;
            }
        }
        
        if(currEnd >= n)
            return count;
        return -1;  
    }
};