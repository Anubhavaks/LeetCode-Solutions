class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        target = len(nums) // 2
        
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > target:
                return num
        