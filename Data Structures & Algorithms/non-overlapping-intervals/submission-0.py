class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        currPrev = intervals[0][1]
        output = 0

        for i, interval in enumerate(intervals):
            start, end = interval

            # We hit an interval
            if currPrev > start:
                output += 1

                if currPrev > end:
                    currPrev = end
            else:
                currPrev = end

        
        return output-1
        