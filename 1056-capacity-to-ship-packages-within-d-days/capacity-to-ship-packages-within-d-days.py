class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            if self.capac(weights,mid,days):
                o=mid
                high=mid-1
            else:
                low=mid+1
        return o
    def capac(self,weights,mid,days):
        sum=0
        k=1
        for weight in weights:
            if(sum+weight>mid):
                k+=1
                sum=weight
            else:
                sum+=weight
                
        return k<=days
                


            
        