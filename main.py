import gestor_dispositivos


def menu():
    print("Menu:")
    print("1:Registrar dispositivo:")
    print("2:Mostrar dispositivos:")
    print("3:Buscar dispositivo:")
    print("4:Automatizar dispositivo:")
    print("5:Eliminar automatizacion")
    print("6:Desconectar dispositivo:")
    print("7:Salir:")


aplicacion_ejecutando = True

while aplicacion_ejecutando:

    print()
    menu()
    print()

    try:
        opcion = int(input("Elija una opcion:"))

        if opcion < 1 or opcion > 7:
            print("Opcion invalida.")
        else:
            if opcion == 1:
                gestor_dispositivos.agregar_dispositivo()
            if opcion == 2:
                gestor_dispositivos.mostrar_dispositivos()
            if opcion == 3:
                gestor_dispositivos.buscar_dispositivo_por_nombre()
            if opcion == 4:
                gestor_dispositivos.automatizar_dispositivo()
            if opcion == 5:
                gestor_dispositivos.eliminar_automatizacion()
            if opcion == 6:
                gestor_dispositivos.eliminar_dispositivo()
            if opcion == 7:
                print("Cerrando aplicacion.")
                aplicacion_ejecutando = False

    except ValueError:
        print("El valor debe ser numerico")
