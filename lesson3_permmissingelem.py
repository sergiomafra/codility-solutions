def solution(A):
    len_A = len(A)
    if A == []:
        return 1
    elif len_A == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    else:
        A = sorted(A)
        if A[0] != 1:
            return 1
        elif A[len_A-1] != len_A+1:
            return len_A+1
        else:
            for i in range(1, len_A):
                if A[i] != (A[i-1] + 1):
                    return A[i] - 1