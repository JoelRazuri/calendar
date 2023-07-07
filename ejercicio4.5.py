""" 
    Escribir funciones que resuelvan los siguientes problemas:
        a) Dado un año indicar si es bisiesto.
        Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
        excepto que también sea divisible por 400.
        b) Dado un mes y un año, devolver la cantidad de días correspondientes.
        c) Dada una fecha (día, mes, año), indicar si es válida o no.
        d) Dada una fecha, indicar los días que faltan hasta fin de mes.
        e) Dada una fecha, indicar los días que faltan hasta fin de año.
        f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
        g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
        entre ambas, en años, meses y días. PENDIENTEEEE
        Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
"""


def es_bisiesto(año):
    # Dado un año indicar si es bisiesto.

    if año%4==0 and (año%100!=0 or año%400==0):
        # print(f"El año {año} es bisiesto.")
        bisiesto=True
    else:
        # print(f"El año {año} no es bisiesto.")
        bisiesto=False

    return bisiesto

def cantidad_dias(mes,año):
    # Dado un mes y un año, devolver la cantidad de días correspondientes.

    if mes==2:
        if es_bisiesto(año)==True:
            # print(f"El mes {mes} del año {año} tiene 29 días.")
            dias=29
        else:
            # print(f"El mes {mes} del año {año} tiene 28 días.")
            dias=28
    elif mes==4 or mes==6 or mes==9 or mes==11:
        # print(f"El mes {mes} del año {año} tiene 30 días.")
        dias=30
    else:
        # print(f"El mes {mes} del año {año} tiene 31 días.")
        dias=31
    
    return dias
    
def existe_fecha(dia,mes,año):
    # Dada una fecha (día, mes, año), indicar si es válida o no.

    dias = cantidad_dias(mes,año)
    
    if dia<=dias:
        # print(f"Es válida la fecha. Fecha: {dia}/{mes}/{año}")
        fecha=True
    else:
        # print(f"No es válida la fecha. Fecha: {dia}/{mes}/{año}")
        fecha=False

    return fecha

def dias_faltantes_mes(dia,mes,año):
    # Dada una fecha, indicar los días que faltan hasta fin de mes.

    existe = existe_fecha(dia,mes,año)
    dias = cantidad_dias(mes,año)
    
    if existe==True:
        resto = dias - dia
        # print(f"Faltan {resto} días para que termine el mes {mes}.")   
    else:
        print("No existe la fecha.")
    
    return resto

def dias_faltantes_año(dia,mes,año):
    # Dada una fecha, indicar los días que faltan hasta fin de año.

    sumador = dia

    for i in range(1,mes):
        sumador = sumador + cantidad_dias(i,año)

    if es_bisiesto(año)==True:
        resto_dias = 366 - sumador
    else:
        resto_dias = 365 - sumador
    
    # print(f"sumador: {sumador}")
    print(f"Fecha: {dia}/{mes}/{año}. Faltan {resto_dias} días para que termine el año.")

# dias_faltantes_año(14,2,2023)


def dias_transcurridos(dia,mes,año):
    # Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.

    sumador = dia
    
    for i in range(1,mes):
        sumador = sumador + cantidad_dias(i,año)

    print(f"En la fecha {dia}/{mes}/{año} han transcurrido {sumador} días.")


# print(es_bisiesto(2023))
# dias_transcurridos(14,2,2023)
# dias_faltantes_año(14,2,2023)