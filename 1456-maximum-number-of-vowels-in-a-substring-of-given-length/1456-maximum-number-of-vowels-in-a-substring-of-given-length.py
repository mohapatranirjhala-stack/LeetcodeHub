class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr = max_cnt = sum(c in vowels for c in s[:k])
        for i in range(k, len(s)):
            curr += (s[i] in vowels) - (s[i - k] in vowels)
            if curr > max_cnt: max_cnt = curr
        return max_cnt