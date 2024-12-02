# Monitor de Red Básico en Python

Este proyecto consiste en un monitor de red básico desarrollado en Python, que utiliza las librerías **psutil**, **curses** y **time** para mostrar estadísticas de red en tiempo real a través de una interfaz de consola. El programa permite visualizar el uso de la red (entrante y saliente) y otras métricas relevantes de manera interactiva.

## Librerías Utilizadas

El proyecto hace uso de las siguientes librerías:

- **psutil**: Proporciona funciones para obtener información del sistema, incluyendo las estadísticas de la red.
- **curses**: Permite crear una interfaz de usuario basada en texto en la terminal.
- **time**: Usada para la sincronización y temporización de la actualización de las estadísticas en pantalla.

## Características

- **Monitorización en tiempo real**: Muestra las estadísticas de la red en tiempo real, actualizándolas constantemente.
- **Interfaz en consola**: Utiliza `curses` para crear una interfaz visual simple pero efectiva para el monitoreo.
- **Estadísticas clave**: Muestra el tráfico entrante y saliente de la red, así como el uso de la red a lo largo del tiempo.
- **Fácil de usar**: Una vez ejecutado, el programa empieza a mostrar los datos inmediatamente.

## Requisitos

Para ejecutar este programa, necesitas tener Python 3.x y las siguientes librerías instaladas:

- **psutil**: Se puede instalar con el siguiente comando:

  ```bash
  pip install psutil
  ```

- **curses**: Esta librería generalmente ya viene incluida en las distribuciones estándar de Python en sistemas Unix (Linux/Mac). En Windows, puede que necesites usar la librería `windows-curses`, que se puede instalar con:

  ```bash
  pip install windows-curses
  ```

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone git@github.com:varkoms/python.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd network_monitor
   ```

3. Instala las dependencias necesarias:

    ```bash
    pip install psutil
    ```

   Si estás en Windows, asegúrate de instalar `windows-curses` si no lo tienes ya.

## Uso

Para ejecutar el monitor de red, simplemente corre el siguiente comando:

```bash
python network.py
```

El programa mostrará las estadísticas de la red en tiempo real. Puedes salir de la aplicación presionando `q`.

## Ejemplo de salida

```bash
Monitoreo de Red - Estadísticas
----------------------------------------------------
Enviado: 82.31 MB
Recibido: 83.41 MB
Velocidad de Envío: 15.11 KB/s
Velocidad de Recepción: 15.11 KB/s
----------------------------------------------------
Presiona 'q' para salir...
```

## Detalles Técnicos

### ¿Cómo funciona?

1. **Obtención de datos**: Se utiliza la librería `psutil` para obtener las estadísticas de la red, como la cantidad de datos enviados y recibidos a través de las interfaces de red.
2. **Interfaz de usuario**: Con `curses`, se genera una interfaz gráfica en la terminal que se actualiza en tiempo real, mostrando las estadísticas de red y la información sobre la interfaz activa.
3. **Actualización continua**: El uso de `time.sleep()` permite actualizar la pantalla cada segundo para reflejar las nuevas métricas de tráfico de red.

### Estructura del código

El código se organiza de la siguiente manera:

- **network.py**: Archivo principal que ejecuta el monitoreo de la red.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un **Pull Request**. Asegúrate de seguir las mejores prácticas de codificación y realizar pruebas antes de proponer cambios.

## Licencia

Este proyecto está bajo la licencia MIT.
