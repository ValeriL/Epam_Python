"""
Написать декоратор instances_counter, который применяется к любому классу и добавляет ему 2 метода.

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    class ExtendClass(cls):

        __instances_counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.__instances_counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.__instances_counter

        @classmethod
        def reset_instances_counter(cls):
            try:
                return cls.__instances_counter
            finally:
                cls.__instances_counter = 0

    return ExtendClass
