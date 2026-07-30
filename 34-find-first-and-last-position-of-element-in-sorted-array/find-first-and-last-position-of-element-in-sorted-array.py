class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return[self.firstpos(nums,target),self.lastpos(nums,target)]

    def firstpos(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                right=mid-1
                ans=mid    
            elif (nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return ans
    
    def lastpos(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                left=mid+1
                ans=mid    
            elif (nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return ans

        