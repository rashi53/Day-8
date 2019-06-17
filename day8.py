Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/python/Python37-32/day8/1.py ==================
enter a number:4
enter a number:2
4 / 2 = 2.0
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/1.py ==================
enter a number:5
enter a number:0
division by zero not allowed
>>> 
================== RESTART: C:/python/Python37-32/day8/1.py ==================
enter a number:5
enter a number:0
division by zero not allowed
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/2.py ==================
No module named 'abc1'
enter a number:5
enter a number:2
5 / 2 = 2.5
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/3.py ==================
enter a number:5
enter a number:4
5 / 4 = 1.25
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/3.py ==================
enter a number:5
enter a number:0
division by zero not allowed
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/4.py ==================
enter a number:c
invalid literal for int() with base 10: 'c'
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/4.py ==================
enter a number:5
enter a number:0
division by zero not allowed
thank u
>>> 
================== RESTART: C:/python/Python37-32/day8/5.py ==================
enter a number:5
enter a number:2
5 / 2 = 2.5
Resource deallocated
>>> 
================== RESTART: C:/python/Python37-32/day8/5.py ==================
enter a number:6
enter a number:0
division by zero not allowed
Resource deallocated
>>> 
================== RESTART: C:/python/Python37-32/day8/6.py ==================
enter a number:5
enter a number:4
5 / 4 = 1.25
Resource deallocated
visit vips again
>>> 
================== RESTART: C:/python/Python37-32/day8/6.py ==================
enter a number:3a
Traceback (most recent call last):
  File "C:/python/Python37-32/day8/6.py", line 2, in <module>
    num1=int(input("enter a number:"))
ValueError: invalid literal for int() with base 10: '3a'
>>> 
================== RESTART: C:/python/Python37-32/day8/6.py ==================
enter a number:3a
enter a number:4
division by zero not allowed or strings are not allowed.please input only integer
Resource deallocated
visit vips again
>>> 
================== RESTART: C:/python/Python37-32/day8/6.py ==================
enter a number:5
enter a number:0
division by zero not allowed or strings are not allowed.please input only integer
Resource deallocated
visit vips again
>>> 
================== RESTART: C:/python/Python37-32/day8/6.py ==================
enter a number:4s
enter a number:0
division by zero not allowed or strings are not allowed.                please input only integer
Resource deallocated
visit vips again
>>> 
================== RESTART: C:/python/Python37-32/day8/7.py ==================
[Errno 2] No such file or directory: 'c:\\python\\student.txt'
error: can't file or read data
Traceback (most recent call last):
  File "C:/python/Python37-32/day8/7.py", line 8, in <module>
    f.close()
NameError: name 'f' is not defined
>>> 
================== RESTART: C:/python/Python37-32/day8/7.py ==================
not writable
error: can't file or read data
thanks
>>> 
================== RESTART: C:/python/Python37-32/day8/8.py ==================
not writable
error: can't file or read data
thanks
>>> x=set("A Python Tutorial")
>>> print(x)
{'T', 'h', 'y', 't', 'o', 'A', 'u', 'l', 'a', 'r', 'i', 'n', 'P', ' '}
>>> print(type(x))
<class 'set'>
>>> x=set(["Perl","python","java"])
>>> print(x)
{'python', 'java', 'Perl'}
>>> cities=set(("Perl","Lyon","London","Berlin","paris","birmingham"))
>>> print(cities)
{'Lyon', 'London', 'Berlin', 'Perl', 'birmingham', 'paris'}
>>> cities=set(["Frankfart","Basel","Freiburg"])
>>> print(cities)
{'Frankfart', 'Basel', 'Freiburg'}
>>> cities=set(["Frankfart","Basel","Freiburg"])
>>> cities=frozenset(["Frankfart","Basel","Freiburg"])
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cities.add("Strasbourg")
AttributeError: 'frozenset' object has no attribute 'add'
>>> adjectives={"cheap","expensive","inexpensive","economical"}
>>> print(adjectives)
{'cheap', 'economical', 'inexpensive', 'expensive'}
>>> more_cities={"Delhi","mumbai","madsour"}
>>> cities_backup=more_cities.copy()
>>> more_cities.clear()
>>> print(cities_backup)
{'mumbai', 'madsour', 'Delhi'}
>>> more_cities={"Delhi","mumbai","madsour"}
>>> cities_backup=more_cities
>>> more_cities.clear()
>>> print(cities_backup)
set()
>>> x={"a","b","c","d","e"}
>>> y={"b","c"}
>>> z={"c","d"}
>>> print(x.difference(y))
{'e', 'd', 'a'}
>>> print(x.difference(y).difference(y))
{'e', 'd', 'a'}
>>> print(x-y)
{'e', 'd', 'a'}
>>> print(x-y-z)
{'e', 'a'}
>>> x={"a","b","c","d","e"}
>>> y={"b","c"}
>>> x.difference_update(y)
>>> print(x)
{'a', 'e', 'd'}
>>> x={"a","b","c","d","e"}
>>> y={"b","c"}
>>> x=x-y
>>> print(x)
{'e', 'd', 'a'}
>>> x={"a","b","c","d","e"}
>>> x.discard("a")
>>> x
{'c', 'b', 'e', 'd'}
>>> x.discard("z")
>>> x
{'c', 'b', 'e', 'd'}
>>> x={"a","b","c","d","e"}
>>> x.remove("a")
>>> x
{'c', 'b', 'e', 'd'}
>>> x.remove("z")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x.remove("z")
KeyError: 'z'
>>> x={"a","b","c","d","e"}
>>> y={"c","d","e","f","g"}
>>> print(x.intersection(y))
{'e', 'd', 'c'}
>>> print(x&y)
{'e', 'd', 'c'}
>>> z={"p","q"}
>>> print(x.isdisjoint("z"))
True
>>> print(x.isdisjoint("y"))
True
>>> print(x.isdisjoint(y))
False
>>> x={"a","b","c","d","e"}
>>> y={"c","d"}
>>> print(x.issubset(y))
False
>>> print(y.issubset(x))
True
>>> print(x-y)
{'e', 'b', 'a'}
>>> print(x<y)
False
>>> print(y<x)
True
>>> print(x<x)
False
>>> print(x<=x)
True
>>> x={"a","b","c","d","e"}
>>> y={"c","d"}
>>> print(x.issuperset(y))
True
>>> print(x>y)
True
>>> print(x>=y)
True
>>> print(x>=x)
True
>>> print(x>x)
False
>>> print(x.issuperset(x))
True
>>> x={"a","b","c","d","e"}
>>> print(x.pop())
c
>>> print(x.pop())
b
>>> y={}
>>> print(y.pop())
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(y.pop())
TypeError: pop expected at least 1 arguments, got 0
>>> 
================== RESTART: C:/python/Python37-32/day8/9.py ==================
union of E and N is  {1, 2, 3, 4, 6, 8}
intersection of E and N is  {2, 4}
difference of N and E is  {1, 3}
defference of E and N is  {8, 6}
symetric difference of E and N is  {1, 3, 6, 8}
Traceback (most recent call last):
  File "C:/python/Python37-32/day8/9.py", line 9, in <module>
    print("symetric difference of N and E is ",(E-N)(N-E))
TypeError: 'set' object is not callable
>>> 
================== RESTART: C:/python/Python37-32/day8/9.py ==================
union of E and N is  {1, 2, 3, 4, 6, 8}
intersection of E and N is  {2, 4}
difference of N and E is  {1, 3}
defference of E and N is  {8, 6}
symetric difference of E and N is  {1, 3, 6, 8}
symetric difference of N and E is  {8, 1, 3, 6}
>>> 
