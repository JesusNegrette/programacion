import random

Limites_Mapa = (-5, 5)

def inicializar_jugador():
    return {
        'nombre': input("Ingresa tu nombre de Heroe: ").lower(),
        'vida': 100,
        'energia': 50,
        'inventario': [], # Usaremos siempre minúsculas
        'posicion': [0, 0]
    }

def mostrar_estado(jugador):
    print("\n" + "="*30)
    print(f"HEROE: {jugador['nombre']} | VIDA: {jugador['vida']} | Energia: {jugador['energia']}")
    print(f"POSICION: {jugador['posicion']} | INVENTARIO: {jugador['inventario']}") 
    print("="*30 + "\n")

def mover_jugador(jugador, direccion):
    x, y = jugador['posicion']
    dx, dy = 0, 0

    match direccion.lower():
        case 'norte': dy = 1
        case 'sur': dy = -1
        case 'este': dx = 1
        case 'oeste': dx = -1
        case 'salir': return "SALIR"
        case _:
            print("(!) Dirección no válida.")
            return False
     
    nueva_posicion = [x + dx, y + dy]

    if Limites_Mapa[0] <= nueva_posicion[0] <= Limites_Mapa[1] and \
       Limites_Mapa[0] <= nueva_posicion[1] <= Limites_Mapa[1]:
        jugador['posicion'] = nueva_posicion
        jugador['energia'] -= 1
        return True 
    else: 
        print("⚠️ No puedes moverte fuera del mapa. ⚠️")
        return False

def batalla(jugador):
    print("⚔️ ¡UN ENEMIGO APARECE!")
    enemigo_vida = random.randint(20, 50)

    while enemigo_vida > 0 and jugador['vida'] > 0:
        print(f"Tu vida: {jugador['vida']} | Vida del enemigo: {enemigo_vida}")
        accion = input("¿Qué quieres hacer Atacar o Huir? (a/h): ").lower()
        
        if accion == "a":
            daño_jugador = random.randint(10, 25)
            enemigo_vida -= daño_jugador
            print(f"-> Causas {daño_jugador} de daño")
            
            if enemigo_vida > 0:
                daño_enemigo = random.randint(5, 15)
                jugador['vida'] -= daño_enemigo
                print(f"<- El Enemigo te quita {daño_enemigo} de vida")
        
        elif accion == "h":
            if random.random() < 0.5:
                print("¡Lograste Escapar!")
                return
            else:
                print("⚠️ ¡No logras huir!")
                jugador['vida'] -= random.randint(5, 15)

    if jugador['vida'] > 0:
        print("Victoria, el enemigo fue Derrotado 🥳")

def evento(jugador, llave_encontrada):
    prob = random.random()   
    if prob < 0.30:
        print("La sala está en silencio.")
    elif prob < 0.60:
        items = ["comida", "pocion"]
        if not llave_encontrada:
            items.append("Llave Maestra")
        
        objeto = random.choice(items)
        jugador['inventario'].append(objeto)
        print(f"🎁 ¡Has encontrado: {objeto}!")
        return objeto == "Llave Maestra"
    else:
        batalla(jugador)
    return False

def jugar():
    jugador = inicializar_jugador()
    llave_cofre = False
    
    print("\nEncuentra la llave maestra y escribe 'salir' para escapar.")

    while jugador['vida'] > 0 and jugador['energia'] > 0:
        mostrar_estado(jugador)
        comando = input("¿A dónde vas? (Norte/Sur/Este/Oeste/Salir): ").lower()

                
        resultado_movimiento = mover_jugador(jugador, comando)
        
        if resultado_movimiento == "SALIR":
            if "Llave Maestra" in jugador['inventario']:
                print(f"¡Felicidades {jugador['nombre']}, has escapado! 🥳")
                return
            else:
                print("No puedes salir sin la Llave Maestra.")
                continue

        if resultado_movimiento is True:
            if evento(jugador, llave_cofre):
                llave_cofre = True

    if jugador['vida'] <= 0:
        print("Has sido derrotado... Fin del juego. 😢")
    else:
        print("Te has quedado sin energía en medio de la oscuridad. 😢")

if __name__ == "__main__":    
    jugar()