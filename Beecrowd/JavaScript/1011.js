var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const raio = lines.shift();

console.log(`VOLUME = ${volumeEsfera(raio).toFixed(3)}`);

function volumeEsfera(raio) {
    const pi = 3.14159;

    return 4/3 * pi * raio**3;
}
