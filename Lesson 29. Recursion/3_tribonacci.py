def tribonacci(n):
    if n in [0, 1]:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
