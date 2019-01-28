import json
import random


class Question(object):
    def __init__(self, grade, question, answer, *choices):
        self.grade = grade
        self.question = question
        self.choises = choices
        self.correct_answer = answer

    def answer(self, choice):
        return self.correct_answer == choice


class Quiz(object):
    def __init__(self):
        self.grade = 0
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        self.grade += 1

    def solve(self, student):
        for question in self.questions:
            if question.answer(random.choice(range(4))):
                student.total_grade += 1


class Class(object):
    def __init__(self, field='Physics'):
        self.students = []
        self.field = field

    def add_student(self, student):
        self.students.append(student)


class Person(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Teacher(Person):
    def __init__(self, name, lastname):
        super(Teacher, self).__init__(name,lastname)
        self.classes = []
        self.quizzes = []

    def add_class(self, cls):
        self.classes.append(cls)

    def get_class(self,student_name, student_lastname):
        for c in self.classes:
            for student in c.students:
                if student.name == student_name and student.lastname == student_lastname:
                    return c

    def get_student(self, name, lastname):
        for c in self.classes:
            for student in c.students:
                if student.name == name and student.lastname == lastname:
                    return student

    def add_student_in_class(self,class_field, student):
        for c in self.classes:
            if c.field == class_field:
                c.add_student(student)

    def load_quiz_from_file(self):
        quiz = Quiz()
        with open('questions.json', 'r') as f:
            data = json.load(f)
            for questions in data['games']:
                for question in questions['questions']:
                    q = Question(10,question['question'],question['correct'],*question['content'])
                    quiz.add_question(q)
        self.quizzes.append(quiz)

    def assign_quiz_to_student(self,student):
        for cls in self.classes:
            for st in cls.students:
                if st == student:
                    st.assign_quiz(random.choice(self.quizzes))
                    break

    def calculate_grade_for(self, student):
        return student.total


class Student(Person):
    def __init__(self, name, lastname):
        super(Student,self).__init__(name,lastname)
        self.quizzes = []
        self._total_grade = 0

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.lastname == other.lastname
        return False

    def assign_quiz(self, qz):
        self.quizzes.append(qz)

    def solve_quiz(self):
        for quiz in self.quizzes:
            quiz.solve(self)

    @property
    def total(self):
        num_of_questions = 0
        for quiz in self.quizzes:
            num_of_questions += quiz.grade
        if self._total_grade == 0:
            return None
        return round(100 * float(self._total_grade)/float(num_of_questions),2)

    @property
    def total_grade(self):
        return self._total_grade

    @total_grade.setter
    def total_grade(self, val):
        self._total_grade = val

# teacher = Teacher("White", "Queen")
#
# student1 = Student("Peter", "Parker")
# student2 = Student("Marty", "McFly")
# student3 = Student("Gorge", "Wilson")
#
# pysics_class = Class()
# # pysics_class.add_student(student1)
# # pysics_class.add_student(student2)
# # pysics_class.add_student(student3)
# #
#
# teacher.add_class(pysics_class)
# teacher.add_student_in_class("Physics", student1)
# teacher.load_quiz_from_file()
# teacher.assign_quiz_to_student(student2)
# student2.solve_quiz()
#
# t = teacher.calculate_grade_for(student2)
