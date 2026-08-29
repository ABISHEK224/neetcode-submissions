class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        left =0
        right=0
        hashMap = {}
        longestWindow=0
        while left<=right and right<len(string):
            if string[right] not in hashMap:
                hashMap[string[right]]=1
            else:
                longestWindow = max(len(hashMap.keys()),longestWindow)
                while string[right] in hashMap:
                    hashMap.pop(string[left])
                    left+=1
                hashMap[string[right]] = 1
            right+=1
        return max(len(hashMap.keys()),longestWindow)