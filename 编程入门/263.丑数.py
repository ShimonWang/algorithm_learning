def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        prime_factor = set()
        i = 2
        while i <= n:
            if n % i == 0:
                prime_factor.add(i)
                while n % i == 0:
                    n = n / i
            i += 1

    if prime_factor - {2, 3, 5} != set():
        return False
    else:
        return True


# print(isUgly(6))
# print(isUgly(30))
# print(isUgly(14))
print(isUgly(8))
