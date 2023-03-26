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