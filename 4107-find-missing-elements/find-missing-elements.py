class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low=min(nums)
        high=max(nums)
        i=0
        ans=[]
        while(low<=high):
            if low in nums:
                low+=1
            else:
                ans.append(low)
                low+=1
                i+=1
        return ans



        