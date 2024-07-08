def opcion_procesos():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Introduzca los puntos de evaluación y comentarios.')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Terminar.')
        num = input()

        if num.isdecimal():
            num = int(num)
            if 1 <= num <= 3:
                return num
            else:
                print('Por favor, introduzca del 1 a 3.')
        else:
            print('Por favor, introduzca del 1 a 3.')

def registrar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{ post } \n')
                file_pc.close()
                break
            else:
                print('Por favor, introduzca un valor entre el 1 y 5')
        else:
            print('Introduzca los puntos de evaluación como números')

def visualizar_resultados():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()

def main():
    while True:
        opcion = opcion_procesos()

        if opcion == 1:
            registrar_puntuacion()
        elif opcion == 2:
            visualizar_resultados()
        elif opcion == 3:
            print('Terminación.')
            break

if __name__ == "__main__":
    main()