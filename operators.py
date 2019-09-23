Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> import sys
>>> sys.max
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sys.max
AttributeError: module 'sys' has no attribute 'max'
>>> import sys
>>> sys.maxsize
2147483647
>>> sys.maxsize
2147483647
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> int 2A
SyntaxError: invalid syntax
>>> int A2
SyntaxError: invalid syntax
>>> a=23
>>> b=3
>>> a+b
26
>>> a-b
20
>>> a*b
69
>>> a%b
2
>>> a/b
7.666666666666667
>>> a//b
7
>>> a**b
12167
>>> a==b
False
>>> a!=b
True
>>> a>b
True
>>> a<b
False
>>> a>=b
True
>>> a<=b
False
>>> a and b
3
>>> a or b
23
>>> b and a
23
>>> b or a
3
>>> not(f)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    not(f)
NameError: name 'f' is not defined
>>> not(false)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    not(false)
NameError: name 'false' is not defined
>>> not(1)
False
>>> a&b
3
>>> a|b
23
>>> a^b
20
>>> a~b
SyntaxError: invalid syntax
>>> ~a
-24
>>> ~b
-4
>>> a>>b
2
>>> a<<b
184
>>> print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> a*b
69
>>> 69*a*b
4761
>>> 
