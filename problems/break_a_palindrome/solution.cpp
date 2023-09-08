class Solution {
public:
    string breakPalindrome(string palind) {
      if (palind.size() <= 1) return "";

    for (size_t i = 0; i < palind.size() / 2; i++) {
        if (palind[i] > 'a') {
            palind[i] = 'a';
            return palind;
        }
    }

    palind[palind.size() - 1]  = 'b';
    return palind;  
    }
};