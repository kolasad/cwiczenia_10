# napisac funkcje, ktora z tablicy wybierze wszystkie liczby calkowite, ktore:
# nie sa zerem, nie zawiraja zera z przodu, zawieraja tylko liczby, ....

tab = ['0 12', '12 0', '12.', '12', '2a', '15']


def get_numbers(numbers_list):
    valid_numbers = []
    for x in numbers_list:
        try:
            valid_numbers.append(int(x))
        except ValueError:
            pass
    return valid_numbers


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


list_comp = [int(number) for number in tab if is_int(number)]
print(list_comp)


# integers = get_numbers(tab)
# print([x for x in integers if x < 13])
# print([x if x < 13 else None for x in integers])
#
# # napisac funkcje zwracajaca liczby calkowite w list comprehenision
# print([x for x in range(10)])














# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
# [A B C    D E F G    H I J]
