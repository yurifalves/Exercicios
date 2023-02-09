var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const valores = lines.shift().split(' ').map(valor => parseFloat(valor));

const a = valores[0];
const b = valores[1];
const c = valores[2];

console.log(`TRIANGULO: ${areaTriangulo(a, c).toFixed(3)}`);
console.log(`CIRCULO: ${areaCirculo(c).toFixed(3)}`);
console.log(`TRAPEZIO: ${areaTrapezio(a, b, c).toFixed(3)}`);
console.log(`QUADRADO: ${areaQuadrado(b).toFixed(3)}`);
console.log(`RETANGULO: ${areaRetangulo(a, b).toFixed(3)}`);

function areaTriangulo(base, altura) {
    return (base*altura)/2;
}

function areaCirculo(raio) {
    const pi = 3.14159;
    return pi*raio**2;
}

function areaTrapezio(base1, base2, altura) {
    return ((base1+base2)*altura)/2;
}

function areaQuadrado(lado) {
    return Math.pow(lado, 2);
}

function areaRetangulo(base, altura) {
    return base*altura;
}
