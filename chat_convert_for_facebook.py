#讀取原有對話    #如果讀取後在第一航開頭出現\ufeff時，要在utf-8再加-sig
def read_dialogue(filename):
    dialogue = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            dialogue.append(line.strip())
    return dialogue

#對話格式轉換
def convert_dialogue(dialogue):
    sentences = []
    name = None             # 防止第一行不是人名時
    for line in dialogue:
        if any(n in line for n in ('Allen','Tom')):
            name = line
            continue
        else:
            sentences.append(name + ': ' + line)
    return sentences

#寫入轉換後的對話格式進入檔案
def write_dialogue(filename, sentences):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:                     
        for s in sentences:
            f.write(s + '\n')

# 執行主程式
def main():
    dialogue = read_dialogue('input.txt')
    sentences = convert_dialogue(dialogue)
    write_dialogue('dialogue.txt', sentences)

main()