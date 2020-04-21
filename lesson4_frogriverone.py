def solution(X, A):
    # Creating an aux dict
    aux = {}
    counter = 0
    for i in range(len(A)):
        if A[i] not in aux:
            aux[A[i]] = 1
            counter += 1
        if counter == X:
            return i
    return -1