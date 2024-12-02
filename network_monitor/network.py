import psutil
import curses
import time

def get_network_info():
    """Obtenemos las estadísticas de la red."""
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def display_network_info(stdscr):
    # Desactivar el cursor y permitir actualizaciones sin borrar pantalla
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000)

    # Obtener la información de la red antes del bucle principal
    prev_sent, prev_recv = get_network_info()

    while True:
        # Limpiar pantalla
        stdscr.clear()

        # Obtener la información de la red actual
        bytes_sent, bytes_recv = get_network_info()

        # Calcular la velocidad de datos en Kbps
        sent_speed = (bytes_sent - prev_sent) / 1024  # en KB
        recv_speed = (bytes_recv - prev_recv) / 1024  # en KB

        # Actualizar las variables previas
        prev_sent, prev_recv = bytes_sent, bytes_recv

        # Mostrar los resultados en pantalla
        stdscr.addstr(0, 0, "Monitoreo de Red - Estadísticas")
        stdscr.addstr(1, 0, "----------------------------------------------------")
        stdscr.addstr(2, 0, f"Enviado: {bytes_sent / 1024 / 1024:.2f} MB")
        stdscr.addstr(3, 0, f"Recibido: {bytes_recv / 1024 / 1024:.2f} MB")
        stdscr.addstr(4, 0, f"Velocidad de Envío: {sent_speed:.2f} KB/s")
        stdscr.addstr(5, 0, f"Velocidad de Recepción: {recv_speed:.2f} KB/s")
        stdscr.addstr(6, 0, "----------------------------------------------------")
        stdscr.addstr(7, 0, "Presiona 'q' para salir...")

        # Actualizar la pantalla
        stdscr.refresh()

        # Esperar un segundo antes de actualizar los datos
        time.sleep(1)

        # Salir si se presiona 'q'
        if stdscr.getch() == ord('q'):
            break

# Iniciar la interfaz con curses
curses.wrapper(display_network_info)
