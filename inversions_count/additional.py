


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


    print(indexed_us1, '\t', indexed_us2)

    sorted_us1 = sorted(indexed_us1, key=lambda x: x[1])       # Sort by values.
    sorted_us2 = sorted(indexed_us2, key=lambda x: x[1])

    print(sorted_us1, '\t', sorted_us2)
    print(sorted_us1[2][0])

    for i in range(checked_len):
        us1_res[sorted_us1[i][0]] = i+1                         # Add values to us1 & us2 from 1 to checked_len.
        us2_res[sorted_us2[i][0]] = i+1

    return us1_res, us2_res


if __name__ == "__main__":
    print(us2_modification([2, 0, 0, 0, 5, 4, 3, 7, 6, 1], [2, 4, 0, 6, 0, 7, 5, 1, 3, 0]))
