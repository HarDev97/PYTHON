# Declarando variables y transformando mediante asignación
var = "William"
print(type(var))
var = 12
print(type(var))
var = True
print(type(var))

# Transformando dato a str con str(age)
age = 12
print("Mi edad es " + str(age))

# Transformando dato a str con f
print(f"Mi edad es {age}")

# Casteando dato de edad
age = input("Ingrese edad: ")
print(type(age))
age = int(age)
print(type(age))
future_age = age + 10
print(f"Edad es {age} años, en 10 años será {future_age}")
