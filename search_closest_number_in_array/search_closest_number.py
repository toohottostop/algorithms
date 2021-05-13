from typing import List


def search_closest(array: List[int], number: int) -> int:
    low = 0
    high = len(array) - 1
    mid = 0
    if not array:
        return -1
    elif len(array) == 1:
        return array[0]
    elif array[low] == number or array[high] == number:
        return number

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == number:
            return guess
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1

    if mid == 0:
        if abs(array[mid] - number) > abs(array[mid + 1] - number):
            return array[mid + 1]
        else:
            return array[mid]
    elif abs(array[mid] - number) > abs(array[mid - 1] - number):
        return array[mid - 1]
    else:
        return array[mid]
