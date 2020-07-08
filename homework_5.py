def three_biggest_int(input_list):
    """
        Дан массив чисел.
        [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
        вывести 3 наибольших числа из исходного массива
    """
    clean_list = sorted(list(set(input_list)), reverse=True)
    biggest_ints = [number for number in clean_list[:3]]
    return biggest_ints


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    low_int_index = input_list.index(min(input_list))
    return low_int_index


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    reversed_result = list(reversed(input_list))
    return reversed_result


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    common_keys = [key for key in dict1.keys() if key in dict2.keys()]
    return common_keys


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    student_list.sort(key=lambda student: student['age'])
    sorted_dict = {student['city']: [] for student in student_list}
    for student in student_list:
        city = student['city']
        student.pop('city')
        name_age_dict = {key: value for key, value in student.items()}
        sorted_dict[city].append(name_age_dict)
    return sorted_dict
