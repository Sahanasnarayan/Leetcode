class MinStack {
public:
    #define ll long long int 
    // this is the bestmethod solve the problem using this logic 
    stack<ll>s;
    int min_ele;
    
    MinStack() {
        min_ele=INT_MAX;
    }
    
    void push(int val) {
        
        if(s.size()==0){
            
            s.push(val);
            min_ele=val;
        }
        
        else if( val >= min_ele){
            s.push(val);
        }
        
        else {
            s.push(2LL*val-min_ele);
            min_ele=val;
        }
    }
    
    void pop() {
  
      if(s.top() >=min_ele){
            s.pop();
        }
        else if(s.top() < min_ele){
            min_ele=2LL*min_ele-s.top();
            s.pop();
        }
    }
    
    int top() {
        if(s.top() >=min_ele){
            return s.top();
        }
        else{
            return min_ele;
        }
    }
    
    int getMin() {
      
        return min_ele;
    }
};

