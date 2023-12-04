#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileOutput = process.argv[3];

request(url, 'utf8', function (error, response, body) {
  if (error) {
    console.error(`Error code: ${error}`);
  } else if (response.statusCode === 200) {
    fs.writeFile(fileOutput, body, 'utf8', (err) => {
      if (err) {
        console.error(`${err}`);
      } else {
        console.log(`${fileOutput}`);
      }
    });
  }
});
