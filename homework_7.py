import os


def logs_file_in_dir(func):
    def wrapper(dir_path):
        result = func(dir_path)
        for file_path in result:
            if os.path.isfile(file_path) and '.log' in file_path:
                with open(file_path, 'r') as file_log:
                    r_file = file_log.read()
                    print(r_file)
    return wrapper


@logs_file_in_dir
def list_file(dir_path):
    result = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    return result
