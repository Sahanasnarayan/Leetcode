class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Set of vowels

        # Two pointers
        i, j = 0, len(s) - 1

        # Convert string to list for easier swapping
        string_list = list(s)

        while i < j:
            if string_list[i] in vowels and string_list[j] in vowels:
                # Swap vowels
                string_list[i], string_list[j] = string_list[j], string_list[i]
                i += 1
                j -= 1
            elif string_list[i] in vowels:
                # Move j pointer if character at i is a vowel
                j -= 1
            else:
                # Move i pointer if character at j is not a vowel
                i += 1

        # Convert the list back to a string
        reversed_string = ''.join(string_list)

        return reversed_string