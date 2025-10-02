import math

a = int(input("Введіть число 1: "))
b = int(input("Введіть число 2: "))

print("Сума =",a + b)
print("Різниця =",a - b)
print("Добуток =",a * b)
print("Середнє арифметичне =",(a * b) / 2 )
print("Середнє геометричне =",math.sqrt(a * b)  if a * b >= 0 else "не існує")
print("Відстань =",abs(a - b))
print("Максимум =",max(a,b) )
print("Мінімум =",min(a,b) )
print("Сума квадратів =",a**2 + b**2 )
print("Квадрат суми =",(a + b)**2 )
print("a в степені b =",a**b )