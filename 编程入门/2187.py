class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        realTrips = 0
        totalTime = 1
        while realTrips < totalTrips:
            realTrips = 0
            for t in time:
                realTrips = realTrips + totalTime // t

            totalTime = totalTime + 1

        return totalTime - 1


s = Solution()
s.minimumTime([1, 2, 3], 5)
