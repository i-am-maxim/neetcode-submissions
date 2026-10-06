class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for curr in operations:
            if curr == "+":
                prev1 = stack.pop()
                temp = prev1 + stack[-1]
                stack.append(prev1)
                stack.append(temp)
            elif curr == "D":
                stack.append(2*stack[-1])
            elif curr == "C":
                stack.pop()
            else:
                stack.append(int(curr))
        ans =0
        while stack:
            ans += stack.pop()
        return ans 
        