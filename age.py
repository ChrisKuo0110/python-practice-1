driving = input('請問您有沒有開過車?(有/沒有) ')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit

age = input('請問你的年齡? ')
age = int(age)
if driving == '有':
    if age >= 18:
        print('好棒棒!可以開車到處趴趴走~')
    else:
        print('奇怪!你竟然開過車!我要檢舉你無照駕駛~')
elif driving == '沒有':
    if age >= 18:
        print('趕快去考駕照吧~這樣才可以開車去兜風')
    else:
        print('再等等幾年就可以考駕照囉~')