def get_to_sum(a, b):
    def get_sum(a, b):
        return a + b

    addition = get_sum(a, b) + 5
    return addition


print(get_to_sum(10, 5))
