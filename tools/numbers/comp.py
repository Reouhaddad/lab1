def sumofdigits(n):
    return sum(int(digit) for digit in str(n))

def ispal(n):
    original_n = n
    reverse_n = 0

    while n > 0:
        reverse_n = reverse_n * 10 + n % 10
        n = n // 10

    return original_n == reverse_n