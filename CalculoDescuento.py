def calcular_descuento(monto_total, porcentaje_descuento=10):

  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Llamadas a la función
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)

monto_compra2 = 200
descuento2 = calcular_descuento(monto_compra2)

descuento_total = descuento1 + descuento2
monto_total= monto_compra1 + monto_compra2

# Mostrar resultados
print(f"Monto compra Ropa: {monto_compra1:.2f}")
print(f"Descuento: {descuento1:.2f}")
print(f"Monto final a pagar: {(monto_compra1 - descuento1):.2f}")

print("\n")
print(f"Monto compra Zapatos: {monto_compra2:.2f}")
print(f"Descuento: {descuento2:.2f}")
print(f"Monto final a pagar: {(monto_compra2 - descuento2):.2f}")

print("\n")
print(f"Descuento Total: {descuento_total:.2f}")
print(f"Monto Total Compra: {monto_total-descuento_total:.2f}")