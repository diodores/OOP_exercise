class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        """Ставим оценку лектору"""

        mylist = {}
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            mylist[course] = rate
            lecturer.assessment_lecturer.append(mylist)
        else:
            return 'Ошибка'

    def average_rating(self):
        """Возвращает средний балл"""
        mylist = []
        for i in self.grades.values():
            mylist.append(i)
        average_rating = sum(mylist) / len(mylist)
        return average_rating


    def __lt__(self, other):
        """Сравниваем студентов по критерию - средний балл"""
        try:
            if not isinstance(other, Student):
                return 'Не корректные данные. Сравнить можно только оценки студентов.'
            elif other.average_rating() < self.average_rating():
                return f'Средний бал {self.name}, выше балла {other.name}'
            else:
                return f'Средний бал {other.name}, выше балла {self.name}'
        except IndentationError:
            print('Не корректные данные. Сравнить можно только оценки объектов однго класса.')
        except ZeroDivisionError:
            print('У одного из студентов отсутсвуют оценки.')


    def __str__(self):
        res = f'some_student\nИмя: {self.name}\nФамилия: {self.surname}\n \
        \rСредняя оценка за домашнее задание: {self.average_rating()}\n\
        \rКурсы в процессе изучения: {self.courses_in_progress}\n\
        \rЗавершенные курсы: {self.finished_courses}'
        return res



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
        """Возвращает средний балл"""
        mylist = []
        for i in self.assessment_lecturer:
            for score in i.values():
                mylist.append(score)
        average_rating = sum(mylist) / len(mylist)
        return average_rating

    def __lt__(self, other):
        """Сравниваем лекторов по критерию - средний балл"""
        try:
            if not isinstance(other, Lecturer):
                return 'Не корректные данные. Сравнить можно только оценки лекторов.'
            elif other.average_rating() < self.average_rating():
                return f'Средний бал {self.name}, выше балла {other.name}'
            else:
                return f'Средний бал {other.name}, выше балла {self.name}'
        except IndentationError:
            print('Не корректные данные. Сравнить можно только оценки объектов однго класса.')
        except ZeroDivisionError:
            print('У одного из лекторов отсутсвуют оценки.')

    def __str__(self):
        res = f' some_lecturer\n Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rating()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Ставим оценку студенту"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Определим вывод данных"""
        res = f' some_reviewer\n Имя: {self.name}\n Фамилия: {self.surname}'
        return res


student = Student('Dmitrij', 'Sazhin', 'man')
student.courses_in_progress += ['python']
lectur = Lecturer('Oleg', 'Bulygin')
lectur.courses_attached += ['python']
student.rate_lecturer(lectur, 'python', 10)
a = Student('Q', 'O', 'b')
a.courses_in_progress = ['python']
a.rate_lecturer(lectur, 'python', 9)
lectur.average_rating()
q = Lecturer('w', 's')
q.courses_attached = ['python']
student.rate_lecturer(q, 'python', 7)
print(q > lectur)
print(student > lectur)
student.grades['p']=8
student.grades['py']=8
a.grades['p']= 9
a.grades['py']= 10
print(a < lectur)
print(student.grades)
print(student.average_rating())
g = Reviewer('Alex', 'Shpak')
print(g)
print(q)
print(student)