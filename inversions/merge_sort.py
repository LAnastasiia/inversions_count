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


if __name__ == "__main__":
    # test code
    print(merge_sort__invertions([4, 3, 7, 2, 10, 6, 1, 9, 5, 8], 0))
