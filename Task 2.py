import random, math

def petya_task(array):
    sum_positive_numbers = sum(number for number in array if number > 0)
    min_index, max_index = array.index(min(array)), array.index(max(array))
    if min_index < max_index:
        product_between_min_max = math.prod(array[min_index + 1:max_index])
    else:
        product_between_min_max = math.prod(array[max_index + 1:min_index])
    return sum_positive_numbers, product_between_min_max