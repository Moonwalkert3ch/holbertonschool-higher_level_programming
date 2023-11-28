#!/usr/bin/node

const numberArgument = process.argv[2];
const numberValue = parseInt(numberArgument);
if (!isNaN(numberValue)) {
  console.log(`My number: ${numberValue}`);
} else {
  console.log('Not a number');
}
