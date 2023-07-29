class Solution {
public:
    string removeOuterParentheses(string s) {
              string ans = "";
        stack<char> st;
        
        for(char c : s){
            if(c == '(') st.push(c);
            if(st.size() > 1) ans += c;
            if(c == ')') st.pop();
        }
        
        return ans;
    }
};

        
   