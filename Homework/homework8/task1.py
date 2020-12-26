"""
We have a file that works as key-value storage.

Each like is represented as key and value separated by = symbol, example:
name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes.
Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
from keyword import iskeyword


class KeyValueStorage:
    def __init__(self, path):  # noqa : CCR001
        self._inner = {}

        with open(path) as file:
            for line in file:
                attr, value = line.rstrip("\n").split("=", 1)
                if not attr.isidentifier() or iskeyword(attr):
                    raise ValueError("Cant be an attribute")
                if value.isdigit():
                    value = int(value)
                self._inner[attr] = value

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __getattr__(self, key):
        return self._inner[key]
