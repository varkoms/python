### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    print("La ejecucion continua")

# Controlar excepciones concretas
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# except Exception as ex:
#     print(ex) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

