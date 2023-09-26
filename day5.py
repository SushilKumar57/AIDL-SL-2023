
import day5_pack.test as test
test.hi()

import day5_pack
day5_pack.test.hi()
day5_pack.xyz()

from day5_pack import test
test.hi()

from day5_pack import xyz
xyz()

# # import day5_lib
# # from day5_lib import multiplier
# # import day5_lib as d5
# from day5_lib import multiplier as mt, data

# values = input('Enter values seperated by comma(,):')
# values = [eval(val) for val in values.split(',')]
# print(values)
# # print(day5_lib.multiplier(*values))
# # print(multiplier(*values))
# # print(d5.multiplier(*values))
# print(mt(*values))
# print(data * 3)