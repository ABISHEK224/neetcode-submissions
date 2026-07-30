class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not len(s):
            return 0
        left =0
        right = 0
        result = 0
        freqMap = {}
        maxFreq=0
        for right in range(len(s)):
            if s[right] in freqMap:
                freqMap[s[right]] = freqMap[s[right]]+1
            else: 
                freqMap[s[right]] = 1
            maxFreq = max(maxFreq,freqMap[s[right]])
            while (right-left+1) - maxFreq > k:
                freqMap[s[left]]-=1
                left=left+1
            result = max(right-left+1,result)
        return result
        