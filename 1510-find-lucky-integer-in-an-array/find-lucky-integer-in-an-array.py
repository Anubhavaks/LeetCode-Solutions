class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f={}
        maxi=-1
        for num in arr:
            f[num]=f.get(num,0)+1
        for element in f:
            if element==f[element]:
                maxi=max(element,maxi)
        return maxi

        