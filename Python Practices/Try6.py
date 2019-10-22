def cube(num):
    return num*num*num
    print("1")
print(cube(3))
print()

is_male = True
is_tall = False
if is_male or is_tall: #if等之后要加冒号
    print("U r a male or tall or both")
elif is_male and not is_tall:
    print("U r a male but not tall")
else:
    print("U r neither a male nor tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("U r a male and tall")
elif is_male and not is_tall:
    print("U r a male but not tall")
else:
    print("U r either not a male or tall")

print()
def max_num(num1,num2,num3): #还可以用于string的比较
    if num1>=num2 and num1>=num3: #"!="是≠的意思，==是相等，一个等号用于赋值
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3
print(max_num(3,4,5))
print(max(3,4,5)) #等于现定义一个max函数
print()
monthconversion = { #没有def
    "Jan": "January", #冒号之后的字符串加逗号
    "Feb": "February",
    "Mar": "March",
}
print(monthconversion["Mar"])
print(monthconversion.get("Mar"))
print(monthconversion.get("Apr"))
print(monthconversion.get("Apr","Not Here"))

print()
i = 1
while i <= 10: # likewise “while” 也要加冒号，此类引导词都是
    print(i)
    i += 1
print("Loop End")
print()

# 若敲入以下代码会无限循环直至死机
# i = 1
# while i <= 10:
    # print(i)
    # i -= 1, i *= 1, i /= 1
# print("Loop End")

print("基础版猜词")
secret = "deer"
guess = ""
i = 0
while guess != secret and i < 3:
    guess = input("Enter Guess: ")
    i += 1
if i < 3:
    print("Correct")
else:
    print("Chance is up")

print("进阶版猜词")
secret = "deer"
guess = ""
i = 0
if guess != secret and i == 0: #用while也可以
    guess = input("Enter Guess: ")
    i += 1
if guess != secret and i == 1:
    guess = input("Enter Guess Again: ")
    i += 1
if guess != secret and i == 2:
    guess = input("Last Chance: ")
    i += 1
if guess == secret:
    print("Correct")
else:
    print("Chance is up")