from homework3.task2 import speed_up_calculate


def test_speed_up_calculate():
    actual_result = speed_up_calculate()

    assert actual_result < 60
