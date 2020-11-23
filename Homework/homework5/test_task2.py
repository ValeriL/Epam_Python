from homework5.task2 import print_result


def test_decorator_save_doc_and_name_function_info():
    @print_result
    def f():
        """Any doc information."""
        pass

    assert f.__name__ == "f"
    assert f.__doc__ == "Any doc information."


def test_addition_of_original_func_attribute():
    def f():
        """Any doc information."""
        pass

    f_decorated = print_result(f)

    assert f_decorated.__original_func == f


def test_decorated_function_print_result_of_original_funciton(capsys):
    @print_result
    def f(a):
        """Any doc information."""
        return a

    f(5)
    captured = capsys.readouterr()

    assert captured.out == "5\n"
