from collections import defaultdict

from homework6.task1 import DeadlineError, Homework, HomeworkResult, Student, Teacher

import pytest

student = Student("Roman", "Petrov")
teacher = Teacher("Daniil", "Shadrin")


def test_homework_result_raise_typeerror():
    homework_str = "homework"
    with pytest.raises(TypeError, match="You gave not a Homework object"):
        HomeworkResult(student, homework_str, "solution")


def test_do_homework_for_expired_homework():
    expired_homework = Homework("Any homework", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(expired_homework, "Any solution")


def test_check_incorrect_homework():
    homework = Homework("Any homework", 1)
    incorrect_result = student.do_homework(homework, "<5")

    assert teacher.check_homework(incorrect_result) is False
    assert homework not in Teacher.homework_done


def test_check_correct_homework():
    Teacher.homework_done.clear()

    homework = Homework("HW", 1)
    correct_result = student.do_homework(homework, "More than 5 symbols.")

    assert teacher.check_homework(correct_result) is True
    assert Teacher.homework_done == defaultdict(list, {homework: [correct_result]})


def test_check_homework_is_without_addition_repeated_solution_into_homework_done_dict():
    Teacher.homework_done.clear()

    teacher1 = Teacher("Daniil", "Shadrin")
    teacher2 = Teacher("Aleksandr", "Smetanin")

    homework = teacher1.create_homework("HW", 1)
    result = student.do_homework(homework, "Homework is done.")

    teacher1.check_homework(result)
    teacher2.check_homework(result)

    assert Teacher.homework_done == defaultdict(list, {homework: [result]})


def test_reset_homework_results_for_given_homework():
    Teacher.homework_done.clear()

    homework1 = teacher.create_homework("HW1", 1)
    homework2 = teacher.create_homework("HW2", 1)

    result1 = student.do_homework(homework1, "Any solution.")
    result2 = student.do_homework(homework2, "Any solution.")

    teacher.check_homework(result1)
    teacher.check_homework(result2)

    Teacher.reset_results(homework2)

    assert Teacher.homework_done == defaultdict(list, {homework1: [result1]})


def test_reset_all_homework_results():
    Teacher.homework_done.clear()

    homework1 = teacher.create_homework("HW1", 1)
    homework2 = teacher.create_homework("HW2", 1)

    result1 = student.do_homework(homework1, "Any solution.")
    result2 = student.do_homework(homework2, "Any solution.")

    teacher.check_homework(result1)
    teacher.check_homework(result2)

    Teacher.reset_results()

    assert not Teacher.homework_done


def test_reset_homework_results_raise_typeerror():
    homework_str = "homework"
    with pytest.raises(TypeError, match="You gave not a Homework object"):
        Teacher.reset_results(homework_str)
