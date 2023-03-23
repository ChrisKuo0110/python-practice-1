#猜數字遊戲
import random

start = input('請決定隨機數字範圍的開始值: ')
end = input('請決定隨機數字範圍的結束值: ')

r = random.randint(start, end)
x = 0

while True:

    num = input('請猜看看所列範圍的整數: ')
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