class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        cantEat = len(students)

        for curr in sandwiches:
            if counter[curr]>0:
                cantEat -=1
                counter[curr]-=1
            else:
                break
        return cantEat