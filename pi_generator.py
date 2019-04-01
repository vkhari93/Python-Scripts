# Generate value of pi using Leibniz formula


def odd_gen():
    # Generate series of odd numbers
    odd = 1
    while True:
        yield odd
        odd = odd + 2


def pi(limit):
    # Returns pi value after applying Leibniz formula for number of terms specified while calling the function
    odd_number = odd_gen()
    result = count = 0
    sign = True
    while count < limit:
        value = 4/next(odd_number)
        if sign:
            result += value
            sign = False
        else:
            result -= value
            sign = True
        count += 1
    return result


if __name__ == "__main__":
    print("Value of pi is {}".format(pi(100000)))







