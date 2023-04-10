data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1  # count = count + 1
        if count % 1000 == 0:
            print(len(data))
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