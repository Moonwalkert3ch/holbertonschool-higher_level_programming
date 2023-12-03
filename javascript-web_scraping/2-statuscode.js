#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('An error has occured');
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
