
import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0


newlist = list(filter(is_sqr, range(1, 101)))
print(newlist)