# Declarando str
name = "Carlos"
last_name = "Olivera"
my_age = 20
print(name)
print(last_name)

# Concatenar nombres
full_name = name + " " + last_name
print(full_name)

# Declarando str con comilla
quote = "I'm Carlos"
print(quote)

quote_2 = 'She said "Hello"'
print(quote_2)

# Dando formato
print("Sin función format")
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

print("Con función format")
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

print("Usando f")
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

print("Usando f con tres variables")
template = (
    f"Hola, mi nombre es {name} y mi apellido es {last_name}, tengo {my_age} años"
)
print(template)

# Replicar string
print("Hola" * 3)
