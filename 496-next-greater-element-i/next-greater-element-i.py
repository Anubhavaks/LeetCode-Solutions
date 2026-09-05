class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f={}
        stack=[]
        ans=[]
        l=-1
        for l in range(-1, -(len(nums2) + 1), -1):
            while len(stack)!=0 and stack[-1]<=nums2[l]:
                stack.pop()
            if len(stack)==0:
                f[nums2[l]]=-1
                stack.append(nums2[l])
            else:
                f[nums2[l]]=stack[-1]
                stack.append(nums2[l])
        for num in nums1:
            ans.append(f[num])
        return ans
            
        