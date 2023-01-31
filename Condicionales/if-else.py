ingreso_mensual = 20000
gastos_mensuales = 18000

# if anidados y else if(elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gastos_mensuales <= 0 or ingreso_mensual - gastos_mensuales < 3000:
        print("Estás en números rojos")
    elif ingreso_mensual - gastos_mensuales >= 3000:
        print("Ahora sí estás bien")
