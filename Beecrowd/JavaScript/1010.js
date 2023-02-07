var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const informacoesPeca1 = lines.shift();
const informacoesPeca2 = lines.shift();

const valorTotal = preco(informacoesPeca1) + preco(informacoesPeca2);

console.log(`VALOR A PAGAR: R$ ${valorTotal.toFixed(2)}`);

function preco(informacoesPeca) {
    const arrayInformacoesPeca = informacoesPeca.split(' ');
    const qtdPecas = parseInt(arrayInformacoesPeca[1]), valorPeca = parseFloat(arrayInformacoesPeca[2]);

    return qtdPecas*valorPeca;
}
