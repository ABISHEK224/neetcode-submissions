import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for i in range(len(strs)):
            key = [0] * 26
            for s in strs[i]:
                key[ord(s) - ord('a')] += 1
            key = tuple(key)
            if key in result:
                result[key].extend([strs[i]])
            else:
                result[key] = [strs[i]]
        return list(result.values())