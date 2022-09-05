#!/usr/bin/node
const listNum = process.argv.length
if (listNum === 3) {
  console.log('Argument found');
} else if (listNum < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
