def ingresar_nombre():
    while True:
        nombre = input("Ingrese el nombre del trabajador: ")
        if nombre.strip() == '' or len(nombre) > 30:
            print("Error: El nombre no puede estar vacío ni tener más de 30 caracteres.")
        else:
            return nombre

def ingresar_sueldo_base():
    while True:
        try:
            sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
            if sueldo_base < 0:
                print("Error: El sueldo base debe ser un valor numérico positivo.")
            else:
                return sueldo_base
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido para el sueldo base.")

def ingresar_horas_extra():
    while True:
        try:
            horas_extra = float(input("Ingrese la cantidad de horas extras trabajadas: "))
            if horas_extra < 0:
                print("Error: Las horas extras deben ser un valor numérico positivo.")
            else:
                return horas_extra
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido para las horas extras.")

def calcular_pago_horas_extra(sueldo_base, horas_extra):
    pago_horas_extra = horas_extra * (sueldo_base * 1.5)
    return pago_horas_extra

def calcular_descuento_fonasa(total_ingresos):
    descuento_fonasa = total_ingresos * 0.07
    return descuento_fonasa

def calcular_descuento_afp(total_ingresos):
    descuento_afp = total_ingresos * 0.1
    return descuento_afp

def calcular_sueldo_neto(total_ingresos, descuento_fonasa, descuento_afp):
    sueldo_neto = total_ingresos - descuento_fonasa - descuento_afp
    return sueldo_neto

def imprimir_liquidacion(nombre, sueldo_base, pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    print("\n--- Liquidación de sueldo ---")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo base: {sueldo_base:.2f}")
    print(f"Pago por horas extras: {pago_horas_extra:.2f}")
    print(f"Total de ingresos: {total_ingresos:.2f}")
    print(f"Descuento por FONASA: {descuento_fonasa:.2f}")
    print(f"Descuento por AFP: {descuento_afp:.2f}")
    print(f"Sueldo neto a pagar: {sueldo_neto:.2f}")

def main():
    nombre = ingresar_nombre()
    sueldo_base = ingresar_sueldo_base()
    horas_extra = ingresar_horas_extra()

    pago_horas_extra = calcular_pago_horas_extra(sueldo_base, horas_extra)
    total_ingresos = sueldo_base + pago_horas_extra
    descuento_fonasa = calcular_descuento_fonasa(total_ingresos)
    descuento_afp = calcular_descuento_afp(total_ingresos)
    sueldo_neto = calcular_sueldo_neto(total_ingresos, descuento_fonasa, descuento_afp)

    imprimir_liquidacion(nombre, sueldo_base, pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

if __name__ == "__main__":
    main()