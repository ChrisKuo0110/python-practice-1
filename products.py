#記帳程式清單
#清單中還有清單 (二維度清單)
products = []
while True:
    item = input('請輸入花費項目: ')
    if item == 'q':
        break
    price = input('請輸入花費金額: ')
    products.append([item, price])

for p in products:
    print('商品', p[0], '的花費是', p[1], '元')