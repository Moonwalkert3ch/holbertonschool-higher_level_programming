#!/usr/bin/node

const args = process.argv.slice(2);
const argToNumber = args.map(arg => parseInt(arg));
const numbers = argToNumber.filter(num => !isNaN(num));

if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedNum = numbers.sort((a, b) => b - a);
  console.log(sortedNum[1]);
}
