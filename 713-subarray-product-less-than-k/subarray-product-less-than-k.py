class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prd=1
        left=0
        ans=0
        if(k<=1):
            return 0
        for right in range(len(nums)):
            prd*=nums[right]
            while(prd>=k):
                prd//=nums[left]
                left+=1
            ans+=right-left+1
        return ans
        

        