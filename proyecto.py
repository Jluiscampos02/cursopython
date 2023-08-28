


import libraryE.funciones_proyectos as fp

print('BIENVENIDOS AL SISTEMA INVENTARIO')

while True:
    print('DIgite la opcion a utlizar:\n 1-agregar proyecto: \n 2-Eliminar proyecto: \n 3- actualizar productos \n0-salir del sistema:')
    opcion = int(input('Ingrese la opcion:'))

    if opcion == 0:
        print('\nGracias por usar el sistema!!!')
        break
    elif opcion ==1 :
        proyecto =  input('ingrese el nombre del proyecto:')
        descripcion = input('ingrese la descripcion del proyecto:')
        fecha = input('ingrese la fecha de vencimiento del proyecto AAAA-MM-DD:')
        fp.agregar_proyecto(proyecto, descripcion, fecha)
    elif opcion==2:
        proyectop = input('Digite el codigo del producto a eliminar')
        fp.eliminar_proyecto(proyectop)
        print('libro eliminado con exito\n')
    elif opcion == 3 :
        print('el libro a mostras:\n')
        fp.mostrar_proyecto()

    else :
        print('opcion invalidad')