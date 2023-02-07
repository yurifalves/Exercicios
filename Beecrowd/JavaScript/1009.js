var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const vendedor = lines.shift();
const salarioFixo = parseInt(lines.shift());
const valorVendido = parseFloat(lines.shift());

const salarioFinal = salarioFixo + 0.15*valorVendido;
console.log(`TOTAL = R$ ${salarioFinal.toFixed(2)}`);
