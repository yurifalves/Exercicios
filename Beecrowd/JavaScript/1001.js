var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
    
const a = parseInt(lines.shift());
const b = parseInt(lines.shift());

console.log(`X = ${a+b}`);
