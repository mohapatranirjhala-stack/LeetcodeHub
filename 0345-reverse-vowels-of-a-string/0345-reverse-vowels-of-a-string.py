class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[c for c in s if c in 'aeiouAEIOU']
        return ''.join(vowels.pop() if c in 'aeiouAEIOU' else c for c in s)
        