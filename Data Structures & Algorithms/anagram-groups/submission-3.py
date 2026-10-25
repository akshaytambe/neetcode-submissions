class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            char_count = [0] * 26

            for char in str:
                char_count[ord(char) - ord("a")] += 1

            if tuple(char_count) in res:
                res[tuple(char_count)].append(str)
            else:
               res[tuple(char_count)] = [str]
        
        ans = []
        for key, item in res.items():
            ans.append(item)
        
        return ans