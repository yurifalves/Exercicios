var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const notaA = parseFloat(lines.shift());
const notaB = parseFloat(lines.shift());
const notaC = parseFloat(lines.shift());
const pesoA = 2;
const pesoB = 3;
const pesoC = 5;

const mediaPonderada = (pesoA*notaA+pesoB*notaB+pesoC*notaC)/(pesoA+pesoB+pesoC);

console.log(`MEDIA = ${mediaPonderada.toFixed(1)}`);
