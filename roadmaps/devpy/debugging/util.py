import traceback
import os

# En lugar de bloquear un programa cuando una excepción ocurre
# puede considerar guardar la información del traceback en un
# archivo txt y mantener el programa ejecutandose. Puedes ver el
# archivo resultante después para realizar el debug del programa.

try:
    # Mecanismo para evitar llegar a la excepción
    # Cambiar condicional a "False" si se desea probar la utilidad de guardado de errores en archivos.
    if False:
        print("Finished!")
    else:
      raise Exception('This is the error message')
except:
    # os.path.realpath(__file__) Nos devuelve la ruta absoluta del script actual
    # os.path.dirname() Obtiene la ruta de la carpeta
    # os.path.join() Unimos las rutas usando el separador del sistema
    errorFile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'errorInfo.txt'), 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written to errorInfo.txt")
    