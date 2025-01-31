MorseCode = {
    # eng
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',  'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',  'v': '...-',
    'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',

    # ru
    'а': '.-',    'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..',
    'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',   'и': '..', 'й': '.---',
    'к': '-.-', 'л': '.-..',  'м': '--', 'н': '-.', 'о': '---', 'п': '.--.',
    'р': '.-.', 'с': '...',   'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....',
    'ц': '-.-.', 'ч': '---.',  'ш': '----', 'щ': '--.-', 'ъ': '--.--',
    'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-',

    ' ': ''
}
language = ''


def encode_to_morse(text):
    encode_list = []
    for el in text:
        if el.lower() in MorseCode:
            encode_list.append(MorseCode[el])
        else:
            encode_list.append(el)
    return encode_list


def decode_from_morse(code):
    decode_list = []
    for codes in code.split('  '):
        for cod in codes.split():
            for el in cod.split():
                for key, value in MorseCode.items():
                    if value == el:
                        if language == 'ru' and 'а' <= key <= 'я':
                            decode_list.append(key)
                            break
                        elif language == 'eng' and 'a' <= key <= 'z':
                            decode_list.append(key)
                            break
                else:
                    decode_list.append(el)
                    break
        decode_list.append(' ')
    return ''.join(decode_list)


def main():
    global language
    print('Привет!\nЯ умею:')
    while True:
        print('1. Кодировать в код Морзе\n',
            '2. Декодировать с кода Морзе\n3. Выход', sep='')

        func = 0
        while func not in [1, 2, 3]:
            func = int(input('Что тебе нужно?\n'))
            if func not in [1, 2, 3]:
                print('Нет такого варианта!')

        if func == 3:
            print('---Конец---')
            return
        
        lang = 0
        while lang not in [1, 2]:
            lang = int(input('\nА теперь выбери язык:\n1. Русский\n2. Аглийский\n'))
            if lang not in [1, 2]:
                print('Нет такого варианта!')
        if lang == 1:
            language = 'ru'
        else:
            language = 'eng'

        if func == 1:
            print('\nРезультат:', *encode_to_morse(input(
                '\nВведите текст, который нужно перевести:\n')), '\n')
        else:
            print('\nРезультат:', decode_from_morse(input(
                '\nВведите текст, который нужно перевести:\n')), '\n')
        language = ''


main()