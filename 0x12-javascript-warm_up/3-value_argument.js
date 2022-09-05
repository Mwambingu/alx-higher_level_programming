#!/usr/bin/node
const listNum = process.argv;
let count = 0;
listNum.forEach(function () {
  count++;
});
if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log(listNum[2]);
} else {
  console.log('Arguments found');
}
