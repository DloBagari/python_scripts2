"""using MappingProxyType provide a view of a dictionary, with this view we can not change the data in original dict"""

from types import MappingProxyType

dict_1_proxy = MappingProxyType({1: 1, 2: 2})
print(dict_1_proxy)
# dict_1_proxy[1] = 2 # raise a typeError : does not support item assignment


