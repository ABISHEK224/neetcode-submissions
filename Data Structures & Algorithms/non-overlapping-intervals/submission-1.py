class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        lastEnd = intervals[0][1]
        toBeRemoved = 0
        for start,end in intervals[1:]:
            if start < lastEnd:
                toBeRemoved+=1
                lastEnd= min(lastEnd,end)
            else:
                lastEnd = end
        return toBeRemoved






        