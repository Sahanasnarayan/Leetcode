class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
     stack<int> st;
     int n=heights.size();
     vector<int> left(n),right(n);
     for(int i=0;i<n;i++){
         int cur=heights[i];
         while(!st.empty() && heights[st.top()]>=cur) st.pop();
         if(st.empty())left[i]=0;
         else left[i] = st.top()+1;
         st.push(i);
     }      
     while(!st.empty())st.pop();
     for (int i=n-1;i>=0;i--){
          int cur=heights[i];
         while(!st.empty() && heights[st.top()] >= cur) st.pop();
         if(st.empty())right[i]=n-1;
         else right[i]=st.top()-1;
         st.push(i);
     }  
     int ans=0;
     for(int i=0;i<n;i++)
     ans=max(ans,heights[i]*(right[i]-left[i]+1));
     return ans;
       }
};