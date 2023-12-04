#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileOutput = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(`Error code: ${error}`);
  } else if (response.statusCode === 200) {
    fs.writeFile(fileOutput, body, 'utf-8', (err) => {
      if (err) {
        console.error(`${err}`);
      }
    });
  }
});
