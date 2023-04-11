#Python 裡所有東西都是物件，只是型別(Type)不同
#通常規矩是，function第一個字是小寫，物件(object)第一個字是大寫
#寫class(類別)可以發明型別
#通常(具規模的程式/發表成套件/或讓設計架構好很多)的情況才會寫成Class，要不然不需要，
#其必要性不高，如GUI(graphical user-interface)圖像使用者介面才會大量使用class

import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1           # count = count + 1
        bar.update(count)
print('檔案讀取完了!總共有', len(data), '筆留言')

sum_length = 0
for i in data:
    sum_length += len(i)
print('每筆留言的平均長度為', sum_length/ len(data), '字')

news = []
for i in data:
    if len(i) < 100:
        news.append(i)
print('總共有', len(news), '筆留言長度小於100字數')

goods = []
for i in data:
    if 'good' in i:
        goods.append(i)
print('總共有', len(goods), '筆留言內容有提及good的字眼')

#list 清單快寫法 (list comprehension)
bads = [i for i in data if 'bad' in i]
print('總共有', len(bads), '筆留言內容有提及bad的字眼')

#文字的計數
start_time = time.time()
wc = {}         #word_count
for d in data:
    words = d.split()      #預設值為空白鍵，用此方式可避免空字串
    for w in words:
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1      #新增新的Key值進字典

print('以下這些字出現超過100萬次: ')
for word in wc:    
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()
print('總共花費', round(end_time - start_time, 2), '秒來執行文字計數程式')

print('總共有', len(wc), '個不同的字')

while True:
    word = input('請輸入想查詢的單字次數: ')
    if word == 'q':        
        break
    elif word in wc:
        print(word, '共出現', wc[word], '次!')
    else:
        print('這個字沒有出現過在留言裡喔!')
print('感謝您的使用本查詢功能!')