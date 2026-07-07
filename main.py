#!/usr/bin/env python3

METODOS_PAGO = {
    1: ("Efectivo", 0.00),
    2: ("Transferencia", 0.05),
    3: ("Tarjeta", 0.10),
}

CAT_PIZZA = "Pizzas"
CAT_POSTRE = "Postres"
CAT_HAMBUR = "Hamburguesas"
CAT_GASEOSA = "Gaseosas"

CATEGORIAS = [CAT_PIZZA, CAT_POSTRE, CAT_HAMBUR, CAT_GASEOSA]

MENU = [
    {
        "codigo": 1,
        "categoria": CAT_PIZZA,
        "nombre": "Pizza Muzzarella",
        "precio": 3500,
    },
    {
        "codigo": 2,
        "categoria": CAT_PIZZA,
        "nombre": "Pizza Napolitana",
        "precio": 3800,
    },
    {
        "codigo": 3,
        "categoria": CAT_PIZZA,
        "nombre": "Pizza Fugazzeta",
        "precio": 4000,
    },
    {
        "codigo": 4,
        "categoria": CAT_PIZZA,
        "nombre": "Pizza Especial",
        "precio": 4500,
    },
    {
        "codigo": 5,
        "categoria": CAT_HAMBUR,
        "nombre": "Hamburguesa de Queso",
        "precio": 2800,
    },
    {
        "codigo": 6,
        "categoria": CAT_HAMBUR,
        "nombre": "Hamburguesa Argentina",
        "precio": 3200,
    },
    {
        "codigo": 7,
        "categoria": CAT_HAMBUR,
        "nombre": "Hamburguesa Doble Carne",
        "precio": 3600,
    },
    {
        "codigo": 8,
        "categoria": CAT_HAMBUR,
        "nombre": "Hamburguesa Completa",
        "precio": 3900,
    },
    {
        "codigo": 9,
        "categoria": CAT_GASEOSA,
        "nombre": "Coca-Cola",
        "precio": 1200,
    },
    {
        "codigo": 10,
        "categoria": CAT_GASEOSA,
        "nombre": "Sprite",
        "precio": 1200,
    },
    {
        "codigo": 11,
        "categoria": CAT_GASEOSA,
        "nombre": "Fanta",
        "precio": 1200,
    },
    {
        "codigo": 12,
        "categoria": CAT_GASEOSA,
        "nombre": "Agua Mineral",
        "precio": 900,
    },
    {
        "codigo": 13,
        "categoria": CAT_POSTRE,
        "nombre": "Flan Casero",
        "precio": 1500,
    },
    {
        "codigo": 14,
        "categoria": CAT_POSTRE,
        "nombre": "Helado",
        "precio": 1800,
    },
    {
        "codigo": 15,
        "categoria": CAT_POSTRE,
        "nombre": "Tiramisú",
        "precio": 2200,
    },
    {
        "codigo": 16,
        "categoria": CAT_POSTRE,
        "nombre": "Ensalada de Frutas",
        "precio": 1600,
    },
]

MENU_POR_CODIGO = { item["codigo"]: item for item in MENU }

mp_actual = 1
carrito = {}

def reset_carrito():
    global mp_actual, carrito
    mp_actual = 1
    carrito = {}

def preguntar_opciones(opciones):
    op_nums = []
    for num, txt in opciones:
        op_nums.append(num)
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
            print("Opción inválida, vuelva a intentar.")
    return op_sel

def preguntar_si_o_no(msj):
    while True:
        op = input(f"{msj} (S/N): ").lower()
        if op in ["s", "n"]:
            return op == "s"

def print_y_esperar(txt):
    print()
    print(txt)
    input("\nPresione cualquier tecla para continuar...")

def preguntar_producto():
    ops = [(0, "Cancelar")]
    for i in range(len(CATEGORIAS)):
        ops.append((i+1, CATEGORIAS[i]))

    print("\nElija una categoría:")
    op_sel = preguntar_opciones(ops)
    if op_sel == 0:
        return 0

    cat = ops[op_sel][1]
    prods = []
    ops = [(0, "Cancelar")]
    for p in MENU:
        if p["categoria"] == cat:
            ops.append((p["codigo"], p["nombre"]))
    print(f"\nComidas disponibles en {cat}:")
    codigo = preguntar_opciones(ops)
    return codigo

def preguntar_metodo_pago():
    ops = [(0, "Cancelar")]
    for num in METODOS_PAGO:
        nombre, recargo = METODOS_PAGO[num]
        ops.append((num, nombre))

    print("\nElija el método de pago:")
    op_sel = preguntar_opciones(ops)
    return op_sel

def calc_precio_total(cant, p_uni):
    nombre, recargo = METODOS_PAGO[mp_actual]
    return cant*p_uni*(1.00 + recargo)

def mostrar_carrito():
    if len(carrito) > 0:
        print("-"*68)
        for cod, cant in carrito.items():
            nomprod = MENU_POR_CODIGO[cod]["nombre"]
            precio = calc_precio_total(cant, MENU_POR_CODIGO[cod]["precio"])
            print(f"{cant:>3}x {nomprod:>40} | $ {precio:>17.2f}")
        print("-"*68)
    else:
        print_y_esperar("No hay productos en el carrito.")

def menu_pedir():
    global mp_actual, carrito
    reset_carrito()
    salir = False
    while not salir:
        op = preguntar_opciones([
            (0, "Cancelar"),
            (1, "Agregar al carrito"),
            (2, "Método de pago"),
            (3, "Ver carrito"),
            (4, "Vaciar carrito"),
            (5, "Efectuar compra")
        ])
        if op == 0:
            salir = True
        elif op == 1:
            prod = preguntar_producto()
            if prod != 0:
                cnt_prod = 0
                if prod in carrito:
                    cnt_prod = carrito[prod]
                carrito[prod] = cnt_prod + 1
                print_y_esperar(
                    "Se agregó el producto al carrito satisfactoriamente!"
                )
        elif op == 2:
            mp = preguntar_metodo_pago()
            if mp != 0:
                mp_actual = mp
                nomp, recmp = METODOS_PAGO[mp]
                print_y_esperar(
                    f"Se ha actualizado el método de pago a: {nomp}"
                )
        elif op == 3:
            mostrar_carrito()
        elif op == 4:
            reset_carrito()
        elif op == 5:
            mostrar_carrito()
            if len(carrito) > 0:
                salir = preguntar_si_o_no("Está satisfecho con su compra?")

def menu_principal():
    salir = False
    while not salir:
        op = preguntar_opciones([
            (0, "Salir"),
            (1, "Realizar un pedido"),
            (2, "Estadísticas")
        ])

        if op == 0:
            salir = True
        elif op == 1:
            menu_pedir()
        elif op == 2:
            # implementar...
            pass

menu_principal()
