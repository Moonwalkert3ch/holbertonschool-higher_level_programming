#!/usr/bin/node

const size = process.argv[2];
const squares = parseInt(size);

if (!isNaN(squares)) {
  for (let i = 0; i < squares; i++) {
    let row = '';
    for (let j = 0; j < squares; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
