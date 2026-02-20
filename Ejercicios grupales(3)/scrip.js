// EL OPTIMIZADOR DE CONTENEDORES PORTUARIOS
// Solo Arrays — Sin Objetos

// Ñ   ñ 

//1. puerto 10 muelles (null = vacios)

let puerto = [null, null, null, null, null, null, null, null, null, null]

let puertoBloqueado = false

//2. Contenedores: [ID, Tipo, Peso, Destino]

const c1 = [1, "Comida", 20, "China"];
const c2 = [2, "Refrigerado", 15, "Mexico"];
const c3 = [3, "Electrodomesticos", 89, "España"];
const c4 = [4, "Recalentado", 30, "Argentina"];
const c5 = [5, "Muebles", 56, "Singapur"];
const c6 = [6, "Ropa", 8, "Chile"];

// 3. Cola de Órdenes: [TIPO_OPERACION, DATOS/ID]

let colaOrdenes = [
    ["CARGAR", c1],
    ["CARGAR", c2],
    ["CARGAR", c3],
    ["CARGAR", c4],
    ["CARGAR", c5],
    ["INSPECCIONAR", null],
    ["DESCARGAR", 2],
    ["CARGAR", c6],
    ["INSPECCIONAR", null],
];


//4. Calcular el peso total

function calcularPeso(matriz) {
    let pesoTotal = 0;
    for (let i = 0; i < matriz.lenght; i++) {
        if (matriz[i] !== null) {
            if (typeof matriz[i][2] == "number") {
                pesoTotal += matriz[i][2];
            }
        }
    }
    return pesoTotal;
}

//5. Cargar Contenedor

function cargarContenedor(matriz, Contenedor) {
    if (!Array.isArray(Contenedor) || Contenedor.length < 4) {

        console.log("Contenedor no valido");
        return false;
    }

    if (typeof Contenedor[2] !== "number") {

        console.log("Peso no valido");
        return false;
    }

    if (puertoBloqueado) {

        console.log("puertoBloqueado (>100 ton)" + contenedor[0] + ".",

        );
        return false;

    }
    let intentos = 0;
    let cargado = false;
    const maxIntentos = 20;

    do {
        let indice = Math.floor(Math.random() * 10);
        if (matriz[indice] === null) {
            matriz[indice] = Contenedor;
            console.log("Contenedor" + Contenedor[0] + "cargado el muelle" + indice

            );

            cargado = true;

        }
        intentos++;
    } while (!cargado && intentos < maxIntentos);

    if (!cargado) {
        let lleno = true;
        for (let i = 0; i < matriz.length; i++) {
            if (matriz[i] === null) {
                lleno = false;
                break;
            }
        }
        if (lleno) {
            console.log("Puerto lleno. No se pudo cargar el contenedor" + Contenedor[0] + ".",

            );
        } else {
            console.log("No se encontro espacio" + maxIntentos + "intentos para cargar el contenedor" + Contenedor[0] + ".",
            );
        }
    }
    let pesoTotal = calcularPeso(matriz);
    if (pesoTotal > 100) {
        puertoBloqueado = true;
        console.log(
            "Peso total (" + pesoTotal.toFixed(1) + " ton) supera 100 BLOQUEADO.",
        );
    }
    return cargado;
}

//6. Descargar Contenedor

function descargarContenedor(matriz, idContenedor) {
    for (let i = 0; i < matriz.length; i++) {
        if (matriz[i] !== null && matriz[i][0] === idContenedor) {
            console.log(
                "Contenedor" + idContenedor + "descargado del muelle" + i,
            );
            matriz[i] = null;
            if (puertoBloqueado && calcularPeso(matriz) <= 100) {
                puertoBloqueado = false;
                console.log("Puerto desbloqueado");
            }
            return true;
        }
    }
    console.log("Contenedor" + idContenedor + "no encontrado para descargar");
    return false;
}

//7. Inspeccionar peso 

function inspeccionar(matriz) {
    console.log("inspeccion - contenedor con peso > 20:");
    let encontrados = 0;
    for (let i = 0; i < matriz.length; i++)
        if (matriz[i] !== null && matriz[i][2] > 20) {
            console.log("Muelle" + i + " ID:" + matriz[i][0] + " Tipo:" + matriz[i][1] + " Peso:" + matriz[i][2] + " Destino:" + matriz[i][3],

            );
            encontrados++;

        }
    if (encontrados === 0) {
        console.log("No se encontraron contenedores con peso > 20");
    }
}

//8. Procesamiento 

console.log("SISTEMA DE GESTIÓN PORTUARIA");

while (colaOrdenes.length > 0) {
    let orden = colaOrdenes.shift();
    let tipo = orden[0];
    let datos = orden[1];

    switch (tipo) {
        case "CARGAR":
            cargarContenedor(puerto, datos);
            break;
        case "DESCARGAR":
            descargarContenedor(puerto, datos);
            break;
        case "INSPECCIONAR":
            inspeccionar(puerto);
            break;
        default:
            console.log("Operación no reconocida:", tipo);
    }

}
console.log("\n==============================================================================");
console.log("MANIFIESTO FINAL DEL PUERTO:");
console.log("================================================================================");
console.log("Muelle - ID - Tipo - Peso - Destino");

puerto.forEach(function (contenedor, indice) {

    if (contenedor !== null) {
        let tipo = contenedor[1].length < 8 ? contenedor[1] + "\t" : contenedor[1];

        console.log(indice + "\t" + contenedor[0] + "\t" + tipo + "\t" + contenedor[2] + "\t" + contenedor[3]

        );
    } else {
        console.log(indice + "null");
    }
});

console.log("PESO TOTAL: " + calcularPeso(puerto).toFixed(1) + "toneladas");
console.log("ESTADO: " + (puertoBloqueado ? "BLOQUEADO" : "OPERATIVO"));