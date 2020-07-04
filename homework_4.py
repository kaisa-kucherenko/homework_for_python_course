def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """

    result_list = [url for url in url_list if '/catalog/' in url]
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """

    middle_index = len(input_str) // 2 - 1
    if len(input_str) % 2 == 0:
        output_str = input_str[middle_index:middle_index + 2]
    else:
        output_str = input_str[middle_index:middle_index + 3]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """

    input_str = input_str.replace(' ', '').lower()
    output_dict = {letter: input_str.count(letter) for letter in input_str}
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """

    middle_index = len(str1) // 2
    letters_lst = [letter for letter in str1]
    letters_lst.insert(middle_index, str2)
    result_str = ''.join(letters_lst)
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """

    even_int_list = [number for number in range(0, 100) if number % 2 == 0]
    even_int_list.remove(0)
    return even_int_list
