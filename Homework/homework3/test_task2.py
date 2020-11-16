from homework3.task2 import slow_calculate, speed_up_calculate


def test_speed_up_calculate():
    max_val = 20
    fast_func_result = speed_up_calculate(max_val)
    slow_func_result = list(map(slow_calculate, range(0, max_val)))

    assert fast_func_result == slow_func_result
