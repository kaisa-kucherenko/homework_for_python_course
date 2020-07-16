def words_counter(func):
    def wrapper(file):
        print(f'File name - {file}')
        result = func(file)
        words_list = result.split()
        print(f'Words count in file - {len(words_list)}')
    return wrapper


@words_counter
def file_reader(file):
    with open(file, 'r') as file:
        r_file = file.read()
        print(r_file)
        return r_file
