'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    output = []
    
    for interval in intervals:
        if not output or output[-1][1] < interval[0]:
            output.append(interval)
        else:
            output[-1][1] = max(output[-1][1], interval[1])
            
    return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))