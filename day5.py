Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = ['she','sells','sea','shells','by','the','sea','shore']
>>> b = "selfish shelfish"
>>> c = [1,1,2,3,5,8,13]
>>> b[3:4]
'f'
>>> c[5]
8
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[2]
'sea'
>>> a[2:4]
['sea', 'shells']
>>> c[1] + c[2]
3
>>> a*3
['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
>>> 'by' in a
True
>>> 'self' in b
True
>>> dog = 'dalmatian'
>>> len(dog)
9
>>> dogs = [dog,'poodle','boxer']
>>> len(dogs)
3
>>> len[dogs]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    len[dogs]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> one  = [1,2,3,4]
>>> two = [7,6,5,4]
>>> three = ['y1', 'friends','fun']
>>> print (one + two)
[1, 2, 3, 4, 7, 6, 5, 4]
>>> print (one[3])
4
>>> one.remove(4)
>>> print(one)
[1, 2, 3]
>>> one.oppend(4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    one.oppend(4)
AttributeError: 'list' object has no attribute 'oppend'
>>> one.append(4)
>>> print (one)
[1, 2, 3, 4]
>>> one.pop(1)
2
>>> print(one)
[1, 3, 4]
>>> four= one + three
>>> print(four)
[1, 3, 4, 'y1', 'friends', 'fun']
>>> one = [1,2,3,4]
>>> print(four)
[1, 3, 4, 'y1', 'friends', 'fun']
>>> four=[one,three]
>>> four
[[1, 2, 3, 4], ['y1', 'friends', 'fun']]
>>> one=[1,2,3]
>>> four
[[1, 2, 3, 4], ['y1', 'friends', 'fun']]
>>> a=[1,2]
>>> b=[a,a]
>>> a[1] = 3
>>> a
[1, 3]
>>> b
[[1, 3], [1, 3]]
>>> a = [1,5]
>>> a
[1, 5]
>>> b
[[1, 3], [1, 3]]
>>> one
[1, 2, 3]
>>> four
[[1, 2, 3, 4], ['y1', 'friends', 'fun']]
>>> one = [1,2,3,4]
>>> four=[one,three]
>>> one.pop[3]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    one.pop[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> one.pop(3)
4
>>> four
[[1, 2, 3], ['y1', 'friends', 'fun']]
>>> three.pop(2)
'fun'
>>> three.remove('fun')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    three.remove('fun')
ValueError: list.remove(x): x not in list
>>> 'fun' in three
False
>>> one[3] = two[0]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    one[3] = two[0]
IndexError: list assignment index out of range
>>> one[3] == two[0]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    one[3] == two[0]
IndexError: list index out of range
>>> one.sort()
>>> print(one)
[1, 2, 3]
>>> two.sort()
>>> print(two)
[4, 5, 6, 7]
>>> 
