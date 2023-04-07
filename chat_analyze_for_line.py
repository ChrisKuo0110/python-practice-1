#讀取原有對話    #如果讀取後在第一航開頭出現\ufeff時，要在utf-8再加-sig
def read_dialogue(filename):
    dialogue = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            dialogue.append(line.strip())
    return dialogue

#對話格式轉換
def convert_dialogue(dialogue):
    name = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in dialogue:
        s = line.strip().split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for i in s[2:]:
                    allen_word_count += len(i)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for i in s[2:]:
                    viki_word_count += len(i)

    print('Allen說了', allen_word_count, '個字')
    print('Allent傳送了', allen_sticker_count, '次貼圖')
    print('Allent傳送了', allen_image_count, '張圖片')
    print('Viki說了', viki_word_count, '個字') 
    print('Viki傳送了', viki_sticker_count, '次貼圖')
    print('Viki傳送了', viki_image_count, '張圖片')   

# 執行主程式
def main():
    dialogue = read_dialogue('LINE-Viki.txt')
    sentences = convert_dialogue(dialogue)

main()