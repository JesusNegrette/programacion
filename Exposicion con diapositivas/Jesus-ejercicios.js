// Lógica Numérica y Secuencias 

// Inversión Numérica Matemática acumuladora

function invertirNumero(n) {
let invertido = 0;
let resto = n;
while (resto > 0) {
let ultimoDigito = resto % 10;
invertido = (invertido * 10) + ultimoDigito;
resto = (resto - ultimoDigito) / 10;
}

console.log("Número invertido:", invertido);
}

// Prueba
invertirNumero(1234);

// Conversor Binario a Decimal (Manual)

function binarioADecimal(binario) {
let decimal = 0;
let multiplicador = 1; 
let temp = binario;
while (temp > 0) {
let digito = temp % 10;
decimal = decimal + (digito * multiplicador);
multiplicador = multiplicador * 2;
temp = (temp - digito) / 10;
}
return decimal;
}

// Prueba
console.log("Decimal:", binarioADecimal(2006));

// Raíz Cuadrada Entera (Aproximación)

function raizCuadradaEntera(n) {
if (n < 0) return "Error: Número negativo";
let i = 0;
while (i * i <= n) {i++;}
return i - 1;
}

// Prueba
console.log("Raíz entera:", raizCuadradaEntera(330));

// Descomposición en Factores Primos

function factoresPrimos(n) {
let d = 2;
let temp = n;
let resultado = ""; 
while (temp > 1) {
while (temp % d === 0) {
console.log(d);
temp = temp / d;}
d++;}
}

// Prueba
factoresPrimos(70);

// Números Amigos

function sonAmigos(a, b) {
let sumaA = 0;
let sumaB = 0;
for (let i = 1; i < a; i++) {
if (a % i === 0) sumaA += i;
}

for (let j = 1; j < b; j++) {
if (b % j === 0) sumaB += j;
}

if (sumaA === b && sumaB === a) {
        console.log(a + " y " + b + " son amigos.");
} else {
        console.log(a + " y " + b + " no son amigos.");
}
}

// Prueba
sonAmigos(220, 284);

// Patrones y Bucles Anidados (Nested Loops)

// El Diamante Hueco

function diamanteHueco(n) {
if (n % 2 === 0) n++; 
let centro = (n + 1) / 2;

for (let i = 1; i <= n; i++) {
let fila = "";
let espaciosExt = (i <= centro) ? centro - i : i - centro;
let espaciosInt = (i <= centro) ? (2 * i - 3) : (2 * (n - i + 1) - 3);

for (let j = 0; j < espaciosExt; j++) fila += " ";
fila += "*";

if (espaciosInt > 0) {
for (let k = 0; k < espaciosInt; k++) fila += " ";
fila += "*";
        }
console.log(fila);}
}

// Prueba
diamanteHueco(20);

// Reloj de Arena 

function relojArena(n) {
  
for (let i = n; i >= 1; i--) {
let fila = "";
for (let s = 0; s < n - i; s++) fila += " ";
for (let j = 1; j <= (2 * i - 1); j++) fila += i;
console.log(fila);
    }

for (let i = 2; i <= n; i++) {
let fila = "";
for (let s = 0; s < n - i; s++) fila += " ";
for (let j = 1; j <= (2 * i - 1); j++) fila += i;
console.log(fila);
}
}

// Prueba
relojArena(5);

// Lógica de Estado y Calendario

// Día del Año (1 a 366)

function diaDelAño(dia, mes, año) {
let esBisiesto = (año % 4 === 0 && año % 100 !== 0) || (año % 400 === 0);
let acumulado = 0;

for (let m = 1; m < mes; m++) {
if (m === 2) acumulado += esBisiesto ? 29 : 28;
else if (m === 4 || m === 6 || m === 9 || m === 11) acumulado += 30;
else acumulado += 31;
}
return acumulado + dia;
}

// Prueba
console.log("Día del año:", diaDelAño(1, 2, 2024));
// Prueba
console.log("Es válida:", validarTarjeta(45567372));

// Validador de Tarjetas 

function validarTarjeta(numero) {
let suma = 0;
let temp = numero;

for (let i = 1; i <= 8; i++) {
let digito = temp % 10;
if (i % 2 === 0) { 
digito *= 2;
if (digito > 9) digito -= 9;
}
suma += digito;
temp = (temp - (temp % 10)) / 10;
}
return (suma % 10 === 0);
}

// Prueba
console.log("Es válida:", validarTarjeta(45567372));

// El Cajero Automático (Greedy Algorithm)

function cajero(monto) {
let restante = monto;
    
let d100 = (restante - (restante % 100)) / 100;
restante %= 100;
if (d100 > 0) console.log(d100 + " billetes de 100");

let d50 = (restante - (restante % 50)) / 50;
restante %= 50;
if (d50 > 0) console.log(d50 + " billetes de 50");

let d20 = (restante - (restante % 20)) / 20;
restante %= 20;
if (d20 > 0) console.log(d20 + " billetes de 20");

let d10 = (restante - (restante % 10)) / 10;
restante %= 10;
if (d10 > 0) console.log(d10 + " billetes de 10");

let d5 = (restante - (restante % 5)) / 5;
restante %= 5;
if (d5 > 0) console.log(d5 + " billetes de 5");

if (restante > 0) console.log(restante + " billetes de 1");
}

// Prueba
cajero(2006);