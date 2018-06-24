class DictKeyStr(dict):
    """dictionary excepts the key as integer or string"""

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError("The key '%s is not in dictionary" % key)
        return self[str(key)]

    # override get method to set default name as None
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        # return key in self.keys() or str(key) in self.keys()
        return True if item in self.keys() else str(item) in self.keys()


if __name__ == "__main__":
    dict_test = DictKeyStr()
    dict_test[1] = 1
    dict_test["2"] = 2
    print(dict_test[2])
    print(2 in dict_test)