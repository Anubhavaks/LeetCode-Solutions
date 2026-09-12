class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        stack=[]
        ans=[]
        n=len(nums)
        if len(nums)==1:
            return True
        stack.append(nums[0])
        ans.append(nums[0])
        for i in range(1,len(nums)):
            if stack and nums[i]>=stack[-1]:
                stack.append(nums[i])
            if ans and nums[i]<=ans[-1]:
                ans.append(nums[i])
        if n==len(stack) or n==len(ans):
            return True
        else:
            return False

        