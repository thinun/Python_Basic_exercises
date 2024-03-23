input_base = int(input("Enter a base: "))
input_exponent = int(input("Enter a exponent: "))


def exponent(base, expo):
    for x in range(expo):
        base = base * base
    return base


print(exponent(input_base, input_exponent))
