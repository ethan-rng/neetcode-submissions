"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # TC: O(n log n)
        if len(intervals) == 0: return True

        intervals.sort(key=lambda x: x.start)
        prevStart, prevEnd = intervals[0].start, intervals[0].end

        for i, interval in enumerate(intervals):
            if i == 0: continue
            currStart, currEnd = interval.start, interval.end

            if currStart >= prevStart and currStart < prevEnd: 
                print(prevStart, prevEnd, currStart, currEnd)
                return False
            
            prevStart, prevEnd = currStart, currEnd
        
        return True