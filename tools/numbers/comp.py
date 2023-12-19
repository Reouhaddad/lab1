def sumofdigits(n):
    from .simp import f_call 
    if not f_call:
        raise Exception("Call a function in 'simp' module before calling functions in 'comp' module.")
    return sum(int(digit) for digit in str(n))

def ispal(n):
    from .simp import f_call  
    if not f_call:
        raise Exception("Call a function in 'simp' module before calling functions in 'comp' module.")
    original_n = n
    reverse_n = 0

    while n > 0:
        reverse_n = reverse_n * 10 + n % 10
        n = n // 10

    return original_n == reverse_n
