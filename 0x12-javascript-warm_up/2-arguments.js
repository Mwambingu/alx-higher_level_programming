#!/usr/bin/node
const listNum = process.argv.length;
if (listNum === 2) {
  console.log('No argument');
} else if (listNum === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
