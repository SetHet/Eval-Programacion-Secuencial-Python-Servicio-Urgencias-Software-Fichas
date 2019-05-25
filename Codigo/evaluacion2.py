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

print("SERVICIO DE ATENCIÓN DE URGENCIAS")
print("---------------------------------")
print("1) Ingresar Ficha del Paciente")
print("2) Actualizar Ficha por el Médico")
print("3) Asignación de Medicamentos")
print("4) Obtención de Estadísticas")
print("5) Salir")
print("")

while opcion != 5:
    opcion = int(input("Ingrese opcion: "))
    if (opcion < 1 or opcion > 5):
        print("Ingrese un valor entre 1 y 5.")
    
    #parte 1, 2, 3
    if (opcion >= 1 and opcion <=3):
        #parte 1 

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


        #parte 2
        print("Ficha por el medico")
        #parte 3
        print("Asignar medicamento")

        #sumar datos
        print("Editando estadisticas.....")
        ficha_ingreso_numero += 1
        cantidad_pacientes_total += 1
        if (ficha_paciente_sexo == "M"):
            cantidad_pacientes_hombres += 1
        if (ficha_paciente_sexo == "F"):
            cantidad_pacientes_mujeres += 1
        


    if (opcion == 4):
        print("Estadisticas....")
        print("Cantidad total de pacientes:", cantidad_pacientes_total)
        print("Cantidad total de pacientes holmbre:", cantidad_pacientes_hombres)
        print("Cantidad total de pacientes mujeres:", cantidad_pacientes_mujeres)