class Solution {
public:
    void reverseString(vector<char>& s) {
        reverseRecursive(s, 0, s.size() - 1);
    }
    void reverseRecursive(vector<char>& s, int start, int end) {
        if (start >= end) {
            return;
        }
        // Swap characters at the start and end positions
        char temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        // Recursively reverse the substring from start+1 to end-1
        reverseRecursive(s, start + 1, end - 1);
    }
};
