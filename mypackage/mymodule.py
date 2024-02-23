def top_n(items, n):
    """ Returns the top n items in an array in descending order
    Args:
        items (array): a list or an array-like object
        n (int): the number of items to return
    Return:
        array: top n items in descending order"""
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    # to get the last n items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]