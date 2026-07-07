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


MENU = {
    "Pizzas": [
        (1, "Pizza Muzzarella", 3500),
        (2, "Pizza Napolitana", 3800),
        (3, "Pizza Fugazzeta", 4000),
        (4, "Pizza Especial", 4500),
    ],
    "Hamburguesas": [
        (1, "Hamburguesa de Queso", 2800),
        (2, "Hamburguesa Argentina", 3200),
        (3, "Hamburguesa Doble Carne", 3600),
        (4, "Hamburguesa Completa", 3900),
    ],
    "Gaseosas": [
        (1, "Coca-Cola", 1200),
        (2, "Sprite", 1200),
        (3, "Fanta", 1200),
        (4, "Agua Mineral", 900),
    ],
    "Postres": [
        (1, "Flan Casero", 1500),
        (2, "Helado", 1800),
        (3, "Tiramisú", 2200),
        (4, "Ensalada de Frutas", 1600),
    ],
}


def pedidos():
    categorias = list(MENU.keys())
    op_categorias = [(i + 1, categorias[i]) for i in range(len(categorias))]

    print("\nElija una categoría:")
    sel_cat = preguntar_opciones(op_categorias)
    categoria = categorias[sel_cat - 1]

    productos = MENU[categoria]
    op_productos = [(num, f"{nombre} - ${precio}") for num, nombre, precio in productos]

    print(f"\nComidas disponibles en {categoria}:")
    sel_prod = preguntar_opciones(op_productos)

    for num, nombre, precio in productos:
        if num == sel_prod:
            print(f"\nSeleccionaste: {nombre} - ${precio}")


def menu_principal():
    op = preguntar_opciones([
        (0, "Salir"),
        (1, "Pedidos"),
        (2, "Estadísticas")
    ])

    if op == 1:
        pedidos()

menu_principal()
