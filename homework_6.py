# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась с такими аргументами, она не будет вызываться снова, вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.

def do_cache(maxsize):
    def do_cache_decorator(func):
        storage = []
        def wrapper_do_cache(*args):
            if len(storage) == 0:
                result_func = func(*args)
                storage.append(
                    {'args_func': args, 'result_func': result_func})
                return result_func
            else:
                if len(storage) >= maxsize:
                    storage.pop()
                for i in storage:
                    if args in i.values():
                        return i['result_func']
                    else:
                        result_func = func(*args)
                        storage.append(
                            {'args_func': args, 'result_func': result_func})
                        return result_func
        return wrapper_do_cache
    return do_cache_decorator


@do_cache(maxsize=3)
def get_value(a, b):
    return a ** b
