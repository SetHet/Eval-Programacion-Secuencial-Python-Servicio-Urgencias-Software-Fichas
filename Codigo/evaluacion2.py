import os; os.system("color 02"); os.system("cls")

#parte Estadisticas

cantidad_pacientes_total = 0 # valor = hombres + mujeres
cantidad_pacientes_mujeres = 0
cantidad_pacientes_hombres = 0

cantidad_pacientes_requieren_reposo = 0

tiempo_total_atencion = 0
tiempo_promedio_atencion = 0 # valor = tiempo / cantidad_total

cantidad_medicamentos_total = 0 # valor = med_1 + med_2....
cantidad_medicamento_paracetamol = 0
cantidad_medicamento_lidocaina = 0
cantidad_medicamento_omeprazol = 0
cantidad_medicamento_penicilina = 0
cantidad_medicamento_salbutamol = 0

ficha_ingreso_numero = 0

#Loop

opcion = 0


while opcion != 5:
    os.system("cls")
    print("")
    print("SERVICIO DE ATENCIÓN DE URGENCIAS")
    print("---------------------------------")
    print("1) Ingresar Ficha del Paciente")
    print("2) Actualizar Ficha por el Médico")
    print("3) Asignación de Medicamentos")
    print("4) Obtención de Estadísticas")
    print("5) Salir")
    print("")
    opcion = int(input("Ingrese opcion: "))
    if (opcion < 1 or opcion > 5):
        print("Ingrese un valor entre 1 y 5.")
    
    #parte 1, 2, 3
    if (opcion >= 1 and opcion <=3):
        #parte 1 
        os.system("cls")
        print("1 >>> Ingresando Ficha del paciente")
        print("")
        print("FICHA DE INGRESO N°", ficha_ingreso_numero)
        ficha_paciente_fecha_atencion = input("Fecha de Atención: ")
        ficha_paciente_hora_atencion = input("Hora de atención: ")
        ficha_paciente_nombre_personal = input("Nombre del personal que ingresa ficha: ")
        print("IDENTIFICACION DEL PACIENTE")
        ficha_paciente_nivel_urgencia = input("Nivel de urgencia: ")
        ficha_paciente_nombre = input("Nombre: ")
        ficha_paciente_apellido = input("Apellido: ")
        ficha_paciente_rut = input("Rut: ")
        ficha_paciente_sexo = ""
        while not(ficha_paciente_sexo == "F" or ficha_paciente_sexo == "M"):
            ficha_paciente_sexo = input("Sexo (F/M): ")
        ficha_paciente_estado_civil = input("Estado Civil: ")
        ficha_paciente_edad = -1
        while ficha_paciente_edad < 0 or ficha_paciente_edad > 120:
            ficha_paciente_edad = int(input("Edad (0-120): "))
        ficha_paciente_domicilio = input("Domicilio: ")
        ficha_paciente_grupo_sanguineo = input("Grupo sanguineo: ")
        ficha_paciente_fono = input("Fono: ")
        ficha_asiste_acompañado = ""
        while ficha_asiste_acompañado != "SI" and ficha_asiste_acompañado != "NO":
            ficha_asiste_acompañado = input("Asiste acompañado (SI/NO): ")
        if (ficha_asiste_acompañado == "SI"):
            print("IDENTIFICACION DE ACOMPAÑANTE")
            ficha_paciente_acompañante_nombre = input("Nombre: ")
            ficha_paciente_acompañante_apellido = input("Apellido: ")
            ficha_paciente_acompañante_rut = input("Rut: ")
            ficha_paciente_acompañante_grado_parentesco = input("Grado de Parentesco: ")
            ficha_paciente_acompañante_fono = input("Fono: ")

        print("")
        print("Paciente agregado")
        os.system("pause")

        #parte 2
        os.system("cls")
        print("")
        print("2 >>> Ficha por el medico")
        print("")
        os.system("pause")
        #parte 3
        os.system("cls")
        print("3 >>> Asignar medicamento")
        agregar_medicamento = ""
        while agregar_medicamento != "no":
            print("")
            agregar_medicamento = input("Agregar medicamento? (si/no): ")
            
            if (agregar_medicamento == "si"):
                os.system("cls")
                cantidad_medicamento = int(input("Ingrese cantidad de medicamentos: "))
                if (cantidad_medicamento <= 0):
                    print("Ningun medicamento.")
                else:
                    print("Medicamentos")
                    print("-"*30)
                    print("1) Paracetamol")
                    print("2) Lidocaina")
                    print("3) Omeprazol")
                    print("4) Penilicilina")
                    print("5) Salbutamol")
                    opcion_medicamento = 0
                    while opcion_medicamento < 1 or opcion_medicamento > 5:
                        opcion_medicamento = int(input("Ingrese un medicamento (1-5): "))
                    if (opcion_medicamento == 1):
                        print("Agregado", cantidad_medicamento, "Paracetamol.")
                        cantidad_medicamento_paracetamol += cantidad_medicamento
                        cantidad_medicamentos_total += cantidad_medicamento
                    elif (opcion_medicamento == 2):
                        print("Agregado", cantidad_medicamento, "Lidocaina.")
                        cantidad_medicamento_lidocaina += cantidad_medicamento
                        cantidad_medicamentos_total += cantidad_medicamento
                    elif (opcion_medicamento == 3):
                        print("Agregado", cantidad_medicamento, "Omeprazol.")
                        cantidad_medicamento_omeprazol += cantidad_medicamento
                        cantidad_medicamentos_total += cantidad_medicamento
                    elif (opcion_medicamento == 4):
                        print("Agregado", cantidad_medicamento, "Penicilina.")
                        cantidad_medicamento_penicilina += cantidad_medicamento
                        cantidad_medicamentos_total += cantidad_medicamento
                    elif (opcion_medicamento == 5):
                        print("Agregado", cantidad_medicamento, "Salbutamol.")
                        cantidad_medicamento_salbutamol += cantidad_medicamento
                        cantidad_medicamentos_total += cantidad_medicamento
            elif agregar_medicamento == "no":
                print("")
                print("Agregar medicamentos finalizado")
                os.system("pause")
        
        #sumar datos
        print("Editando estadisticas.....")
        ficha_ingreso_numero += 1
        cantidad_pacientes_total += 1
        if (ficha_paciente_sexo == "M"):
            cantidad_pacientes_hombres += 1
        if (ficha_paciente_sexo == "F"):
            cantidad_pacientes_mujeres += 1
        


    if (opcion == 4):
        os.system("cls")
        print("")
        print("=============== Estadisticas ===============")
        print("Cantidad total de pacientes:", cantidad_pacientes_total)
        print("Cantidad total de pacientes holmbre:", cantidad_pacientes_hombres)
        print("Cantidad total de pacientes mujeres:", cantidad_pacientes_mujeres)
        print("Cantidad total de medicamentos:", cantidad_medicamentos_total)
        print("Cantidad total de paracetamol:", cantidad_medicamento_paracetamol)
        print("Cantidad total de lidocaina:", cantidad_medicamento_lidocaina)
        print("Cantidad total de omeprazol:", cantidad_medicamento_omeprazol)
        print("Cantidad total de penicilina:", cantidad_medicamento_penicilina)
        print("Cantidad total de salbutamol:", cantidad_medicamento_salbutamol)

        print("")
        os.system("pause")


print("CERRANDO SERVICIO....")
