import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

x = b**2 - 4*a*c
if x == 0:
    print("Один корінь: ", -(b / (2*a)))

if x < 0:
    print("Коренів немає")

if x > 0:
    print("Перший корінь: ", round((-b) - (math.sqrt(x)) / (2 * a), 2))
    print("Другий корінь: ", round((-b) + (math.sqrt(x)) / (2 * a), 2))