# refactor 重構
import os  #operating system

#讀取現有檔案資料
def read_file(filename):
    products = []
    with open(filename, 'r') as f:    
        for line in f:
            if '商品,價格' in line:
                continue      
            item, price = line.strip().split(',')     
            products.append([item, price])
    return products   

#計入新商品花費
def user_input(products):
    while True:
        item = input('請輸入花費項目: ')
        if item == 'q':
            break
        price = input('請輸入花費金額: ')
        price = int(price)
        products.append([item, price])
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print('商品', p[0], '的花費是', p[1], '元')

#寫入資料進入檔案
def write_file(filename, products):
    with open(filename, 'w') as f:                     
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

# main function
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):             #檢查檔案在不在
        print('檔案在相同資料夾中')
        products = read_file(filename)
        print(products)
    else:
        print('檔案不在此資料夾中')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

# 執行主要程式
main()