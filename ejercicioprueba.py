stock = {
    "concepcion": 500,
    "puentealto": 1300,
    "valpo": 100,
    "muellevergaraenviñadelmar": 50
}

clientes = {
    "concepcion": [],
    "puentealto": [],
    "valparaiso": [],
    "muellevergaraenviñadelmar": []
}

def codigoconf(codigo):
    if len(codigo) < 6:
        return False
    mayuscula = False
    num = False
    for c in codigo:
        if c.isupper():
            mayuscula = True
        if c.isdigit():
            num = True
        if c == " ":
            return False
    return mayuscula and num

def compraconcepcion():
    print("\n***Compra en Concepción*** ")
    if stock["concepcion"] <= 0:
        print("\nNo hay entradas disponibles")
        return
    nombre = input("Nombre del comprador: ").strip()
    if nombre in clientes["concepcion"]:
        print("\nComprador ya registrado")
        return
    codigo = input("Código de confirmación: ").strip()
    if not codigoconf(codigo):
        print("\nCódigo de confirmación inválido")
        return
    clientes["concepcion"].append(nombre)
    stock["concepcion"]-= 1
    print(f"\nEntrada registrada! Stock restante: {stock["concepcion"]}")

def comprapuentealto():
    print("\n***Compra en Puente Alto***")
    if stock["puentealto"] <= 0:
        print("\nNo hay entradas disponibles")
        return
    nombre = input("Nombre del comprador: ").strip()
    if nombre in clientes["puentealto"]:
        print("\nComprador ya registrado")
        return
    try:
        cant = int(input("Ingrese cantidad de entradas (max 3): "))
        if cant < 1 or cant > 3:
            print("\nsolo se permiten entre 1 y 3 entradas por persona.")
            return
        if cant > stock["puentealto"]:
            print("\nstock insuficiente")
            return
    except:
        print("\nIngrese un número válido")
        return
    clientes["puentealto"].append(nombre)
    stock["puentealto"] -= cant
    print(f"\nEntrada registrada! Stock restante: {stock['puentealto']}")

def compravalparaiso():
    print("\n***Compra en Muelle Barón, Valparaíso***")
    if stock["valpo"] <= 0:
        print("\nNo hay entradas disponibles")
        return
    nombre = input("Nombre del comprador: ").strip()
    if nombre in clientes["valparaiso"]:
        print("\nComprador ya registrado")
        return
    codigo = input("Código de confirmación: ").strip()
    if not codigoconf(codigo):
        print("\nCódigo de confirmación inválido")
        return
    clientes["valparaiso"].append(nombre)
    stock["valpo"] -= 1
    print(f"\nEntrada registrada! Stock restante: {stock['valpo']}")

def compraviñadelmar():
    print("\n***Compra en Muelle Vergara en Viña del Mar***")
    if stock["muellevergaraenviñadelmar"] <= 0:
        print("\nNo hay entradas disponibles")
        return
    nombre = input("Nombre del comprador: ").strip()
    if nombre in clientes["muellevergaraenviñadelmar"]:
        print("\nComprador ya registrado")
        return
    tipo = input("Tipo de entrada: (Sun=Sunset, Ni=Night): ").strip()
    if tipo != "Sun" and tipo != "Ni":
        print("\nTipo de entrada inválido")
        return
    clientes["muellevergaraenviñadelmar"].append(nombre)
    stock["muellevergaraenviñadelmar"] -= 1
    print(f"\nEntrada registrada! Stock restante: {stock["muellevergaraenviñadelmar"]}")

def menu():
    print("\nTOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE")
    print("\n1.- Comprar entrada en Concepcion.")
    print("2.- Comprar entrada en Puente Alto.")
    print("3.- Comprar entrada en Muelle Baron Valparaiso.")
    print("4.- Comprar entrada en Muelle Vergara Viñadel Mar.")
    print("5.- salir.")

def main():
    while True:
        menu()
        op = input("Selecciona una opción: ")
        if op == "1":
            compraconcepcion()
        elif op == "2":
            comprapuentealto()
        elif op == "3":
            compravalparaiso()
        elif op == "4":
            compraviñadelmar()
        elif op == "5":
            print("\nsaliendo del programa...")
            break
        else:
            print("\nopcion no válida")

if __name__ == "__main__":
    main()