# Comparacion números flotantes

# Al comparar los flotantes puede surgir diferencia en datos por precisión (decimales)
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# Forma string
# Trasnfomando a y (quitando precisión decimal)
y_string = format(y, ".2g")
print("Forma str=>", y_string == str(x))

# Forma matemática
# Trasnfomando a y (quitando precisión decimal)
tolerance = 0.0001
print("Forma matemática=>", abs(x - y) < tolerance)

# Forma redondeo
print("Forma de redondeo=>", round(x, 1) == round(y, 1))
