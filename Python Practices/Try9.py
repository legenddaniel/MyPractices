from tools import Chef
mychef = Chef()
mychef.chicken()
mychef.special()

from tools import ChineseChef
mychinesechef = ChineseChef()
mychinesechef.chicken()
mychinesechef.special()

list = [1,3,5,6]
list.insert(2,4)
list.pop(1) #相当于 del list[1]
print(list)

list1 = [3, 7, 8, 9, 12]
list2 = [5, 6, 10, 13, 25, 30]
list3 = []
while list1 and list2: # list1或2有意义的时候（非空列表）
    if list1[0] < list2[0]:
        list3.append(list1[0])
        list1.remove(list1[0])
    else:
        list3.append(list2[0])
        list2.remove(list2[0])
for i in list2: # 把while循环结束后剩下的写进去
    list3.append(i)
print(list3)

print()
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for w in words[:]:  # 不写[:]就会无限插入，这个貌似很重要
    if len(w) > 6:
        words.insert(0, w)
    print(words)

print()
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            #break
            #因为n x都为任意值，所以n%x存在两种情况都符合的情况，此时break的作用是：
            #只要第一个判定满足就不进行第二次判定，注意else是在for循环中
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print()
'''
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?')
'''

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(-1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

print()