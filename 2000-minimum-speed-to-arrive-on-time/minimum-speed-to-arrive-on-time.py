class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low=1
        high=10**7
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if self.tim(dist, mid,hour):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


    def tim(self, dist: List[int], mid: int, hour: float)->bool:
        sum=0
        fir=dist[len(dist)-1]/mid
        for i in range(len(dist)-1):
            sum+=math.ceil(dist[i]/mid)
        sum+=fir
        return sum<=hour

        
        