def solution(A):
    # write your code in Python 3.6
    occurrences_dict = {}
    for element in A:
        if element in occurrences_dict:
            occurrences_dict[element] += 1
        else:
            occurrences_dict[element] = 1

    for key, value in occurrences_dict.items():
        if value % 2 == 1:
            return key
