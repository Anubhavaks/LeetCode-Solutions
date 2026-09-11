class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] <num:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index  
            stack.append(i)
        return ans


        


            

        