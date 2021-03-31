class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack [-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    count = max(count, i-stack[-1])
                else:
                    stack.append(i)
                
        return count