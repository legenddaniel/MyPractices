# python手册/文档 很强！！！！！
noun="\n"
print("This section deals with strings, numbers, and some functions, use of \\ in the sentences like \\""n"+str(noun))
print("You can see that there's an empty line created by this \\""n")
print("Also you can type \\\" to type \" and type \\\\ to type \\ in python")
print("I learned some functions like \"upper/lower\", ""\"isupper/islower\", ""\"replace, index\", etc."+str(noun))
print("\"\\t\" means indentation")
print("使用repr()就无需这么复杂，打出来就是",
      repr("\\"), "或者开头加个r")
#定义/赋值的函数都用=，数学意义的用==

print()
print('''
yyy
nnn
''')

print(r"C:\\Windows\name"r"\"") #\\和\n会作用

print('{1} and {0}'.format('spam', 'eggs')) #等于以下代码
a = 'eggs'
b = 'spam'
print(a, 'and', b, end="") #输出结果至同一行，以""里内容分隔，但最后一行代码也会把下一段代码拽上来
print(a + 'and' + b)

print()
print((5 * True + 2 ** False) % (False + 4))
print()

print([ (x, y) for x in range(10) if x % 3 #( == True 即 != 0)
        if x > 3 for y in range(10) if y > 7 if y != 8 ])

hello = 'hello, world\n'
hellos = str(hello)
helloss = repr(hello) #面向用户一般用str，除非需要打出引号，debug用repr
print(hellos) #\n生效
print(helloss) #\n作为字符串

my_name = "Siyuan Zuo lalalalala"
another_name = "Siyuan Zuo"
my_age = "25"
print(set(my_name)) # 多个集合运算，a+b=并集，a-b=只在a中有的，a*b=交集，a^b=只有其中一个有的
'''set就是只有key没有value的dict，无序不重复，可参考浏览器收藏'''
# 集合会自动消除重复的元素

print()
y = {x: x ** 2 for x in (2, 4, 6)} #也可通过dict创建字典: dict(a = 1, b = 2, etc.)
print(y)

print()
print("I\"m "+my_age+",")
print("It's " , str(my_name.isupper()).upper() , " to print my name in lower case")
print(my_name.lower().isupper())
print(len(my_name))
print(my_name[14])
print(my_name[-14])
print(my_name.index("a"))
print(my_name.index("Zuo"))
print(my_name.replace("lalala","balabababa"))
print(3/5,5%3)
print(str(my_name))

print()
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:5}')

print()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!a}.') #!a = ascii()
print(f'My hovercraft is full of {animals!s}.') #!s = str() = 什么都不写
print(f'My hovercraft is full of {animals!r}.') #!r = repr()
print()

from math import *
import math
print(f'The value of pi is approximately {math.pi:.3f}.') #f = 小数点后位数，g = 有效数字位数

number=-3
print(abs(number)+number+pow((number+1),(number+1)))
print("Here is a #: " + str(round(2.5))) #理论应该是3,python的bug？
print(round(3.5))
print(round(2.545,1))
print("Here is a #: " + str(round(2.545,2))) #又一个
print(floor(3.5))
print(ceil(3.5))
print(sqrt(4.5))
print("\"")
print("\n")
print("g\a")
print("g/A")
print("")

print()
try:
    print(my_name.index("t"))
except ValueError as err:
    print('Error: {0}'.format(err))
print()

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks, ',', e.tricks)

print()
from collections import Counter #计数器，以字典形式打印
Var = "1987262819009787718192084951"
print (Counter(Var))

name=input("Enter your name ")
age=input("Enter your age ")
print("Hi "+name+"! Are you "+age+" years old or above?")
