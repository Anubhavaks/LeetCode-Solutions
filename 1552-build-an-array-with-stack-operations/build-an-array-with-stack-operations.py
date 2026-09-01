class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        f=set()
        t=set()
        ans=[]
        for num in target:
            f.add(num)
        for i in range(1,n+1):
            if i in f:
                ans.append("Push")
                t.add(i)
                if (t==f):
                    return ans
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans


        