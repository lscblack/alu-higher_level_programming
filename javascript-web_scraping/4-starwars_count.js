#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const parsedData = JSON.parse(body);
    const results = parsedData.results;
    let i = 0;
    results.forEach(result => {
      result.characters.forEach(characterUrl => {
        if (characterUrl.includes('18')) {
          i++;
        }
      });
    });
    console.log(i);
  }
});
