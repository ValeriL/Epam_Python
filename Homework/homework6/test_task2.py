from homework6.task2 import instances_counter


def test_get_created_instances():
    @instances_counter
    class Cls:
        instances_counter = 42

    Cls()

    assert Cls.get_created_instances() == 1


def test_reset_instances_counter():
    @instances_counter
    class Cls:
        instances_counter = 42

    Cls()

    assert Cls.reset_instances_counter() == 1
    assert Cls.get_created_instances() == 0
