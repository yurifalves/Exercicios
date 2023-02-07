var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const numero = parseInt(lines.shift());
const horasTrabalhadas = parseInt(lines.shift());
const valorHora = parseFloat(lines.shift());

console.log(`NUMBER = ${numero}`);
console.log(`SALARY = U$ ${(horasTrabalhadas*valorHora).toFixed(2)}`);
