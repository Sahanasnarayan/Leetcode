class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        unable_to_eat = 0

        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                unable_to_eat = 0  # Reset the count if a student eats
            else:
                students.append(students.pop(0))
                unable_to_eat += 1

        # Check if all students are unable to eat
            if unable_to_eat == len(students):
                return unable_to_eat

        return 0