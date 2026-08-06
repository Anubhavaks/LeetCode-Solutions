class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while(low<=high):
            mid=(low+high)//2
            if self.candiv(nums,threshold,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def candiv(self,nums,threshold,mid):
        sum=0
        for num in nums:
            sum+=(num+mid-1)//mid
            if sum>threshold:
                return False
        return sum<=threshold
        