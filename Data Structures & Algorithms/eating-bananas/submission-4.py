class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        lowest_speed = right

        while left <= right:
            mid = left + (right - left) //2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)

            if hours > h:
                left = mid + 1
            elif hours <= h:
                lowest = min(lowest_speed, mid)
                right = mid - 1

        return lowest