#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileOutput = process.argv[3];

request(url, function (err, body, response) {
  if (err) {
    console.error(`Error code: ${err}`);
  } else if (response.statusCode === 200) {
    fs.writeFile(fileOutput, body, 'utf8', (error) => {
      if (error) {
        console.error('An error has occurred');
      }
    });
  }
});
