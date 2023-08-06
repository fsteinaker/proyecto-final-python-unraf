#IMPORTAR DE LA BIBLIOTECA LA FUNCION: PRESIONAR UNA TECLA PARA CONTINUAR
import msvcrt
#IMPORTAR DE LA BIBLIOTECA LA PROPIEDAD RANDOM
import random

#INICIALIZAMOS VARIABLES
contador_apuesta = 0
acumulador_apuesta = 0
contador_quiniela = 0
contador_quini6 = 0

#MENU PRINCIPAL
def menu():
    #DENTRO DEL MENU PRINCIPAL LAS VARIABLES DECLARADAS LAS HACEMOS DE ACCESO GLOBAL
    global contador_apuesta
    global acumulador_apuesta
    global contador_quiniela
    global contador_quini6
    #MONTO FIJO DEL QUINI 6
    monto_quini6 = 400
    #SE IMPRIME LOS CONTENIDOS DEL MENU
    print(" ")
    print("**************************************")
    print("* Quiniela    'S A N      D I E G O' *")
    print("**************************************")
    print(" ")
    print("1. Quiniela")
    print("2. Quini 6")
    print("3. Comprobar apuesta")
    print("4. Arqueo de caja")
    print("5. Salir")
    print(" ")
    print("**************************************")
    print("| PRESIONE UNA OPCION PARA CONTINUAR |")    
    print("**************************************")
    print(" ")

    seleccion = int(input("INGRESE UNA OPCION: "))    

    # Si el usuario selecciona la opción 1, le solicitamos que ingrese los números de su apuesta en QUINIELA
    if seleccion == 1:
        print("------------------------------------")
        print("Q U I N I E L A - Quiniela San Diego")
        print("------------------------------------")
        #INPUTS DEL TICKET DE QUINIELA
        nombre = str(input("Ingrese el nombre: "))
        fecha = str(input("Ingrese la fecha: "))
        hora = str(input("Ingrese la hora de la apuesta: "))
        dni = str(input("Ingrese el DNI del apostador: "))

        #COMPROBAR SI HAY CAMPOS VACIOS
        if nombre == "" or fecha == "" or hora == "" or dni == "":
             print(" ")
             print("ERROR: Debe ingresar la informacion solicitada para imprimir el ticket")
             print(" ")
             print("VOLVERA AL MENU PRINCIPAL. Presione una tecla para continuar...")
             msvcrt.getch()
             menu()

        apuesta_quiniela = int(input("Ingrese el numero de su apuesta (2, 3 o 4 cifras): "))
        if apuesta_quiniela <10 or apuesta_quiniela >9999:
            print(" ")
            print("ERROR: Ingrese un numero entre 2 y 4 cifras. Vuelva a ingresar los datos de nuevo.")
            print(" ")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
            menu()
            
        ingresoApuesta = float(input("Ingrese el monto de la apuesta: $ "))

        #IMPRESION TICKET DE LA QUINIELA
        print(" ")
        print("------------------------------------")
        print("Q U I N I E L A - Quiniela San Diego")
        print("------------------------------------")
        print(" ")
        print("Cliente: ",nombre,"\nFecha: ",fecha,"\nHora: ",hora,"\nDocumento: ",dni,"\nNumero apostado: ",apuesta_quiniela,"\nMonto apostado: $",ingresoApuesta)
        print(" ")
        print("------------------------------------")
        print(" G R A C I A S   P O R   J U G A R  ")
        print(" ")
        print("---------Guarde su ticket-----------")
        print(" ")
        #SE CONTABILIZA LA APUESTA Y SE CARGA AL ACOMULADOR EL MONTO INGRESADO
        contador_apuesta += 1
        contador_quiniela += 1
        acumulador_apuesta += ingresoApuesta
        #PRESIONAR UNA TECLA PARA CONTINUAR
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        #VOLVER AL MENU PRINCIPAL
        menu()

    #IMPRESION TICKET DE QUINI 6
    if seleccion == 2:
        print(" ")
        print("------------------------------------")
        print("Q U I N I   6  -  Quiniela San Diego")
        print("------------------------------------")
        print(" ")
        #INPUTS APUESTA QUINI 6
        nombre = str(input("Ingrese el nombre: "))
        fecha = str(input("Ingrese la fecha: "))
        hora = str(input("Ingrese la hora de la apuesta: "))
        dni = str(input("Ingrese el DNI del apostador: "))

        #COMPROBAR SI HAY CAMPOS VACIOS
        if nombre == "" or fecha == "" or hora == "" or dni == "":
             print(" ")
             print("ERROR: Debe ingresar la informacion solicitada para imprimir el ticket")
             print(" ")
             print("VOLVERA AL MENU PRINCIPAL. Presione una tecla para continuar...")
             msvcrt.getch()
             menu()

        #FUNCION BUCLE WHILE PARA INGRESAR LOS SEIS NUMEROS DEL QUINI 6
        def nros_apostados_quini6():
            apuesta_quini6 = []
            print("Ingrese seis numeros del 00 al 45 inclusive:")

            while len(apuesta_quini6) < 6:
                for i in range(6):
                    numeros = int(input("Ingrese el número {}: ".format(i+1)))

                    #USO DEL IF PARA COMPROBAR QUE LOS VALORES SEAN LOS CORRECTOS, CASO CONTRARIO SE DEBERA VOLVER
                    #A INGRESAR ACCEDIENDO NUEVAMENTE DESDE EL MENU PRINCIPAL
                    if numeros in apuesta_quini6 or numeros < 0 or numeros > 45:
                        print(" ")
                        print("ERROR: Ingrese los numeros del 00 al 45 inclusive.")
                        print("       No puede volver ingresar numeros registrados.")
                        print(" ")
                        print("VOLVERA AL MENU PRINCIPAL. Presione cualquier tecla para volver ingresar...")
                        msvcrt.getch()
                        #VOLVER AL MENU TRAS EL ERROR
                        menu()
                    #SE USA UN IF PARA VERIFICAR QUE NO HAYA VALORES REPETIDOS
                    elif numeros not in apuesta_quini6:
                        #SE AGREGA LOS NUMEROS AL ARRAY apuesta_quini6
                        apuesta_quini6.append(numeros)                        
                    else:
                         print(" ")
                         print("ERROR: No puede ingresar ese valor.")
                         print("Presione una tecla para volver a ingresar un nuevo valor")
                         msvcrt.getch()
                         print(" ")
            #ORDENAR NUMEROS APOSTADOS DE MENOR A MAYOR
            apuesta_quini6.sort()

            return apuesta_quini6

        if __name__ == "__main__":
            #OBTENER NUMEROS DE LA FUNCION nros_apostados_quini6 MEDIANTE LA VARIABLE apuesta_quini6
            apuesta_quini6 = nros_apostados_quini6()

        print(" ")
        print("------------------------------------")
        print("Q U I N I   6  -  Quiniela San Diego")
        print("------------------------------------")
        print(" ")
        print("Cliente: ",nombre,"\nFecha: ",fecha,"\nHora: ",hora,"\nDocumento: ",dni,"\nNumeros elegidos: ",apuesta_quini6,"\nMonto apostado: $",monto_quini6)
        print(" ")
        print("------------------------------------")
        print(" G R A C I A S   P O R   J U G A R  ")
        print(" ")
        print("---------Guarde su ticket-----------")
        print(" ")
        #PRESIONAR UNA TECLA PARA CONTINUAR
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        contador_apuesta += 1
        contador_quini6 += 1
        acumulador_apuesta += monto_quini6
        menu()

    #COMPROBAR NUMERO GANADOR
    elif seleccion == 3:
            print(" ")
            print("-------------------------------------")
            print(" NRO. GANADOR  -  Quiniela San Diego ")
            print("-------------------------------------")
            print(" ")
            print("RECUERDE QUE LOS NUMEROS CONSULTADOS AQUI NO SE ACOMULAN")
            print("AL TOTAL DE LAS APUESTAS DEL DIA.")
            print(" ")
            print("Ingrese el sorteo que desee consultar:")
            print("1. Quiniela")
            print("2. Quini 6")
            print("3. Volver al menu principal")
            print(" ")
            opcion_submenu = int(input("INGRESE LA OPCION: "))

            #VERIFICAR NUMERO GANADOR EN QUINIELA
            if opcion_submenu == 1:
                print(" ")
                print("----------------------------------------")
                print("-N R O.  G A N A D O R  Q U I N I E L A-")
                print("----------------------------------------")
                print(" ")
                # Solicita al usuario que ingrese un número
                nro_quiniela = int(input("Por favor ingrese un número de 2, 3 o 4 cifras: "))
                if nro_quiniela >= 10 and nro_quiniela <= 99:
                        nro_azar_quiniela = random.randint(10, 99)
                        # Comprueba si el número ingresado es igual al número generado al azar del 10 al 99 (DOS CIFRAS)
                        if nro_quiniela == nro_azar_quiniela:
                            print(" ")
                            print("FELICIDADES TU NUMERO ES EL GANADOR!!!")
                            print(" ")
                            print("VOLVERAS AL MENU PRINCIPAL")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                            menu()
                        else:
                            print(" ")
                            print("Lo lamentamos, perdiste. El número ganador de la QUINIELA era el {} ".format(nro_azar_quiniela))
                            print("VOLVERAS AL MENU PRINCIPAL")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                            menu()
                elif nro_quiniela >= 100 and nro_quiniela <= 999:
                        nro_azar_quiniela = random.randint(100, 999)
                        # Comprueba si el número ingresado es igual al número generado al azar del 100 al 999 (TRES CIFRAS)
                        if nro_quiniela == nro_azar_quiniela:
                            print(" ")
                            print("FELICIDADES TU NUMERO ES EL GANADOR!!!")
                            print(" ")
                            print("VOLVERAS AL MENU PRINCIPAL")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                            menu()
                        else:
                            print(" ")
                            print("Lo lamentamos, perdiste. El número ganador de la QUINIELA era el {} ".format(nro_azar_quiniela))
                            print("VOLVERAS AL MENU PRINCIPAL")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                            menu()
                elif nro_quiniela >= 1000 and nro_quiniela <= 9999:
                        nro_azar_quiniela = random.randint(1000, 9999)
                        # Comprueba si el número ingresado es igual al número generado al azar del 1000 al 9999 (CUATRO CIFRAS)
                        if nro_quiniela == nro_azar_quiniela:
                            print(" ")
                            print("FELICIDADES TU NUMERO ES EL GANADOR!!!")
                            print(" ")
                            print("VOLVERAS AL MENU PRINCIPAL")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                            menu()
                        else:
                            print(" ")
                            print("Lo lamentamos, perdiste. El número ganador de la QUINIELA era el {} ".format(nro_azar_quiniela))
                            print("VOLVERAS AL MENU PRINCIPAL")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                            menu()
                else:
                    #ERROR AL INGRESAR UN VALOR QUE NO CORRESPONDE
                    print(" ")
                    print("ERROR: Ingrese un número de 2, 3 o 4 cifras.")
                    print("VOLVERAS AL MENU PRINCIPAL")
                    print("Presione una tecla para continuar...")
                    msvcrt.getch()
                    menu()

            #VERIFICAR NUMERO GANADOR EN QUINI 6
            elif opcion_submenu == 2:
                    print(" ")
                    print("--------------------------------------")
                    print("-N R O.  G A N A D O R  Q U I N I  6 -")
                    print("--------------------------------------")
                    print(" ")                   
                 
                    #ARREGLO DE SEIS NUMEROS ALEATORIOS
                    def verificar_apuesta_quini6():
                            apuesta_quini6 = []
                            print("Ingrese seis numeros del 00 al 45 inclusive:")
                            while len(apuesta_quini6) < 6:
                                for i in range(6):
                                    numeros = int(input("Ingrese el número {}: ".format(i+1)))
                                    #USO DEL IF PARA COMPROBAR QUE LOS VALORES SEAN LOS CORRECTOS, CASO CONTRARIO SE DEBERA VOLVER
                                    #A INGRESAR ACCEDIENDO NUEVAMENTE DESDE EL MENU PRINCIPAL                                
                                    if numeros in apuesta_quini6 or numeros < 0 or numeros > 45:
                                        print("ERROR: Ingrese los numeros del 00 al 45 inclusive.")
                                        print("       No puede volver ingresar numeros registrados.")
                                        print(" ")
                                        print("Presione una tecla para volver a ingresar un nuevo valor")
                                        msvcrt.getch()
                                        #VOLVER AL MENU TRAS EL ERROR
                                        menu()
                                    #SE USA UN IF PARA VERIFICAR QUE NO HAYA VALORES REPETIDOS
                                    elif numeros not in apuesta_quini6:
                                        #SE AGREGA LOS NUMEROS AL ARRAY apuesta_quini6
                                        apuesta_quini6.append(numeros)                        
                                    else:
                                        print(" ")
                                        print("ERROR: No puede ingresar ese valor.")
                                        print("Presione una tecla para volver a ingresar un nuevo valor")
                                        msvcrt.getch()
                                        print(" ")
                                #ORDENAR NUMEROS APOSTADOS DE MENOR A MAYOR                           
                                apuesta_quini6.sort()

                            return apuesta_quini6                    
                    
                    if __name__ == "__main__":
                        #OBTENER NUMEROS DE LA FUNCION nros_apostados_quini6 MEDIANTE LA VARIABLE apuesta_quini6
                        apuesta_quini6 = verificar_apuesta_quini6()

                    print(" ")
                    print("Numeros consultados:", apuesta_quini6)
                    msvcrt.getch()

                    #SE GENERA ARRAY DE NUMEROS SORTEADOS
                    nros_aleatorios_quini6 = []                   

                    #SE USA EL BUCLE WHILE PARA GENERAR LA LISTA DE 6
                    # NROS SORTEADOS Y QUE NO SE REPITAN
                    while len(nros_aleatorios_quini6) < 6:
                        nro_aleatorio = random.randint(0, 45)
                        if nro_aleatorio not in nros_aleatorios_quini6:
                            nros_aleatorios_quini6.append(nro_aleatorio)

                    #ORDENAR ARRAY DE NUMEROS SORTEADOS
                    nros_aleatorios_quini6.sort()

                    print(" ")
                    print("Numeros ganadores:", nros_aleatorios_quini6)
                    print(" ")

                    #CONTADOR IGUALDAD
                    igualdad = 0

                    #BUCLE FOR QUE VERIFICA LA IGUALDAD ENTRE LAS DOS ARRAYS
                    for i in range(6):
                        if apuesta_quini6[i] in nros_aleatorios_quini6:
                            igualdad += 1

                    # Imprimir el mensaje de COINCIDENCIAS
                    if igualdad == 3:
                        print("TENES UN PREMIO POR LOS 3 ACIERTOS!!!")
                    elif igualdad == 4:
                        print("TENES UN PREMIO POR LOS 4 ACIERTOS!!!")
                    elif igualdad == 5:
                        print("Hay 5 ACIERTOS!!!")
                    elif igualdad == 6:
                        print("FELICIDADES, HAY 6 ACIERTOS!!!")
                    else:
                        print("TU APUESTA NO FUE LA GANADORA.")

                    print(" ")
                    print("VOLVERA AL MENU PRINCIPAL. Presione cualquier tecla para continuar ...")
                    msvcrt.getch()
                    #VOLVER AL MENU TRAS EL ERROR
                    menu()

            #REGRESAR AL MENU PRINCIPAL
            elif opcion_submenu == 3:
                menu()

            #MENSAJE DE ERROR: SE VUELVE AL MENU PRINCIPAL
            else:
                print("ERROR: Seleccione algunas de la opciones disponibles.")
                print("VOLVERAS AL MENU PRINCIPAL")
                print("Presione una tecla para continuar...")
                msvcrt.getch()
                menu()

    #ARQUEO DE CAJA
    elif seleccion == 4:
       print(" ")
       print("------------------------------------")
       print("A R Q U E O   -   Quiniela San Diego")
       print("------------------------------------")
       print(" ")
       print("La cantidad de apuestas TOTAL:",contador_apuesta)
       print("La cantidad de apuestas en QUINIELA:",contador_quiniela)
       print("La cantidad de apuestas en QUINI 6:",contador_quini6)
       print("La recaudacion TOTAL diaria es: $",acumulador_apuesta)
       print("Retención: $", acumulador_apuesta * 0.47)
       print("Ganancia neta: $", acumulador_apuesta * 0.53)
       print(" ")
       #PRESIONAR UNA TECLA PARA CONTINUAR
       print("Presione una tecla para continuar...")
       msvcrt.getch()
       menu()

    #SALIR DEL PROGRAMA
    elif seleccion == 5:
        print(" ")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||                                                                                ||")
        print("||   Gracias por jugar en la Quiniela  S A N   D I E G O . Los esperamos pronto.  ||")
        print("||                                                                                ||")
        print("|| L O S  D A T O S  A L M A C E N A D O S  E N  E L  D I A  S E  B O R R A R A N ||")
        print("||                                                                                ||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(" ")
        print("  Desarrollado por: Federico R. Steinaker - UnRaf - Curso de Python - 07/08/2023")
        #PRESIONAR UNA TECLA PARA CONTINUAR
        print(" ")
        print("Presione una tecla para salir...")
        msvcrt.getch()
        #SALIDA DEL BUCLE (SE TOMA DE LA BIBLIOTECA DE PYTHON)
        exit()
    #EN CASO DE QUE NO SE SELECCIONE NINGUNA DE LAS OPCIONES DEL 1 AL 5 SE DETALLA EL SIGUIENTE MENSAJE Y SE VUELVE A PEDIR
    #OPCION (PORQUE ESTAMOS DENTRO DEL BUCLE WHILE), SE IMPRIME DE NUEVO EL MENU PRINCIPAL
    else:
        print(" ")
        print("ERROR: Opción no valida. Ingrese una opción del 1 al 5")
        #PRESIONAR UNA TECLA PARA CONTINUAR
        print("Presione una tecla para continuar...")
        msvcrt.getch()

#SI SE RETORNA UN VALOR TRUE SE VUELVE AL MENU PRINCIPAL
while True:
    menu()