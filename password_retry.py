#密碼重試程式
x = 3
password = '9193'
while True:
    response = input('請輸入四位數密碼【最多輸入三次】:')
    if response == password:
        print('登入成功')
        break
    else:
        x = x - 1
        if x >= 1:
            print('密碼錯誤!還有', x, '次機會')
        elif x == 0:
            print('密碼已錯誤3次，將無法再執行!')
            break