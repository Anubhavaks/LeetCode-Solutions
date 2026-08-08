class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=1
        high=max(bloomDay)
        res=-1
        while(low<=high):
            mid=(low+high)//2
            if self.canmake(bloomDay,mid,m,k):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def canmake(self,bloomDay,mid,m,k):
        i=0
        ans=[]
        count=0
        bouq=0
        for bloom in bloomDay:
            if(bloom<=mid):
                if(count+1==k):
                    bouq+=1
                    count=0
                else:
                    count+=1
            else:
                count=0
        return bouq>=m

        