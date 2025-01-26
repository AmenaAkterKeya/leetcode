class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i', 'o','u'}
        current_count = 0
        maxVowel_count = 0
        for i in range(k):
            if s[i] in vowel:
                current_count += 1
        maxVowel_count = current_count
        for i in range(k,len(s)):
            if s[i] in vowel:
                current_count += 1
            if s[i-k] in vowel:
                current_count -= 1
            maxVowel_count = max(maxVowel_count,current_count)
        return maxVowel_count

