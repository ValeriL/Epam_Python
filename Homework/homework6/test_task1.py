from collections import defaultdict

from homework6.task1 import DeadlineError, Homework, HomeworkResult, Student, Teacher

import pytest


@pytest.fixture()
def student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def homework():
    return Homework("Any homework text", 1)


def test_homework_result_raise_typeerror(student):
    homework_str = "homework"
    with pytest.raises(TypeError, match="You gave not a Homework object"):
        HomeworkResult(student, homework_str, "solution")


def test_do_homework_for_expired_homework(student):
    expired_homework = Homework("Any homework text", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(expired_homework, "More than 5 symbols solution.")


def test_check_incorrect_homework(student, teacher, homework):
    incorrect_result = student.do_homework(homework, "<5")

    assert teacher.check_homework(incorrect_result) is False
    assert homework not in Teacher.homework_done


def test_check_correct_homework(student, teacher, homework):
    Teacher.homework_done.clear()

    correct_result = student.do_homework(homework, ">5 symbols solution.")

    assert teacher.check_homework(correct_result) is True
    assert Teacher.homework_done == defaultdict(list, {homework: [correct_result]})


def test_not_add_to_homework_done_repeated_solutions(student, teacher, homework):
    Teacher.homework_done.clear()

    result = student.do_homework(homework, "Homework is done.")

    teacher.check_homework(result)
    teacher.check_homework(result)

    assert Teacher.homework_done == defaultdict(list, {homework: [result]})


def test_reset_homework_results_for_given_homework(student, teacher):
    Teacher.homework_done.clear()

    homework1 = teacher.create_homework("HW1", 1)
    homework2 = teacher.create_homework("HW2", 1)

    result1 = student.do_homework(homework1, ">5 symbols solution.")
    result2 = student.do_homework(homework2, ">5 symbols solution.")

    teacher.check_homework(result1)
    teacher.check_homework(result2)

    Teacher.reset_results(homework2)

    assert Teacher.homework_done == defaultdict(list, {homework1: [result1]})


def test_reset_all_homework_results(student, teacher):
    Teacher.homework_done.clear()

    homework1 = teacher.create_homework("HW1", 1)
    homework2 = teacher.create_homework("HW2", 1)

    result1 = student.do_homework(homework1, ">5 symbols solution.")
    result2 = student.do_homework(homework2, ">5 symbols solution.")

    teacher.check_homework(result1)
    teacher.check_homework(result2)

    Teacher.reset_results()

    assert not Teacher.homework_done


def test_reset_homework_results_raise_typeerror():
    homework_str = "homework"
    with pytest.raises(TypeError, match="You gave not a Homework object"):
        Teacher.reset_results(homework_str)
