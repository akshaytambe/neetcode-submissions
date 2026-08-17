class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            count_char = [0] * 26
            for char in str:
                count_char[ord(char) - ord("a")] += 1
            if tuple(count_char) in res:
                res[tuple(count_char)].append(str)
            else:
                res[tuple(count_char)] = [str]
        
        return list(res.values())