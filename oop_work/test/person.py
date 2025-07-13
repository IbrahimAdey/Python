from problem import problem

class Person:
    def __init__(self, name: str, age: int, gender: str):   # constructor in python
        self.__name = name
        self.__age = age
        self.gender = gender
        self.__problems = []    # private and can only be accessible to the class

    def add_problem(self, problem: problem):
        self.__problems.append(problem)


person1 = Person("John", 12, "male")
