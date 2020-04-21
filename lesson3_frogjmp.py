def solution(X, Y, D):
    # Checking if X and Y are the same to avoid unnecessary calculations
    if X == Y:
        return 0
    # Covering cases that X < Y
    else:
        distance_to_Y = Y - X
        number_of_jumps = int(distance_to_Y / D)
        if distance_to_Y % D > 0:
            number_of_jumps += 1

        return number_of_jumps
