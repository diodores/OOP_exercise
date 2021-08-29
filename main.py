class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        mylist = {}
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            mylist[course] = rate
            lecturer.assessment_lecturer.append(mylist)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.assessment_lecturer = []

    def average_rating(self):
        mylist = []
        for i in self.assessment_lecturer:
            for score in i.values():
                mylist.append(score)
        average_rating = sum(mylist) / len(mylist)
        return average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'





student = Student('Dmitrij', 'Sazhin', 'man')
student.courses_in_progress += ['python']
lectur = Lecturer('Oleg', 'Bulygin')
lectur.courses_attached += ['python']
student.rate_lecturer(lectur, 'python', 10)
a = Student('Q', 'O', 'b')
a.courses_in_progress = ['python']
a.rate_lecturer(lectur, 'python', 9)
lectur.average_rating()
print(lectur.average_rating())