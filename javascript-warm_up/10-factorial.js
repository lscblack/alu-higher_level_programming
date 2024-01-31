#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n < 0) return 1;
  if (n === 1 || n === 0) return 1;
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
