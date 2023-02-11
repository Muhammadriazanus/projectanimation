Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
calsius=998
fahrenhite=int(1.8*calsius)+32
print(fahrenhite)
1828
fahrenhite=float(1.8*calsius)+32
print(fahrenhite)
1828.4
fahrenhite=input(1.8*calsius)+32
1796.4
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fahrenhite=input(1.8*calsius)+32
TypeError: can only concatenate str (not "int") to str
fahrenhite=input(1.8*calsius)+32
1796.4
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fahrenhite=input(1.8*calsius)+32
TypeError: can only concatenate str (not "int") to str
fahrenhite-88
1740.4
fahrenhite=88
calsius=int(0.5*fahrenhite)-32
print(calsius)
12
calsius=float(0.5*fahrenhite)-32
print(calsius)
12.0
calsius=input(0.5*fahrenhite)-32
44.0
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    calsius=input(0.5*fahrenhite)-32
TypeError: unsupported operand type(s) for -: 'str' and 'int'
price=45
discount=33
discount=33
originalprice=price*discount
print(originalprice)
1485
originalprice=int(price)*int(discount)
print(originalprice)
1485
sellprice=int(price)-int(discount)
print(sellprice)
12
print(sellprice)
