### Loops ###

# While - Usar en elementos INFINITOS, es decir,
# cuando no sabemos la cantidad exacta de elementos a iterar

print("[WHILE LOOP]")
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break
    
    print(my_condition)

print("La ejecucion continua")

# For - Usar en elementos FINITOS, es decir
# que sepamos cuantos valores tenemos
print("[FOR LOOP]")

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (33, 1.79, "Cesar", "Mendoza", "Cesar")

for element in my_tuple:
    print(element)

my_set = {"Cesar", "Mendoza", 33}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Cesar", "Apellido": "Mendoza", "Edad": 33, 1:"Python"}
for element in my_dict:
    print(element)
    # if element == "Edad":
    #     continue
else:
    print("El bucle for del dict ha finalizado")
