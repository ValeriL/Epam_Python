from homework6.task2 import instances_counter


def test_instances_are_counted():
    @instances_counter
    class Cls:
        pass

    Cls()

    assert Cls.instances_counter == 1


def test_get_created_instances():
    @instances_counter
    class Cls:
        pass

    Cls()

    assert Cls.get_created_instances() == 1


def test_reset_instances_counter():
    @instances_counter
    class Cls:
        pass

    Cls()

    assert Cls.reset_instances_counter() == 1
    assert Cls.get_created_instances() == 0
