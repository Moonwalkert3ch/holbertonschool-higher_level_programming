#!/usr/bin/node
const request = require('request');
const filePath = process.argv[2];

request.get(filePath).on('response', function (response) {
  console.log('code: ${response.statusCode}');
});
