# farenheit = [47, 32, 212]
# print(list(map(lambda index: (index, (index - 32) * 5 / 9), farenheit)))

height_per_meter = [(index, index * 0.0254,) for index in [69, 77, 54]]
list(map(lambda index: index in [69, 77, 54], height_per_meter))

print(height_per_meter)

