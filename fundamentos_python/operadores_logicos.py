# Operadores lógicos

# And (las dos partes de la operación deben dar verdadero)
print("AND")
print("True and True =>", True and True)  # True
print("True and False =>", True and False)  # False
print("False and False =>", False and False)  # False

# Ejemplo and
stock = input("Ingrese el número de stock => ")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

# And (las dos partes de la operación deben dar verdadero)
print("OR")
print("True or True =>", True or True)  # True
print("True or False =>", True or False)  # True
print("False or False =>", False or False)  # False

# Ejemplo or
rol = input("Ingrese el rol=> ")

print(rol == "admin" or rol == "seller")
