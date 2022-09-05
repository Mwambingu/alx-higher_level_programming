#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
