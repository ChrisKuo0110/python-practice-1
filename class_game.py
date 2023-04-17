# class 類別(種類)
#寫class 才可以發明自己的type(型別) ，然後就可以做出這個type(型別)的object(物件)
#不同型別的物件有不同的屬性(attributes)或稱能力(function)--可以用dir()查詢物件屬性

# 可以使用self來存取身上的function 
# 在class裡面的method間格空一行,在class外面的function間格空兩行

import random

class Player:
    def __init__(self, name, hp, ak):
        self.name = name
        self.hp = hp
        self.ak = ak

    def attack(self, target):
        print(self.name, '攻擊', target.name)
        target.hp -= self.ak


p1 = Player('Chris', random.randint(50, 100), random.randint(1, 10))
p2 = Player('Darren', random.randint(50, 100), random.randint(1, 10))

print('玩家',  p1.name, '的初始生命值是', p1.hp)
print('玩家',  p1.name, '的初始攻擊力是', p1.ak)
print('玩家',  p2.name, '的初始生命值是', p2.hp)
print('玩家',  p2.name, '的初始攻擊力是', p2.ak)

print(p2.name, '攻擊了', p1.name)
p2.attack(p1)
print(p1.name, '的生命值剩下', p1.hp)

#class 三大好處:
#1. 把相關function收納在一起
#2. 透過slef來共用身上的屬性
#3. 包裝程式碼方便使用