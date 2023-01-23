var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const notaA = parseFloat(lines.shift());
const notaB = parseFloat(lines.shift());
const pesoA = 3.5;
const pesoB = 7.5;

const mediaPonderada = (pesoA*notaA+pesoB*notaB)/(pesoA+pesoB);

console.log(`MEDIA = ${mediaPonderada.toFixed(5)}`);
