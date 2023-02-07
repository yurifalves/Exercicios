var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const valores = lines.shift().split(' ');

const a = parseFloat(valores[0]);
const b = parseFloat(valores[1]);
const c = parseFloat(valores[2]);

console.log(`${Math.max(a, b, c)} eh o maior`);
