class Solution:
    def average(self, salary: List[int]) -> float:
        Max=max(salary)
        Min=min(salary)
        salary.remove(Max)
        salary.remove(Min)
        sum=0
        for i in range (0,len(salary)):
            sum=sum+salary[i]
        avg=sum/(len(salary))
        return avg
        