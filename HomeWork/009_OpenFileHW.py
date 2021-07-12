with open('text_file//threemusketeer.txt', 'r', encoding='utf8') as rfile:
    words = []
    lines = rfile.read().splitlines()
    un_words = set()
    for line in lines:
        un_words |= set(line.split())
    print("-------- Подсчёт слов уникальных слов ------------")
    print(f"Количевство уникальных слов в книге: {len(un_words)}")
    print("----------------------------------------------------")