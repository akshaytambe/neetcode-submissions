class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for index, char in enumerate(s):
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1

        for index, char in enumerate(t):
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] -= 1
        
        for char in seen:
            if seen[char] != 0:
                return False

        return True
        