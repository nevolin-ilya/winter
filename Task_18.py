class Data:
    def __init__(self, task): self.task = task

class Teacher:
    def __init__(self, result):
        self.work = 0
        self.result = result
        self.solution = []
    def send_task(self, task, student):
        student.take(task)
        self.work += 1
    def take_solution(self, solution):
        self.solution.append(solution)
    def send_result(self, result, student):
        student.take_result(result)
        result += 1
class Student:
    def __init__(self, name, solution):
        self.name = name
        self.knowledge = []
        self.zachet = []
        self.solution = solution
    def take_task(self, task):
        self.knowledge.append(task)
    def send_solution(self, solution, teacher):
        teacher.take(solution)
        self.solution += 1
    def take_result(self, result):
        self.zachet.append(result)


