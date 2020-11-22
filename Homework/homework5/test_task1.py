from homework5.task1 import Homework, Student, Teacher


def test_homework_is_active_for_not_expired_homework():
    hw_text, days = "Any homework", 3
    not_expired_homework = Homework(hw_text, days)

    assert not_expired_homework.is_active()


def test_do_homework_for_expired_homework(capsys):
    hw_text, days = "Any homework", 0
    expired_homework = Homework(hw_text, days)

    first_name, last_name = "Roman", "Petrov"
    student = Student(first_name, last_name)

    student.do_homework(expired_homework)
    captured = capsys.readouterr()

    assert captured.out == "You're late\n"
    assert student.do_homework(expired_homework) is None


def test_do_homework_for_not_expired_homework():
    hw_text, days = "Any homework", 3
    not_expired_homework = Homework(hw_text, days)

    first_name, last_name = "Roman", "Petrov"
    student = Student(first_name, last_name)

    assert student.do_homework(not_expired_homework) == not_expired_homework


def test_create_function():
    first_name, last_name = "Roman", "Petrov"
    teacher = Teacher(first_name, last_name)

    hw_text, days = "Any homework", 3
    created_homework = teacher.create_homework(hw_text, days)

    assert isinstance(created_homework, Homework)
    assert created_homework.text == hw_text
