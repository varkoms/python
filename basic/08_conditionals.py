### Conditionals ###

my_condition = False

if my_condition: # Es lo mismo if my_condition === True
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if") 

if my_condition > 10 and my_condition < 20:
    print("Es mayor a 10 y menor que 20")

elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual que 20 o distinto de 25")

print("La ejecucion continua")

my_string = "Mi cadena de texto"
if my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de textooooooooo":
    print("Estas cadenas de texto no coinciden")