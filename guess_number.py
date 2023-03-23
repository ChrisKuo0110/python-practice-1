#猜數字遊戲
import random

x = 0
r = random.randint(1, 100)
while True:
    num = input('請猜看看1到100的整數: ')
    num = int(num)
    x = x + 1
    if num == r:
        print('恭喜你在第', x, '次猜中了!')
        break
    elif num > r:
        print('還要比', num, '更小喔!')
    else:
        print('還要比', num, '更大喔!')
    print('您已經猜錯', x, '次囉!')