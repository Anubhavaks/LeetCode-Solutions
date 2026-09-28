class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Deals with patterns like a*, a*b*, or .* matching an empty string s
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                char_s = s[i - 1]
                char_p = p[j - 1]
                
                if char_p == char_s or char_p == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif char_p == '*':
                    # Case 1: Count zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: Count one or more occurrences if the preceding element matches
                    prev_p = p[j - 2]
                    if prev_p == char_s or prev_p == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]
        