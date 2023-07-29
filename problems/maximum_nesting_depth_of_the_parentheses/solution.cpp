class Solution {
public:
    int maxDepth(string s) {
        
        int result=0,current=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
             current+=1;
             result=max(result,current);
            }

        
        else if(s[i]==')'){
        current-=1;
        }}
return result;
    }
    
};