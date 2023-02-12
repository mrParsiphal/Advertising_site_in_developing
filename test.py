while True:
    object_in_directory = input()
    object_format = object_in_directory.find('.')
    object_format_file = object_in_directory[object_format + 1:]
    print(object_format_file)