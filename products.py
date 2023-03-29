#記帳程式清單

import os  #operating system

#讀取現有檔案資料
#如果出現UnicodeDecodeError,要額外加額外加, encoding = 'utf-8'
#變成with open('products.csv', 'r', encoding = 'utf-8') as f:
#continue只能在迴圈裡面寫，
#continue跳到下一回，不再繼續執行迴圈裡後續的程式
#continue通常都是寫在迴圈中最高的位置 
products = []
if os.path.isfile('products.csv'):            #檢查檔案在不在 
    print('檔案在相同資料夾中')
    with open('products.csv', 'r') as f:    
        for line in f:
            if '商品,價格' in line:
                continue      
            item, price = line.strip().split(',')     
            products.append([item, price])
    print(products)
else:
    print('檔案不在此資料夾中')

#計入新商品花費
while True:
    item = input('請輸入花費項目: ')
    if item == 'q':
        break
    price = input('請輸入花費金額: ')
    price = int(price)
    products.append([item, price])      #清單中還有清單 (二維度清單)

for p in products:
    print('商品', p[0], '的花費是', p[1], '元')

#寫入資料進入檔案
#如果中文欄位名讀取有問題可以額外加, encoding = 'utf-8'
#變成with open('products.csv', 'w', encoding = 'utf-8') as f:
with open('products.csv', 'w') as f:                     
    f.write('商品,價格\n')                               #欄位名稱
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')          #寫入檔案