class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq = collections.deque(students)
        stack = sandwiches[::-1]

        while True:
            curr = dq.popleft()
            if curr == stack[-1]:
                stack.pop()
            else:
                dq.append(curr)
            if len(stack)==0 or (stack[-1]==0 and len(dq)==sum(dq)) or (stack[-1]==1 and sum(dq)==0):
                break
        return len(dq)
        