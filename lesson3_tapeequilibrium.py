def solution(A):
    # List of all absolute differences
    abs_list = []
    # Auxiliar variables
    sum_A = sum(A)
    sum_til_i = 0
    # Calculating split abs differences and appending to abs_list
    for i in range(1,len(A)):
        sum_til_i += A[i-1]
        sum_i_forward = sum_A - sum_til_i
        abs_list.append(abs(sum_til_i - sum_i_forward))

    return min(abs_list)