class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        self.courses_in_progress.remove(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')
            return
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__calculate_mean_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    
    def __calculate_mean_grade(self):
        all_grades = []
        for grades_by_courses in self.grades.values():
            for grade in grades_by_courses:
                all_grades.append(grade)

        return round(sum(all_grades) / len(all_grades), 1)
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.__calculate_mean_grade() < other.__calculate_mean_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__calculate_mean_grade()}'
    
    def __calculate_mean_grade(self):
        all_grades = []
        for grades_by_courses in self.grades.values():
            for grade in grades_by_courses:
                all_grades.append(grade)

        return round(sum(all_grades) / len(all_grades), 1)
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.__calculate_mean_grade() < other.__calculate_mean_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')
            return
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
def course_mean_grade_students(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]

    mean_grade = round(sum(all_grades) / len(all_grades), 1)
    print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {course}: {mean_grade}')
    return mean_grade   

def course_mean_grade_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]

    mean_grade = round(sum(all_grades) / len(all_grades), 1)
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {mean_grade}')
    return mean_grade   


student_1 = Student('Ivan', 'Petrov', 'male')
student_2 = Student('Maria', 'Pivovarova', 'female')
lecturer_1 = Lecturer('Valentin', 'Nikiforov')
lecturer_2 = Lecturer('Inna', 'Timofeeva')
reviewer_1 = Reviewer('Konstantin', 'Denisov')
reviewer_2 = Reviewer('Alevtina', 'Mogaeva')

lecturer_1.courses_attached += ['Python', 'English']
lecturer_2.courses_attached += ['Git', 'Python', 'CSS']
reviewer_1.courses_attached += ['Python', 'CSS']
reviewer_2.courses_attached += ['Git', 'English']
student_1.courses_in_progress += ['Python', 'CSS', 'Git', 'English']
student_2.courses_in_progress += ['Python', 'CSS', 'Git', 'English']

student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'English', 7)
student_1.rate_lecture(lecturer_2, 'Git', 6)
student_1.rate_lecture(lecturer_2, 'CSS', 10)
student_1.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_1, 'Python', 7)
student_2.rate_lecture(lecturer_1, 'English', 8)
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'CSS', 6)
student_2.rate_lecture(lecturer_2, 'Python', 6)

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_1, 'CSS', 8)
reviewer_1.rate_hw(student_2, 'CSS', 9)
reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_1, 'English', 8)
reviewer_2.rate_hw(student_2, 'English', 8)

print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()

course_mean_grade_students([student_1, student_2], 'Python')
course_mean_grade_lecturers([lecturer_1, lecturer_2], 'Python')
course_mean_grade_students([student_1, student_2], 'CSS')
course_mean_grade_lecturers([lecturer_1, lecturer_2], 'CSS')
print()

student_1.add_courses('Python')
student_2.add_courses('Python')
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
print()

print(student_1)
print()

print(student_1 < student_2)
print(lecturer_1 < lecturer_2)

    
