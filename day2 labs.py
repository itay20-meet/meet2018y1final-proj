Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> my_age=15
>>> print('i am' + my_age + 'years old')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print('i am' + my_age + 'years old')
TypeError: must be str, not int
>>> print9'i am' + 'my age' + 'years old')
SyntaxError: invalid syntax
>>> print('i am' + 'my age' + 'years old')
i ammy ageyears old
>>> print('i am' + 'my_age' + 'years old')
i ammy_ageyears old
>>> 'my_age'=15
SyntaxError: can't assign to literal
>>> my_age=15
>>> print('i am' + my_age + 'years old')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('i am' + my_age + 'years old')
TypeError: must be str, not int
>>> print('i am' +str(my_age) + 'years old')
i am15years old
>>> my_age = 15
>>> str(my_age)
'15'
>>> print('i am' +str (my_age) + 'years old')
i am15years old
>>> print('i am ' + str (my_age) + 'years old')
i am 15years old
>>> print('i am ' + str (my_age) + 'years old ')
i am 15years old 
>>> print('i am ' + str (my_age) + ' years old')
i am 15 years old
>>> score=1
>>> count
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    count
NameError: name 'count' is not defined
>>> total=score+(count*2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    total=score+(count*2)
NameError: name 'count' is not defined
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> print('total')
total
>>> 
