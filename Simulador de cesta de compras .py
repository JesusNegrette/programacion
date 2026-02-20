def simulador_cesta():
    cesta = []
    precios = []

    print(" ¡Bienvenido a tu Supermercado Virtual Python! ")

    while True:
        print("--- MENÚ DE GESTIÓN ---")
        print("1. Agregar producto")
        print("2. Mostrar cesta")
        print("3. Eliminar producto")
        print("4. Calcular total")
        print("5. Renunciar (Salir)")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            item = input("¿Qué producto deseas añadir?: "). capitalize()
            try:
                precio = float(input(f"¿Cuál es el precio de {item}?: "))
                cesta.append(item)
                precios.append(precio)
                print(f"¡{item} ha sido añadido con éxito!")
            except ValueError:
                print(" Error: Por favor, introduce un precio numérico válido.")

        elif opcion == "2":
            if not cesta:
                print(" Tu cesta está vacía actualmente.")
            else:
                print("--- Tu Contenido Actual ---")
                for i, (prod, prec) in enumerate(zip(cesta, precios), 1):
                    print(f"{i}. {prod} - ${prec:.2f}")

        elif opcion == "3":
            if not cesta:
                print(" No hay nada que eliminar, la cesta está vacía.")
            else:
                try:
                    indice = int(input("Introduce el número del producto a eliminar: ")) - 1
                    if 0 <= indice < len(cesta):
                        eliminado = cesta.pop(indice)
                        precios.pop(indice)
                        print(f"{eliminado} ha sido retirado de la cesta.")
                    else:
                        print(" Ese número de producto no existe.")
                except ValueError:
                    print(" Por favor, introduce un número válido.")

        elif opcion == "4":
            total = sum(precios)
            print(f" EL TOTAL DE TU COMPRA ES: ${total:.2f}")
            print(f"Llevas {len(cesta)} productos en total.")

        elif opcion == "5":
            print(" ¡Gracias por usar nuestro simulador! ¡Hasta pronto! ")
            break

        else:
            print(" Opción no válida. Inténtalo de nuevo (1-5).")

if __name__ == "__main__":
    simulador_cesta()
    