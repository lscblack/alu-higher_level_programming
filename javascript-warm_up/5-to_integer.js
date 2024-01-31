#!/usr/bin/node
const input = process.argv[2];
const isNumber = !isNaN(parseInt(input));

if (isNumber) {
  console.log(`My number: ${parseInt(input)}`);
} else {
  console.log('Not a number');
}
