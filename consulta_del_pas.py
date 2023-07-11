from Bases_de_datos import Base_de_datos_IAPSER, Base_de_datos_Norte, Base_de_datos_Rivadavia, Base_de_datos_Sancor

marca = input("Ingrese la marca del auto a cotizar:")
modelo = input("Ingrese el modelo: ")

#IAPSER
if modelo in Base_de_datos_IAPSER.Peugeot:
    cotizacion_cuota_seguro = Base_de_datos_IAPSER.Peugeot[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en IAPSER es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_IAPSER.Fiat:
    cotizacion_cuota_seguro = Base_de_datos_IAPSER.Fiat[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en IAPSER es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_IAPSER.Renault:
    cotizacion_cuota_seguro = Base_de_datos_IAPSER.Renault[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en IAPSER es de: {cotizacion_cuota_seguro}")
else:
    print("No existen cotizaciones para el modelo solicitado.")
    

#Norte
if modelo in Base_de_datos_Norte.Peugeot:
    cotizacion_cuota_seguro = Base_de_datos_Norte.Peugeot[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Norte es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_Norte.Fiat:
    cotizacion_cuota_seguro = Base_de_datos_Norte.Fiat[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Norte es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_Norte.Renault:
    cotizacion_cuota_seguro = Base_de_datos_Norte.Renault[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Norte es de: {cotizacion_cuota_seguro}")
else:
    print("No existen cotizaciones para el modelo solicitado.")


#Rivadavia    
if modelo in Base_de_datos_Rivadavia.Peugeot:
    cotizacion_cuota_seguro = Base_de_datos_Rivadavia.Peugeot[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Rivadavia es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_Rivadavia.Fiat:
    cotizacion_cuota_seguro = Base_de_datos_Rivadavia.Fiat[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Rivadavia es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_Rivadavia.Renault:
    cotizacion_cuota_seguro = Base_de_datos_Rivadavia.Renault[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Rivadavia es de: {cotizacion_cuota_seguro}")
else:
    print("No existen cotizaciones para el modelo solicitado.")
    
    
    
#Sancor    
if modelo in Base_de_datos_Sancor.Peugeot:
    cotizacion_cuota_seguro = Base_de_datos_Sancor.Peugeot[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Sancor es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_Sancor.Fiat:
    cotizacion_cuota_seguro = Base_de_datos_Sancor.Fiat[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Sancor es de: {cotizacion_cuota_seguro}")
elif modelo in Base_de_datos_Sancor.Renault:
    cotizacion_cuota_seguro = Base_de_datos_Sancor.Renault[modelo]
    print(f"El valor estimado de la cuota para un {marca} {modelo} en Sancor es de: {cotizacion_cuota_seguro}")
else:
    print("No existen cotizaciones para el modelo solicitado.")