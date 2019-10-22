for letter in "Mom":
    print(letter) #letter没有语法意义，可换成任何词
print()
for guy in ["Daniel","David","Bobby"]:
    print(guy)
    print(str(guy.upper().isupper()).upper()) #布尔算符必须转换成字符串
print("print后会发现首先按矩阵内元素排序，再按print列表排序")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)]) #利用排序顺序不同进行的矩阵行列交换

#相当于以下代码
new_matrix = []
for i in range(4):
    inter = []
    for row in matrix:
        inter.append(row[i])
    new_matrix.append(inter)
print(new_matrix)

print(list(zip(*matrix))) #注意新list以tuple组成

print()
print(range(3))
for index in range(3):
    print(index)
for index in range(1,3):
    print(index)
for index in range(1,10,3):
    print(index)

print()
guys = ["Daniel","David","Bobby"]
for index in range(len(guys)):
    print(index, guys[index])
print(guys[index])

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items(): # 提取key和value
    print(k, v)

guy_enumerate = dict(enumerate(guys)) #将iterate结果变成dict
print((guy_enumerate)) # tuple和list都是逗号，元以小括号括起来
for guy in guy_enumerate:
    print(guy) #打出来的是序号

guy_enumerate2 = list(enumerate(guys,start=1)) #将iterate结果变成list，1为起始计数
print((guy_enumerate2))
for guy in guy_enumerate2:
    print(guy) #打出来的带括号

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print()
for index in range(3):
    if index == 0:
        print(00)
    elif index == 1:
        print(str(00))
    else:
        print("00")

print()
def powering(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result
print(powering(2,3))

print()
file = open("For Try8", "r") #r w a r+
print(file.readable()) # T F F T
print(file.writable()) # F T T T 没有appendable
# print(file.read()) 这几行read只能运行一个，此行代码是原始还原
# print(file.readlines()[1])
for items in file.readlines(): #此行代码是分行显示，每行之间有空格
    print(items)
file = open("For Try8","a")
print(file.write("\nCCC")) #每次运行都会多一个CCC，而且多个数字？
file = open("For Try8","w")
print(file.write("CCC")) #覆盖了
# file = open("For","w") #如果打开一个不存在的文件会自动创建然后写入
file.close()

print()
import tools
print(tools.roll_dice(10))

print()
from tools import Student
student1 = Student("Jim", "Business", 3.1)
print(student1.name)
print(student1.honor())

print()
from tools import parrot
parrot(1000)                                          # 1 positional argument
print()
parrot(voltage=1000)                                  # 1 keyword argument
print()
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print()
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print()
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
print()
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
'''
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
'''

print()
from tools import Question
question_prompt = [
    "What color are apples?\n(a) Red\n(b) Purple",
    "What color are bananas?\n(a) Red\n(b) Yelllow",
    "What color are strawberries?\n(a) Green\n(b) Red",
]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "b"),
]
def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions)) + " correct")
run(questions)