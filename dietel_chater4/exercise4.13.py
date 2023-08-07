def product_number(*args):
    product = 1
    for numbers in args:
        product *= numbers
    return product


# print(product_number(43, 10, 40))
print(product_number(*range(2, 5, )))