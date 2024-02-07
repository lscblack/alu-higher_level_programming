#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
