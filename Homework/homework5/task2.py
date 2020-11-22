"""
Написать декоратор.

Который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
from typing import Callable


def wraps(wrapped: Callable) -> Callable:
    def decorator(wrapper):
        wrapper.__name__ = wrapped.__name__
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__original_func = wrapped
        return wrapper

    return decorator


def print_result(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function."""
        result = func(*args, **kwargs)
        print(result)  # noqa
        return result

    return wrapper


# All above was in the task file
@print_result
def custom_sum(*args):
    """Sum any objects which have __add___."""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)  # noqa
    print(custom_sum.__name__)  # noqa
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
