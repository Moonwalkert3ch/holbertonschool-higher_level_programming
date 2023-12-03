#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

function stringToFile(filePath, data) {
  fs.stringFile(filePath, data, 'utf8', (error) => {
    if (error) {
      console.error('An error has occurred');
    }
  });
}
stringToFile(filePath, content);
