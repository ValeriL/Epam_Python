class KeyValueStorage:
    def __init__(self, path):  # noqa : CCR001
        with open(path) as file:
            for line in file:
                attr, value = line.replace("\n", "").split("=")
                if attr.isdigit():
                    raise ValueError("Int cant be an attribute")
                if value.isdigit():
                    self.__dict__[attr] = int(value)
                else:
                    self.__dict__[attr] = value

    def __getitem__(self, key):
        return self.__dict__[key]
