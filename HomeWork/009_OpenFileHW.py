
with open('text_file//lovecraft.txt', 'r',encoding='utf8') as rfile:
    lines = rfile.read().lower().replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').split()
    un_words = set()
    for line in lines:
        un_words |= set(line.split())
    print("-------- Подсчёт уникальных слов ------------")
    print(f"Количевство уникальных слов в книге: {len(un_words)}")

with open('text_file//lovecraft.txt', 'r',encoding='utf8') as rfile2:
    count = len(rfile2.read().split())
    print("-------- Подсчёт всех слов ------------------")
    print(f"Количевство слов в книге: {count}")
    print("---------------------------------------------")

with open('text_file//lovecraft_log.txt','w',encoding='UTF8') as wfile:
    wfile.write(f'There are {count} words in text.\n'
                f'There are {len(un_words)} uniqie words in text')