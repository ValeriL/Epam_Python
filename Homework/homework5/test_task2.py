from homework5.task2 import print_result


def test_decorator_save_doc_and_name_function_info():
    @print_result
    def f():
        """Any doc information."""
        pass

    assert f.__name__ == "f"
    assert f.__doc__ == "Any doc information."


def test_addition_of_original_func_attribute():
    @print_result
    def f(a=5):
        """Any doc information."""
        return a

    not_original_func = f.__original_func

    assert not_original_func() == f()
