from behave import given, then, when
import quiz


@given("There is a teacher {name_lastname}")
def declare_teacher(context, name_lastname):
    name, lastname = name_lastname.split(' ')
    context.teacher = quiz.Teacher(name,lastname)


@given("There is a {field} class that she teaches")
def declare_class(context, field):
    context.teacher.add_class(quiz.Class(field))


@given("There is a student {name_lastname} in {field} class")
def declare_student(context, name_lastname, field):
    name, lastname = name_lastname.split(' ')
    context.teacher.add_student_in_class(field, quiz.Student(name,lastname))


@given("There is another student {name_lastname} in {field} class")
def declare_student(context, name_lastname, field):
    name, lastname = name_lastname.split(' ')
    context.teacher.add_student_in_class(field, quiz.Student(name, lastname))


@when("Teacher getting quiz '{quiz}'")
def get_quiz(context, quiz):
    if quiz == 'from json':
        context.teacher.load_quiz_from_file()

@when("Teacher assigns quiz to student {name_lastname}")
def assign_quiz(context, name_lastname):
    name, lastname = name_lastname.split(' ')
    context.teacher.assign_quiz_to_student(context.teacher.get_student(name, lastname))

@when("Student {name_lastname} solves the quiz")
def solve_quiz(context, name_lastname):
    name, lastname = name_lastname.split(' ')
    student = context.teacher.get_student(name,lastname)
    student.solve_quiz()

@then("Teacher gets the result for student {name_lastname}")
def i_should_see_text(context, name_lastname):
    name, lastname = name_lastname.split(' ')
    res = context.teacher.calculate_grade_for(context.teacher.get_student(name,lastname))
    assert res != None
