import collections


class DictKeyStr2(collections.UserDict):
    """dictionary extends UserDict which stores keys as string"""
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError("key: %s is not in dictionary" % key)
        return self[str(key)]

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, item):
        return str(key) in self.data


if __name__ == "__main__":
    dict_1 = DictKeyStr2()
    dict_1[1] = 1
    print(dict_1["1"])
    print(dict_1[1])
