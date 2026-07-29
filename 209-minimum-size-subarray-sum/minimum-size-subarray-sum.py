class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=float('inf')
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]
            while(sum>=target):
                ans=min(ans,right-left+1)
                sum-=nums[left]
                left+=1
        return 0 if ans==float('inf') else ans
