# dict is inherited form collection.abc.Mapping
from collections.abc import Mapping
dict_one = {}
print(isinstance(dict_one, Mapping))

# creating dict:
dict_1 = dict(one=1, two=2)
dict_2 = {"one": 1, "two": 2}
dict_3 = dict(zip(["one", "two"], [1, 2]))
dict_4 = dict([("one", 1), ("two", 2)])
dict_5 = dict({"one": 1, "two": 2})
print(dict_1 == dict_2 == dict_3 == dict_4 == dict_5)


# dict comprehensions
names_ages = [("name1", 1), ("name2", 2)]
dict_name_ages = {name: age for name, age in names_ages}
print(dict_name_ages)
dict_age_name = {age: name.upper() for name, age in names_ages}
print(dict_age_name)
