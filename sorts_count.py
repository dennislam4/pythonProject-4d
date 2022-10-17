# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-17-2022
# Description: Contains two comparison function. Bubble sort that counts the number of comparisons and the number of
# exchanges made while sorting a list and returns a tuple of the two values. Uses two sorting methods, bubble sort
# and insertion sort.

def bubble_count(a_list):
    """Bubble sort alogrithim that also counts number of comparisons and exchanges while sorting a list."""
    number_of_comparisons = 0
    number_of_exchanges = 0
    list_length = len(a_list)
    for pass_num in range(list_length - 1):
        for index in range(list_length - 1 - pass_num):
            number_of_comparisons += 1
            if a_list[index] > a_list[index + 1]:
                value = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = value
                number_of_exchanges += 1
    # return a_list
    return (number_of_comparisons, number_of_exchanges)


def insertion_count(a_list):
    """Insertion sort algorithim that also counts number of comparisons and exchanges while sorting a list."""
    number_of_comparisons = 0
    number_of_exchanges = 0
    for index in range(1, len(a_list)):
        value = a_list[index]
        position = index - 1
        while position >= 0 and a_list[position] > value:
            a_list[position + 1] = a_list[position]
            position -= 1
            number_of_comparisons += 1
            number_of_exchanges += 1
        a_list[position + 1] = value
    # return a_list
    return (number_of_comparisons, number_of_exchanges)


# print(bubble_count([3, 1, 6, 11, 8, 2]))
# print(insertion_count([7, 8, 9, 0, 2, 3]))
