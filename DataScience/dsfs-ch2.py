"""Data Science from Scratch Chapter 2: A Crash Course in Python"""

from collections import defaultdict, Counter
import random, re

# defaultdict

"""count words in document, if word is in dict, increase count by one, else
add the word to the dict"""

document = ['the', 'a', 'cat', 'dog', 'the', 'a', 'car', 'dog', 'if', 'the']

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

"""count words in document, try increase count by one, except if a KeyError is
raised, then add the word to the dict"""
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

"""count words in document, use built-in get method which handles missing
keys well"""

word_counts = {}
for word in document:
    # add the word if it isn't in the dict with get method
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

"""use defaultdict to add a default value to keys. it will add a key that
it doesn't contain"""

word_counts = defaultdict(int)      # int() produces 0
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)         # list() produces an empty list
dd_list[2].append(1)                # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)         # dict() produces an empty dict
dd_dit["Joel"]["City"] = "Seattle"  # { "Joel": { 'City': "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                   # now dd_pair contains {2: [0, 1]}

# Counter
"""Counter turns a sequence of values into a defaultdict(int)-like object
mapping keys to counts, which is good for making histograms"""
c = Counter([0, 1, 2, 0])           # c is (basically){ 0 : 2, 1 : 1, 2 : 1}
word_counts = Counter(document)
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print word, count

# Sets

s = set()
s.add(1)    # s is now { 1 }
s.add(2)    # s is now { 1, 2 }
s.add(2)    # s is still { 1, 2 }
x = len(s)  # equals 2
y = 2 in s  # equals True
z = 3 in s  #equals False

""" Sets will be used because in is a fast operation for sets and to find
the distinct items in a collection """

# Control Flow

for x in range(10):
    print x, "is less than 10"

# Truthiness

x = None
print x == None     # prints True, but is not Pythonic
print x is None     # prints True, and is Pythonic

""" The following are all Falsy: False, None, [] (empty list), {} (empty dict), "", set(), 0, 0.0 """

all([True, 1, { 3 }])       # True
all([True, 1, {}])          # False, {} is falsy
any([True, 1, {}])          # True, True is truthy
all([])                     # True, no falsy elements in the list
any([])                     # False, no truthy elements in the list

# Sorting

x = [4,1,2,3]
y = sorted(x)       # is [1,2,3,4], x is unchanged
x.sort()            # now x is [1,2,3,4]

# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True)  # is [-4,3,-2,1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(), 
            key=lambda (word, count): count,
            reverse=True)

# List Comprehensions

even_numbers = [x for x in range(5) if x % 2 == 0]      # [0, 2, 4]
squares      = [x * x for x in range(5)]                # [0, 1, 4, 9, 16]
even_squares = [x * x for x in range(5) if x % 2 == 0]  # [0, 4, 16]

square_dict = {x : x * x for x in range(5)}             # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set = {x * x for x in [-1, 1]}                   # { 1 }

zeroes = [0 for _ in even_numbers]      # has the same length as even_numbers
pairs = [(x, y)
          for x in range(10)
          for y in range(10)]   # 100 pairs (0,0), (0,1) ... (9,8), (9,9)

increasing_pairs = [(x, y)                          # only pairs with x < y
                    for x in range(10)              # range(lo, hi) equals
                    for y in range(x + 1, 10)]      # [lo, lo + 1, ..., hi - 1]

# Generators and Iterators

def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10):
    do_something_with(i)

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
    yield n
    n += 1

# the downside of a generator is that you can only iterate over it once

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# Randomness

four_uniform_randoms = [random.random() for _ in range(4)]

# random.random() produces numbers uniformly between 0 and 1
# it's the random function we'll use the most often

# if you want reproducible results, set an internal state with
# random.seed(#)

random.seed(10)         # set the seed to 10
print random.random()   # 0.57140259469
random.seed(10)         # reset the seed to 10
print random.random()   # 0.57140259469 again

random.randrange(10)    # choose randomly from range(10) = [0, 1, ... ,9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = range(10)
random.shuffle(up_to_ten)   # randomly reorder elements of up_to_ten
print up_to_ten             # [2, 5, 1, 9, 7, 3, 8, 6, 4, 0]
# randomly pick one element from a list:
my_best_friend = random.choice(['Alice', 'Bob', 'Charlie'])
# randomly choose a sample of elements without replacement:
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]
# randomly choose a sample with replacement:
four_with_replacement = [random.choice(range(10))
                        for _ in range(4)]          # [9, 4, 4, 2]

# Regular Expressions

print all([                                     # all of these are True, because
    not re.match("a", "cat"),                   # * 'cat' doesn't start with 'a'
    re.search("a", "cat"),                      # * 'cat' has an 'a' in it
    not re.search("c", "dog"),                  # * 'dog' doesn't have a 'c' in it
    3 == len(re.split("[ab]", "carbs")),        # * split on a or b to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2")      # * replace digits with dashes
    ]) # prints True

# Enumerate

# Python's enumerate produces tuples (index, element):

for i, document in enumerate(documents):
    do_something(i, document)
# if we just want the indexs:
for i, _ in enumerate(documents): do_something(i)   # Pythonic

# Zip and Argument Unpacking

# zip transforms multiple lists into a single list of tuples:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)           # is [('a', 1), ('b', 2), ('c', 3)]

# you can unzip using:
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)          # asterisk performs unpacking

# unpacking works with any function

def add(a,b): return a + b

add(1, 2)       # returns 3
add([1, 2])     # TypeError!
add(*[1, 2])    # returns 3

# args and kwargs

# sometimes we need a function that takes arbitrary arguments:

def magic(*args, **kwargs):
    print "unnamed args:", args
    print "keyward args:", kwargs

    magic(1, 2, key="word", key2="word2")

    # prints
    # unnamed args: (1, 2)
    # keyword args: {'key2': 'word2', 'key': 'word'}

# when we define a function like this, args is a tuple of unnamed arguments
# kwargs is a dict of its named arguments

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
print other_way_magic(*x_y_list, **z_dict)  # 6

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

def f2(x, y): return x + y

g = doubler_correct(f2)
print g(1, 2)   # 6
 