#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let yves = '';
    for (let z = 0; z < size; z++) {
      yves += 'X';
    }
    console.log(yves);
  }
}
