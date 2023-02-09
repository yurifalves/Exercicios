var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const distanciaFinal = lines.shift();  // Km
const diferencaDasVelocidades = 30;  // Km/h
const tempoNecessario = distanciaFinal / diferencaDasVelocidades;  // h

console.log(`${60 * tempoNecessario} minutos`);
