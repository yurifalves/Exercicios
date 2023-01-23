var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const a = parseInt(lines.shift());
const b = parseFloat(lines.shift());

console.log(`PROD = ${a*b}`);
