
def custom_write(file_name, strings):
    st = 0
    el = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        st += 1
        file.write(f'{i}\n')
        file.close()
        el.update({(st, tell):i})
    return el
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for el in result.items():
    print(el)