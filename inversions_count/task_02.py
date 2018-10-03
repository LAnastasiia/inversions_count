# File: task_02.py
# This module contains functions for finding the difference k between movie watchers by counting inversions.

def us_fix(us1, us2):
    """
    Returns an alternative modification of us2 list due to us1's standarts.
    :param us1:            List of the top movies charts for the 1st ('ideal') user.
    :param us2:            List of the top movies chart for another user.
    :return: us2_res       Modified copy of us2's movie chart
    """
    us_len = len(us1)                                         # Secure the length value of initial list.

    # Check values for correspondance (if both users have seen the movie).
    checked_us1 = [us1[i] for i in range(us_len) if us1[i] and us2[i]]
    checked_us2 = [us2[i] for i in range(us_len) if us1[i] and us2[i]]

    checked_len = len(checked_us1)                             # Secure the length of new list to avoid recalculating.

    us1_res = [None] * checked_len                             # Create empty lists for future us1 and us2.
    us2_res = [None] * checked_len

    indexed_us1 = list(zip(range(checked_len), checked_us1))   # Keep initial indexes for every value.
    indexed_us2 = list(zip(range(checked_len), checked_us2))

    sorted_us1 = sorted(indexed_us1, key=lambda x: x[1])       # Sort by values.
    sorted_us2 = sorted(indexed_us2, key=lambda x: x[1])

    for i in range(checked_len):
        us1_res[sorted_us1[i][0]] = i+1                         # Add values to us1 & us2 from 1 to checked_len.
        us2_res[sorted_us2[i][0]] = i+1

    return us1_res, us2_res


def us2_modification(us1, us2):
    """
    Returns an alternative modification of us2 list due to us1's standarts.
    :param us1:            List of the top movies charts for the 1st ('ideal') user.
    :param us2:            List of the top movies chart for another user.
    :return: us2_res       Modified copy of us2's movie chart
    """
    u1, u2 = us_fix(us1, us2)
    us_len = len(u1)
    u2_res = [None] * us_len
    # Order values in the loop.
    for i in range(us_len):
        u2_res[u1[i]-1] = u2[i]
    return u2_res


def _merge(arr_left, arr_right):
    """
    Merge together two parts of the list.
    :param arr_left:
    :param arr_right:
    :return: arr_res.
    """
    arr_res = []
    i, j = 0, 0
    inversion_count = 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr_res.append(arr_left[i])
            i += 1
        elif arr_right[j] < arr_left[i]:
            arr_res.append(arr_right[j])
            inversion_count += len(arr_left[i:])
            j += 1
    # Complete sorted list with leftover elements of the longer sublist.
    if i < j:
        arr_res.extend(arr_left[i:])
    else:
        arr_res.extend(arr_right[j:])

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
        arr_left = merge_sort__invertions(arr[:half_ind], inversions)   # (left part, inversions from merging this part)
        arr_right = merge_sort__invertions(arr[half_ind:], inversions)  # (right part, inversions from merging this part)
        # Merging two parts together + counting inversions in current merge.
        merge_results = _merge(arr_left[0], arr_right[0])
        inversions = arr_left[1] + arr_right[1] + merge_results[1]     # Update the value of total inversions.
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
    inversion_array = sorted(inversion_array, key=lambda pair: pair[1])
    return inversion_array
