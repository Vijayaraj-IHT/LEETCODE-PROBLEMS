from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        counts = Counter(students)
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                counts[sandwich] -= 1
            else:
                return counts[0] + counts[1]
        return 0