class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int n=tokens.size();
        stack<int> s;
        for(int i=0;i<n;i++){
        if(tokens[i]=="+"){
            // first read and then delete the elements
            int ele1=s.top();s.pop();
            int ele2=s.top();s.pop();
            s.push(ele1+ele2);
        }else if(tokens[i]=="-"){
            // first read and then delete the elements
            int ele1=s.top();s.pop();
            int ele2=s.top();s.pop();
            s.push(ele2-ele1);
        }
            else if(tokens[i]=="*"){
            // first read and then delete the elements
            int ele1=s.top();s.pop();
            int ele2=s.top();s.pop();
            s.push(ele1*ele2);
            }else if(tokens[i]=="/"){
            // first read and then delete the elements
            int ele1=s.top();s.pop();
            int ele2=s.top();s.pop();
            s.push(ele2/ele1);
            } else{
                int sign = 1;
                int j=0;
                // converting string to integer
                if(tokens[i][0]=='-'){
                    sign =-1;
                    j++;
                }
                int val=0;
                for(;j<tokens[i].size();j++){
                    val=val*10+(tokens[i][j]-'0');
                }
                // remember this closing parenthesis, it causes error
                    s.push(val*sign);
                }
        }
                return s.top();

            }

    
};