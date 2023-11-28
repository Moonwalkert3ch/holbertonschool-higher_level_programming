#!/usr/bin/node

const x = process.argv[2];

const count = parseInt(x);

if (!isNaN(count)) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences')
}
