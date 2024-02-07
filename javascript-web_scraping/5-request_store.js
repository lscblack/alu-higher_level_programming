#!/usr/bin/node
const requ = require('request');
const fs = require('fs');
const file = process.argv.slice(2);
requ(file[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file[1], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
