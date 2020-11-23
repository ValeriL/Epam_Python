from homework5.task1 import Homework, Student, Teacher


def test_homework_is_active_for_not_expired_homework():
    not_expired_homework = Homework("Any homework", 3)

    assert not_expired_homework.is_active()


def test_do_homework_for_expired_homework(capsys):
    expired_homework = Homework("Any homework", 0)
    student = Student("Roman", "Petrov")

    student.do_homework(expired_homework)
    captured = capsys.readouterr()

    assert captured.out == "You're late\n"
    assert student.do_homework(expired_homework) is None


def test_do_homework_for_not_expired_homework(capsys):
    not_expired_homework = Homework("Any homework", 3)
    student = Student("Roman", "Petrov")

    student.do_homework(not_expired_homework)
    captured = capsys.readouterr()

    assert not captured.out
    assert student.do_homework(not_expired_homework) == not_expired_homework


def test_create_function():
    teacher = Teacher("Roman", "Petrov")
    created_homework = teacher.create_homework("Any homework", 3)

    assert isinstance(created_homework, Homework)
    assert created_homework.text == "Any homework"
