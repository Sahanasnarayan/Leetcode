class Solution {
public:
    int longestValidParentheses(string s) {
       stack<int>st;
       int n= s.length();
       vector<int> ones(n,0);
       for(int i=0;i<n;i++){
           if(s[i]=='('){
               st.push(i);
           }else if(!st.empty()){
                   ones[i]=1;
                   ones[st.top()]=1;
                   st.pop();
               }
           }
           int ans=0,count=0;
           for(int i=0;i<n;i++){
               if (ones[i]==1)count++;
               else{
                   ans=max(count,ans);
                   count=0;
               }
           }
               ans= max(ans,count);
               return ans;
           }
};