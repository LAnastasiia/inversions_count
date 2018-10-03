# File: task_02.py
# This module contains functions for finding the difference k between movie watchers by counting inversions.


def us2_modification(us1, us2):
    """
    Returns an alternative modification of us2 list due to us1's standarts.
    :param us1:            List of the top movies charts for the 1st ('ideal') user.
    :param us2:            List of the top movies chart for another user.
    :return: us2_res       Modified copy of us2's movie chart
    """
    us_len = len(us1)
    us2_res = [None] * us_len
    # Order values in the loop.
    for i in range(us_len):
        us2_res[us1[i]-1] = us2[i]
    print(us2_res)
    return us2_res

def _merge(arr_left, arr_right):
    import math
    infinity = math.inf
    """
    Merge together two parts of the list.
    :param arr_left:
    :param arr_right:
    :return: arr_res.
    """
    arr_res = []
    i, j = 0, 0
    inversion_count = 0

    # arr_left.append(infinity)
    # arr_right.append(infinity)

    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr_res.append(arr_left[i])
            i += 1
        elif arr_right[j] < arr_left[i]:
            arr_res.append(arr_right[j])

            print("CHECK", j, arr_left[i:])
            inversion_count += len(arr_left[i:])
            j += 1
    # Complete sorted list with leftover elements of the longer sublist.
    # print("i, j:  ", i, j, "arr_left", len(arr_left[i:])-1)
    if i < j:
        arr_res.extend(arr_left[i:])
        # if len(arr_left[i:]) > 1:
            # inversion_count += inversion_count * (len(arr_left[i:])-1)
    else:
        arr_res.extend(arr_right[j:])

    print("inversion_count", inversion_count)
    return arr_res, inversion_count


def merge_sort__invertions(arr, inversions=0):
    """
    Function for counting total number of inversions in the list using the Merge Sort algorithm.
    :param arr:            initial list (array)
    :param inversions:     current number of inversions
    :return:               (sorted array, total number of invertions in the initial list)
    """
    if len(arr) <= 1:
        return arr, 0
    else:
        half_ind = len(arr) // 2
        arr_left = merge_sort__invertions(arr[:half_ind], inversions)  # (left part, inversions from merging this part)
        arr_right = merge_sort__invertions(arr[half_ind:], inversions) # (right part, inversions from merging this part)
        print(arr_left, arr_right, inversions)
        # Merging two parts together + counting inversions in current merge.
        merge_results = _merge(arr_left[0], arr_right[0])
        inversions = arr_left[1] + arr_right[1] + merge_results[1]     # Update the value of total inversions.
        print("total:", inversions)
        return merge_results[0], inversions

def count_inversions(data, x):
    """
    :param data:            2D array with user's top charts of movies
    :param x:               Index of 'ideal' user in data to which all other users will be compared
    :return inversions_res: 2D array of [user index; inversions] ordered by increasing number of inversions value.
    """
    inversion_array = []
    for us_i in range(len(data)):
        ideal_us = data[x]
        if us_i != x:
            modified_us = us2_modification(ideal_us, data[us_i])
            inversions = merge_sort__invertions(modified_us, 0)[1]
            inversion_array.append([us_i, inversions])
    print(inversion_array)
    print(inversion_array.sorted())



#
# if __name__ == "__main__":
data = [[3, 2, 10, 6, 9, 1, 5, 7, 4, 8], [2, 10, 8, 9, 5, 4, 3, 7, 6, 1], [2, 4, 9, 6, 10, 7, 5, 1, 3, 8], [3, 9, 10, 6, 7, 4, 1, 2, 5, 8], [7, 3, 8, 6, 5, 4, 10, 1, 2, 9]]
count_inversions(data, 0)
