def prime_numbers(n: int, m: int) -> list:
    result = []
    for element in range(n, m + 1):
        is_prime = True
        for divider in range(2, element):
            if divider > 1 and element % divider == 0:
                is_prime = False
                break
        if is_prime:
            result.append(element)
    return result