from functools import reduce
# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.


#   **********************  START FIRST OPTION   **************************

# def odd_numbers (number):
#     if number % 2 != 0:
#         return True

# def add (a,b):
#     return a+b

# numbers_list = [1,23,45,4,67,8,6,10,14,11,14,82]
# odd_result=(list(filter(odd_numbers,numbers_list)))
# print(reduce(add,odd_result))


#   **********************  END FIRST OPTION   **************************


#   **********************  START SECOND OPTION   **************************


def odd_numbers(numbers):
    odds = [i if (i %2 != 0) else '*' for i in numbers ]
    if len(odds) > 0:
        result_odds =  list(filter(odd_numbers,odds))
        return reduce(add,result_odds)
        return True
    return False

def add (a,b):
    return a + b


numbers_list = [1,20,3,49,51,6,5,6,7,87]
print(odd_numbers(numbers_list))

# odd_result = list(filter(odd_numbers(numbers_list),numbers_list))
# print(odd_result)
#result = reduce(add,odd_result)


#   **********************  END SECOND OPTION   **************************