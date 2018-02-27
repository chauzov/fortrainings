# task: try to make variable
# a = range(10000000)
# a = range(100000000)
# a = range(1000000000)
# a = range(10000000000)
# why you see exception, how to fix it
# note: try to find size of object (without using pympler.asizeof)

# a>>> import sys
# >>> sys.getsizeof
# <built-in function getsizeof>
# a = xrange(10000000)
# >>> sys.getsizeof(a)
# 40
# >>> a = range(1000000)
# >>> sys.getsizeof(a)
# 8000072
