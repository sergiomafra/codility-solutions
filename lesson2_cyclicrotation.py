def solution(A, K):
    # write your code in Python 3.6
    len_A = len(A) # saving A length to a var
    # Testing coditions
    if len_A == 0 or K == 0 or len_A == K:
        return A
    elif len_A < K:
        K = K % len_A
    # Calculating the final result
    new_A = A[-K:] + A[:-K]

    return new_A
