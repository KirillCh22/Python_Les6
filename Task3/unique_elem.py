
def unique_elements(list1: int, list2: int):

    set1, set2 = set(list1), set(list2)

    # print(set1)
    # print(set2)

    return list(set1.union(set2))