var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const distanciaPercorrida = parseInt(lines.shift());
const combustivelGasto = parseFloat(lines.shift());
const consumoMedio = distanciaPercorrida/combustivelGasto;

console.log(`${consumoMedio.toFixed(3)} km/l`);
