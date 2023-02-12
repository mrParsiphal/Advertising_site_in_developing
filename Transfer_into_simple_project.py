import os


def Conservation(object_in_directory):
    pass


def Poisk():
    this_directory = os.getcwd()
    objects_in_directory = os.listdir(path=".")
    for object_in_directory in objects_in_directory:
        object_format = object_in_directory.find('.')
        if object_format > 0:
            object_format_file = object_in_directory[object_format + 1:]
            if object_format_file == 'html':
                Transfer(object_in_directory)
                Conservation(object_in_directory)
            elif object_format_file in ('png', 'jpg'):
                Transfer(object_in_directory)
                Conservation(object_in_directory)
            elif object_format_file in ('js'):
                Transfer(object_in_directory)
                Conservation(object_in_directory)
            elif object_format_file in ('css'):
                Transfer(object_in_directory)
                Conservation(object_in_directory)
        else:
            Poisk()



def Transfer():
    print(os.getcwd())
    print(os.listdir(path="."))
    # for i in 1:
    #     print()
    os.chdir('Main_site')
    print(os.getcwd())
    print(os.listdir(path="."))






if __name__ == '__main__':
    Transfer()
    input('Press Enter to exit the console!')