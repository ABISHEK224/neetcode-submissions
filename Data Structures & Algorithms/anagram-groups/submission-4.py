class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        result = []
        for s in strs:
            arr = [0]*26
            for letter in s:
                arr[ord(letter)-97]+=1
            tuple_ = tuple(arr)
            if tuple_ in hashMap:
                hashMap[tuple_].append(s)
            else:
                hashMap[tuple_] = [s]
        
        for v in hashMap.values():
            result.append(v)
        return result

        
                



        