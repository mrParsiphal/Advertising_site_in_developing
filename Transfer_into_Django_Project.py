import os


def transfer():
    text = open(input('Chose name file for reading:') + '.html', encoding='utf-8', mode='r')
    print('Read succesful')
    file_name = input('Chose file name for safe results:')
    new_file = ['{% load static %}']
    for stroke in text:
        if (stroke.find('href') != -1) and (stroke.find('css/') != -1):
            stroke = stroke.replace('css/', "{% static 'main/css/")
            stroke = stroke.replace('css"', "css' %}\"")
            print(stroke.rstrip())
        elif stroke.find('src') != -1:
            if stroke.find('img/') != -1:
                stroke = stroke.replace('img/', "{% static 'main/img/")
                try:
                    stroke = stroke.replace('png"', "png' %}\"")
                except: pass
                try:
                    stroke = stroke.replace('jpg"', "jpg' %}\"")
                except: pass
            elif stroke.find('js/') != -1:
                stroke = stroke.replace('js/', "{% static 'main/scripts/")
                stroke = stroke.replace('.js"', ".js' %}\"")
            elif stroke.find('scripts/') != -1:
                stroke = stroke.replace('js/', "{% static 'main/scripts/")
                stroke = stroke.replace('.js"', ".js' %}\"")
            print(stroke.rstrip())
        else:
            print(stroke.rstrip())
        new_file.append(stroke.rstrip())

    with open(f'{file_name}.html', encoding='utf-8', mode='w') as result:
        for i in new_file:
            result.write(i + '\n')
    result.close()
    text.close()
    print('File write succesful')


if __name__ == '__main__':
    transfer()
    input('Press Enter to exit the console!')


