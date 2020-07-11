# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась с такими аргументами, она не будет вызываться снова, вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.

def do_cache(maxsize):
    def decorator_do_cache(func):
        storage = []
        def wrapper_do_cache(*args):
            for data_func in storage:
                if args == data_func['args_func']:
                    return data_func['result_func']
            if len(storage) == maxsize:
                storage.pop()
            result_func = func(*args)
            storage.append({'args_func': args, 'result_func': result_func})
            return result_func
        return wrapper_do_cache
    return decorator_do_cache


@do_cache(maxsize=3)
def get_value(a, b):
    return a ** b
