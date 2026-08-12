class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f={}
        left=0
        right=0
        ans=0
        for right in range(len(nums)):
            f[nums[right]]=f.get(nums[right],0) +1
            while f[nums[right]] > k:
                f[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
                
        