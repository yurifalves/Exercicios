var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function areaCircunferencia(raio) {
    const pi = 3.14159;
    return pi * raio**2;
}

const raio = parseFloat(lines.shift());
console.log(`A=${areaCircunferencia(raio).toFixed(4)}`);
