def fib(limit):
    a = 0
    b = 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a
        b += a
        count += 1


value = input('Enter the limit for fibonacci series\t')
try:
    value = int(value)
except ValueError:
    print('Enter valid number above 0')
else:
    fib_list = [i for i in fib(value)]
    print("fibonacci numbers are {}".format(fib_list))
