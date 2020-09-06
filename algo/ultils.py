def check_in(candidate, record):
    for item in candidate:
        if item not in record:
            return False
    return True


def calculate_sup(candidate, db):
    support = 0
    for record in db:
        if check_in(candidate, record):
            support += 1
    return support


def check_array_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    if check_in(arr1, arr2):
        return True
    return False


def check_exist(candidate, list_candidate):
    for temp in list_candidate:
        if check_array_equal(temp, candidate):
            return True
    return False


def build_new_list_candidate(list_candidate, list_first_candidate):
    res = []
    for candidate in list_candidate:
        for first_candidate in list_first_candidate:
            new_candidate = set()
            for item in candidate:
                new_candidate.add(item)
            for item in first_candidate:
                new_candidate.add(item)
            if (len(new_candidate) > len(candidate)) and (not check_exist(new_candidate, res)):
                res.append(list(new_candidate))
    return res
