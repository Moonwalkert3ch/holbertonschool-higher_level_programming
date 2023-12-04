#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileOutput = process.argv[3];

request(url, 'utf8', function (error, response, body) {
  if (error) {
    console.error(`Error code: ${err}`);
  } else if (response.statusCode === 200) {
    fs.writeFile(fileOutput, body, 'utf8', (err) => {
      if (err) {
        console.error('An error has occurred: ${err}');
      } else {
        console.log(`${fileOutput}`);
      }
    });
  }
});
