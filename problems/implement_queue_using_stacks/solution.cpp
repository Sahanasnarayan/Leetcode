class MyQueue {
    stack<int> input, output;
public:

    void push(int x) {
        input.push(x);
    }
int pop() {
        peek();
        int x = output.top();
        output.pop();
        return x;
    }
    int peek(void) {
        if (output.empty())
            while (input.size())
                output.push(input.top()), input.pop();
        return output.top();
    }

    bool empty(void) {
        return input.empty() && output.empty();
    }
};
