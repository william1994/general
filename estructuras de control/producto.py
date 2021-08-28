#INGRESO DE DATOS

valor = int(input('Valor del producto'))

# PROCEDIMIENTO

if valor >= 100:
    descuento= 0.10
else:
    descuento = 0
valordeldescuentoapagar = valor*descuento
totalpagar = valor-valordeldescuentoapagar
#salida
print(totalpagar)
