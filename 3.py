user_input = input("Введіть 4-значне число: ")
digits = [int(x) for x in user_input]
print(" + ".join(user_input), "=", sum(digits))
