import math

x = int(input("Оберіть формулу 1 (S), 2 (FV), 3 (G), 4 (C): "))
if x == 1:
    s0 = float(input("Введіть s0: "))
    v0 = float(input("Введіть v0: "))
    t = float(input("Введіть t: "))
    g = float(input("Введіть g: "))
    s = s0 + v0 * t + (g * t**2) / 2
    print(s)

if x == 2:
    PV = float(input("Введіть PV: "))
    INT = float(input("Введіть INT: "))
    YRS = int(input("Введіть YRS: "))
    FV = PV * (1 + (INT / 100))**YRS
    print(FV)

if x == 3:
    a = float(input("Введіть a: "))
    p = float(input("Введіть p: "))
    m1 = float(input("Введіть m1: "))
    m2 = float(input("Введіть m2: "))
    G = 4 * (math.pi)**2 * (a**3) / (p**2 * (m1 + m2))
    print(G)

if x == 4:
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    gamma = float(input("Введіть γ: "))
    c = math.sqrt((a**2) + (b**2) - 2 * a * b * math.cos(gamma))
    print(c)