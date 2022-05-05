print('Привет я тут чтоб считать буквы и символы в твоём тексте)')
text = input('Введи свой текст: ')
for char in text:
    n = text.count(char)
    print(f'символ {char} встречался {n} раз')
