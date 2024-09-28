from math import sqrt
a = float(input('Введите значение a:'))
b = float(input('Введите значение b:'))
c = float(input('Введите значение c:'))
p = a * b * c / 2
ha = (2 * sqrt(p * (p - a) * (p - b) * (p - c))) / a
hb = (2 * sqrt(p * (p - a) * (p - b) * (p - c))) / b
hc = (2 * sqrt(p * (p - a) * (p - b) * (p - c))) / c
print(f'Высота с точки a: {round(ha, 1)}')
print(f'Высота с точки b: {round(hb, 1)}')
print(f'Высота с точки c: {round(hc, 1)}')