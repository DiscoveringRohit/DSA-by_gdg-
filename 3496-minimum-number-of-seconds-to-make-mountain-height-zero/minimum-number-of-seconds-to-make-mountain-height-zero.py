class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def canFinish(time):
            total = 0
            
            for t in workerTimes:
                # solve k(k+1)/2 * t <= time
                # k^2 + k - (2*time/t) <= 0
                
                import math
                k = int((math.sqrt(1 + 8*(time//t)) - 1) // 2)
                total += k
                
                if total >= mountainHeight:
                    return True
            
            return False
        
        l = 0
        r = 10**18
        
        while l < r:
            mid = (l + r) // 2
            
            if canFinish(mid):
                r = mid
            else:
                l = mid + 1
        
        return l