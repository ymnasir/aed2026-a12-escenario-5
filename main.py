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
        (1, "Realizar un pedido"),
        (2, "Carrito"),
        (3, "Método de pago"),
        (4, "Estadísticas")
    ])

    if op == 1:
        menu_pedidos()
    elif op == 2:
        carrito()
    elif op == 3:
        metodopago = preguntar_opciones([
            (0, "Efectivo"),
            (1, "Tarjeta de crédito"),
            (2, "Tarjeta de débito")
        ])
    #    elif op == 3:
    #    estadisticas()


def menu_pedidos():
    op = preguntar_opciones([
        (0, "Salir"),
        (1, "Mostrar menú del día"),
        (2, "Promociones")
    ])

    if op == 1:
        print("este seria el menu del dia")
    if op == 2:
        print("aca irian las promociones")


def carrito():
    op = preguntar_opciones([
        (0, "Salir"),
        (1, "Ver carrito actual"),
    ])

    if op == 1:
        print("aca se mostraria el carrito")


menu_principal()
