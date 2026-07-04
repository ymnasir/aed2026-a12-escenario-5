#!/usr/bin/env python3

def preguntar_opciones(opciones):
    op_nums = []
    for num, txt in opciones:
        op_nums.append(num)
    for num, txt in opciones:
        print(f"{num}. {txt}")

    op_sel = -1
    opcion_valida = False
    while not opcion_valida:
        op_sel = input("> ")
        try:
            op_sel = int(op_sel)
            if op_sel in op_nums:
                opcion_valida = True
            else:
                print("Opción inválida, vuelva a intentar.")
        except:
            pass
    return op_sel

def menu_principal():
    op = preguntar_opciones([
        (0, "Salir"),
        (1, "Pedidos"),
        (2, "Estadísticas")
    ])

menu_principal()

