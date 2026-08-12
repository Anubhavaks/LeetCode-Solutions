class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        while(j<=len(nums2)-1):
            if(i>len(nums1)-1):
                nums1.insert(i,nums2[j])
                j+=1
            elif(nums1[i]>=nums2[j]):
                nums1.insert(i,nums2[j])
                j+=1
            else:
                i+=1
        n=len(nums1)
        m=len(nums1)-1
        if(n%2==0):
            ans=(nums1[m//2]+nums1[(m//2)+1])/2
        else:
            ans=nums1[(m+1)//2]
        return ans


        