#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2);

fs.writeFile(file[0], file[1], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
