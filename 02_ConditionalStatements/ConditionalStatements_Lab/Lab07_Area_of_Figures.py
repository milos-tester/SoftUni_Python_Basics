import math

type_of_figure = str(input())
if type_of_figure == 'square':
    side_length = float(input())
    result = side_length * side_length
    print(f'{round(result,3)}')
elif type_of_figure == 'rectangle':
    side_one_length = float(input())
    side_two_length = float(input())
    result = side_one_length * side_two_length
    print(f'{round(result,3)}')
elif type_of_figure == 'circle':
    radius_length = float(input())
    result = math.pow(radius_length, 2) * math.pi
    print(f'{round(result,3)}')
elif type_of_figure == 'triangle':
    side_length = float(input())
    height_length = float(input())
    result = (side_length * height_length) / 2
    print(f'{round(result,3)}')