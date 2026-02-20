# --- INICIO DEL JUEGO ---
print("--- EL MISTERIO DEL CASTILLO ---")

# NIVEL 1
print(" Estás en la entrada. Hay un FOSFORO y una LINTERNA.")
eleccion1 = input("¿Qué eliges? ").strip().upper()

if eleccion1 == "FOSFORO":
    # NIVEL 2
    print(" ¡Ves un OSO! ¿Quieres CORRER, ESCONDERTE o TREPAR?")
    eleccion2 = input("Respuesta: ").strip().upper()

    if eleccion2 == "ESCONDERSE":
        # NIVEL 3
        print(" El oso se va. Encuentras una trampilla. ¿Deseas ENTRAR, VOLVER o SALTAR?")
        eleccion3 = input("Respuesta: ").strip().upper()

        if eleccion3 == "ENTRAR":
            # NIVEL 4
            print(" Hay tres llaves: ROJA, AZUL y VERDE. ¿Cuál eliges?")
            eleccion4 = input("Respuesta: ").strip().upper()

            if eleccion4 == "AZUL":
                # NIVEL 5
                print(" Abres un cofre con un mapa. ¿Quieres ESTUDIAR el mapa o QUEMAR el mapa?")
                eleccion5 = input("Respuesta: ").strip().upper()

                if eleccion5 == "ESTUDIAR":
                    # NIVEL 6
                    print(" ¡El mapa te guía al tesoro! HAS GANADO ")
                elif eleccion5 == "QUEMAR":
                    print(" Sin mapa te pierdes para siempre. FIN.")
                else:
                    print(" Opción inválida. El viento se lleva el mapa. FIN.")
            
            elif eleccion4 == "ROJA":
                print(" La llave roja activa una trampa. FIN.")
            else:
                print(" Esa llave no abre nada. Te quedas encerrado. FIN.")

        elif eleccion3 == "SALTAR":
            print(" Saltas a un pozo sin fondo. FIN.")
        else:
            print(" Te pierdes en la oscuridad al volver. FIN.")

    elif eleccion2 == "CORRER":
        print(" El oso es más rápido. FIN.")
    else:
        print(" Te caes del árbol y el oso te atrapa. FIN.")

elif eleccion1 == "LINTERNA":
    # NIVEL 2 (Ruta B)
    print(" Ves un camino. ¿Quieres SEGUIR el camino o BUSCAR en los árboles?")
    eleccion2b = input("Respuesta: ").strip().upper()

    if eleccion2b == "SEGUIR":
        # NIVEL 3
        print(" Llegas a un río de lava. ¿Quieres CRUZAR, NADAR o ESPERAR?")
        eleccion3b = input("Respuesta: ").strip().upper()

        if eleccion3b == "CRUZAR":
            # NIVEL 4
            print(" Un guardián te pide una fruta: MANZANA, PERA o UVA.")
            eleccion4b = input("Respuesta: ").strip().upper()

            if eleccion4b == "MANZANA":
                # NIVEL 5
                print(" El guardián te da un deseo. ¿Pides RIQUEZA o VOLAR?")
                eleccion5b = input("Respuesta: ").strip().upper()

                if eleccion5b == "VOLAR":
                    # NIVEL 6
                    print(" ¡Vuelas por encima del bosque y llegas a salvo! VICTORIA ")
                elif eleccion5b == "RIQUEZA":
                    print(" El oro pesa tanto que te hundes en el suelo. FIN.")
                else:
                    print(" El guardián se cansa de esperar y te echa de allí. FIN.")
            else:
                print(" Al guardián no le gusta esa fruta. Te lanza al río. FIN.")
        else:
            print(" No puedes hacer eso en un río de lava. FIN.")
    else:
        print(" Un duende te roba la linterna y te pierdes. FIN.")

else:
    print("\nOpción no válida. Debes elegir FOSFORO o LINTERNA.")
    