class Data:
    def __init__(self, task): self.task = task

class Teacher:
    def __init__(self):
        self.task = 0
        self.result = []
        self.solution = []
    def send_task(self, task, student):
        student.take_task(task)
        self.task += 1
    def take_solution(self, solution):
        self.solution.append(solution)
    def send_result(self, result, student):
        student.take_result(result)
        result += 1
class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = []
        self.zachet = []
        self.solution = []
    def take_task(self, task):
        self.knowledge.append(task)
    def send_solution(self, solution, teacher):
        teacher.take_solution(solution)
        self.solution.append(solution)
    def take_result(self, result):
        self.zachet.append(result)

t = Teacher()
p = Student("Ivan")
d = Data([1])
t.send_result(d.task[0], p)
print(t.task)
print(p.zachet)

