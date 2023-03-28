#記帳程式清單
#清單中還有清單 (二維度清單)
products = []
while True:
    item = input('請輸入花費項目: ')
    if item == 'q':
        break
    price = input('請輸入花費金額: ')
    price = int(price)
    products.append([item, price])

for p in products:
    print('商品', p[0], '的花費是', p[1], '元')

with open('products.csv', 'w') as f:        #打開檔案
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')   #寫入檔案