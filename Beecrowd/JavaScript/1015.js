var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const dadosPonto1 = lines.shift().split(' ');
const dadosPonto2 = lines.shift().split(' ');
const x1 = parseFloat(dadosPonto1[0]);
const y1 = parseFloat(dadosPonto1[1]);
const x2 = parseFloat(dadosPonto2[0]);
const y2 = parseFloat(dadosPonto2[1]);

class Ponto {
    x;
    y;

    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

function distanciaPontos(ponto1, ponto2) {
    return Math.sqrt((ponto1.x - ponto2.x)**2 + (ponto1.y - ponto2.y)**2);
}

const ponto1 = new Ponto(x1, y1);
const ponto2 = new Ponto(x2, y2);

console.log(`${distanciaPontos(ponto1, ponto2).toFixed(4)}`);
